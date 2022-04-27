
"""
 * @author nhphung
"""
from ast import arg
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, is_const = False):
        self.name = name
        self.mtype = mtype
        self.is_const = is_const


class MemSymbol:
    def __init__(self, is_static, sym):
        self.is_static = is_static
        self.sym = sym


class StaticChecker(BaseVisitor,Utils):

    libname = "io"
    global_envi = [
        MemSymbol(False, Symbol("getInt", MType([], IntType()))),
        MemSymbol(False, Symbol("putIntLn", MType([IntType()], VoidType())))
    ]

    def __init__(self, ast):
        self.ast = ast
 
    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)


    """
            HELPERS
    """
    @staticmethod
    def check_undeclared_class(classtype, stack):
        if isinstance(classtype, ClassType) and not classtype.classname.name in stack[-1]:
            raise Undeclared(Class(), classtype.classname.name)
        return classtype

    @staticmethod
    def log(msg):
        print('='*60)
        print(msg)
        print('='*60)

    """
            VISITORS
    """
    def visitProgram(self, ast: Program, c):
        # Check for Undeclared/Redeclared first
        env = { StaticChecker.libname: StaticChecker.global_envi }
        ret = [self.visit(decl, env) for decl in ast.decl]

        # Check for entry
        program_class = self.lookup("Program", ast.decl, lambda decl: decl.classname.name)
        if program_class is None or not any(
            isinstance(mem, MethodDecl) 
                and mem.name.name == "main" 
                and len(mem.param) == 0
            for mem in program_class.memlist
        ):
            raise NoEntryPoint()
        
        return ret 


    def visitClassDecl(self, ast: ClassDecl, c):
        cname = ast.classname.name
        parent_cname = ast.parentname.name if ast.parentname else None

        if cname in c:
            raise Redeclared(Class(), cname)
        c[cname] = []
        
        if parent_cname:
            if not parent_cname in c:
                raise Undeclared(Class(), parent_cname)
            else:
                pass
                # TODO: Support polymorphism

        # Holds an array of Symbols
        # Pass the global class env and also name of current class for members
        [self.visit(mem, (c, cname)) for mem in ast.memlist]


    def visitAttributeDecl(self, ast: AttributeDecl, classes):
        cname = classes[1]
        decl = ast.decl
        is_const = isinstance(decl, ConstDecl)
        attr_name = decl.constant.name if is_const else decl.variable.name
        if len(classes[0][cname]) > 0 and self.lookup(attr_name, classes[0][cname], lambda sym: sym.sym.name):
            raise Redeclared(Attribute(), attr_name)

        is_static = isinstance(ast.kind, Static)
        typ = decl.constType if is_const else decl.varType
        StaticChecker.check_undeclared_class(typ, classes[0])

        classes[0][cname].append(MemSymbol(is_static, Symbol(attr_name, typ, is_const)))
    

    def visitMethodDecl(self, ast: MethodDecl, classes):
        cname = classes[1]
        method_name = ast.name.name
        if len(classes[0][cname]) > 0 and self.lookup(method_name, classes[0][cname], lambda sym: sym.sym.name):
            raise Redeclared(Method(), method_name) if method_name not in ['Constructor, Destructor'] else \
                Redeclared(SpecialMethod(), method_name)
        
        stack = [[Symbol(p.variable.name, p.varType) for p in ast.param]] + [classes[0]]
        for i in range(len(stack[0]) - 1):
            cur = stack[0][i]
            rest = stack[0][i+1:]
            StaticChecker.check_undeclared_class(cur.mtype, stack) 
            if self.lookup(cur.name, rest, lambda sym: sym.name):
                raise Redeclared(Parameter(), cur.name)
            
        partype = [p.varType for p in ast.param]
        rettype = self.visit(ast.body, stack)

        is_static = isinstance(ast.kind, Static)
        classes[0][cname].append(MemSymbol(
            is_static, 
            Symbol(method_name, MType(partype, rettype))
        ))


    def visitBlock(self, ast: Block, stack):
        rettype = VoidType()
        for stmt in ast.inst:    
            self.visit(stmt, stack)
            if isinstance(stmt, Return):
                rettype = self.visit(stmt, stack)
        return rettype


    def visitVarDecl(self, ast: VarDecl, stack):
        varname = ast.variable.name
        if self.lookup(varname, stack[0], lambda sym: sym.name):
            raise Redeclared(Variable(), varname)
        StaticChecker.check_undeclared_class(ast.varType, stack)

        if ast.varInit and type(ast.varType) != type(self.visit(ast.varInit, stack)):
            raise TypeMismatchInStatement(ast)

        stack[0].append(Symbol(varname, ast.varType, False))


    def visitConstDecl(self, ast: ConstDecl, stack):
        constname = ast.constant.name
        if self.lookup(constname, stack[0], lambda sym: sym.name):
            raise Redeclared(Constant(), constname)
        StaticChecker.check_undeclared_class(ast.constType, stack)

        if ast.value:
            if type(ast.constType) != type(self.visit(ast.value, stack)):
                raise TypeMismatchInConstant(ast)
            
            # TODO: Check static evaluation
            def cannot_be_evaluated_statically(expr):
                if isinstance(expr, Literal):
                    return False
                else:
                    return False
            if cannot_be_evaluated_statically(ast.value):
                raise IllegalConstantExpression(ast.value)

        stack[0].append(Symbol(constname, ast.constType, True))


    def visitAssign(self, ast: Assign, c):
        # TODO: Should return a Symbol to check for constant?
        typ1, is_constant = self.visit(ast.lhs, c)
        if is_constant:
            raise CannotAssignToConstant(ast)
    
        typ2 = self.visit(ast.exp, c)
        if isinstance(typ2, tuple): typ2 = typ2[0]
        if type(typ1) != type(typ2):
            raise TypeMismatchInStatement(ast)


    def visitCallStmt(self, ast: CallStmt, stack):
        method_name = ast.method.name
        # TODO: Check method is declared
        if isinstance(ast.obj, Id):
            if ast.obj.name in stack[-1]:
                method_sym = self.lookup(method_name, stack[-1][ast.obj.name], lambda sym: sym.sym.name)
                if not method_sym:
                    raise Undeclared(Method(), method_name)
                # Check param len
                if len(ast.param) != len(method_sym.sym.mtype.partype):
                    raise TypeMismatchInStatement(ast)
                # Check param type
                partype = [type(par) for par in method_sym.sym.mtype.partype]
                for (arg, ptype) in list(zip(ast.param, partype)):
                    vartype = type(self.visit(arg, stack))
                    if vartype != ptype:
                        raise TypeMismatchInExpression(arg)
            else:
                raise Undeclared(Class(), method_name)
        else:
            self.visit(ast.obj, stack)



    def visitIf(self, ast: If, c):
        typ = self.visit(ast.expr, c)
        if not isinstance(typ, BoolType):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, c)
        self.visit(ast.elseStmt, c)
        return None


    def visitFor(self, ast: For, stack):
        ast.expr1
        ast.expr2
        ast.expr3
        ast.id
        stack[0].append(Symbol("For", VoidType()))
        self.visit(ast.loop, stack)
        stack[0] = filter(lambda sym: sym.name != "For", stack[0])


    def visitBreak(self, ast: Break, stack):
        # somehow stack must know that there is a loop being called
        for scope in stack[:-1]:
            if self.lookup("For", scope, lambda sym: sym.name if isinstance(sym, Symbol) else sym.sym.name):
                return
        raise MustInLoop(ast)


    def visitContinue(self, ast: Continue, stack):
        for scope in stack[:-1]:
            if self.lookup("For", scope, lambda sym: sym.name if isinstance(sym, Symbol) else sym.sym.name):
                return
        raise MustInLoop(ast)


    def visitReturn(self, ast: Return, c):
        return self.visit(ast.expr, c) if ast.expr else VoidType()

    # WIP
    def visitCallExpr(self, ast: CallExpr, stack): 
        method_name = ast.method.name
        # TODO: Check method is declared
        if isinstance(ast.obj, Id):
            if ast.obj.name in stack[-1]:
                method_sym = self.lookup(method_name, stack[-1][ast.obj.name], lambda sym: sym.sym.name)
                
                # Check param len
                if method_sym and len(ast.param) != len(method_sym.sym.mtype.partype):
                    raise TypeMismatchInExpression(ast)
            else:
                raise Undeclared(Method(), method_name)
        else:
            self.visit(ast.obj, stack)
    

    def visitId(self, ast: Id, c):
        not_glob_env = c[:-1]
        for scope in not_glob_env:
            res = self.lookup(ast.name, scope, lambda sym: sym.name)
            if res: return res, res.is_const
        raise Undeclared(Identifier(), ast.name)


    def visitBinaryOp(self, ast: BinaryOp, c):
        ast.left
        ast.right
        ast.op
        return None


    def visitUnaryOp(self, ast: UnaryOp, c):
        ast.op
        ast.body
        return None


    def visitNewExpr(self, ast: NewExpr, c):
        ast.classname
        ast.param
        return None


    def visitArrayCell(self, ast: ArrayCell, c):
        return None


    def visitFieldAccess(self, ast: FieldAccess, stack):
        rettype = VoidType()
        is_const = False
        classes = stack[-1]
        field = ast.fieldname.name

        if isinstance(ast.obj, Id):
            class_name = ast.obj.name
            if not self.lookup(class_name, classes, lambda x: x):
                raise Undeclared(Class(), class_name)

            attr_name = self.lookup(field, classes[class_name], lambda sym: sym.sym.name if isinstance(sym, MemSymbol) else sym.name)
            if not attr_name:
                raise Undeclared(Attribute(), field)
            else:
                rettype = attr_name.mtype if isinstance(attr_name, Symbol) else attr_name.sym.is_const
                is_const = attr_name.is_const if isinstance(attr_name, Symbol) else attr_name.sym.is_const
        
        elif isinstance(ast.obj, FieldAccess):
            self.visit(ast.obj, stack)
            attr_name = self.lookup(field, classes[ast.obj.fieldname], lambda sym: sym.sym.name if isinstance(sym, MemSymbol) else sym.name)
            if not attr_name:
                raise Undeclared(Attribute(), field)
            else:
                rettype = attr_name.mtype if isinstance(attr_name, Symbol) else attr_name.sym.is_const
                is_const = attr_name.is_const if isinstance(attr_name, Symbol) else attr_name.sym.is_const
        
        # print('='*60)
        # print(field + " is " + str(is_const))
        # print('='*60)
        return rettype, is_const


    def visitIntLiteral(self, ast: IntLiteral, c): 
        return IntType()


    def visitFloatLiteral(self, ast: FloatLiteral, c):
        return FloatType()


    def visitStringLiteral(self, ast: StringLiteral, c):
        return StringType()


    def visitBooleanLiteral(self, ast: BooleanLiteral, c):
        return BoolType()


    # TODO: implement
    def visitArrayLiteral(self, ast: ArrayLiteral, c):
        ele_type = self.visit(ast.value[0], c)
        if any(ele_type != self.visit(ele, c) for ele in ast.value):
            raise IllegalArrayLiteral(ast)

        array_dim = len(ast.value) + ele_type.size if isinstance(ele_type, ArrayType) else len(ast.value)
        while isinstance(ele_type, ArrayType):
            ele_type = ele_type.eleType

        return ArrayType(array_dim, ele_type)
