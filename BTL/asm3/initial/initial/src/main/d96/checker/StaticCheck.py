
"""
 * @author nhphung
"""
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
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType()))
    ]

    def __init__(self, ast):
        self.ast = ast
 
    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)


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
        if parent_cname and not parent_cname in c:
            raise Undeclared(Class(), parent_cname)
        
        # Holds an array of Symbols
        c[cname] = []
        # Pass the global class env and also name of current class for members
        return [self.visit(mem, (c, cname)) for mem in ast.memlist]
    

    def visitAttributeDecl(self, ast: AttributeDecl, classes):
        cname = classes[1]
        decl = ast.decl
        is_const = isinstance(decl, ConstDecl)
        attr_name = decl.constant.name if is_const else decl.variable.name
        if len(classes[0][cname]) > 0 and self.lookup(attr_name, classes[0][cname], lambda sym: sym.sym.name):
            raise Redeclared(Attribute(), attr_name)

        is_static = isinstance(ast.kind, Static)
        typ = decl.constType if is_const else decl.varType, classes
        classes[0][cname].append(MemSymbol(is_static, Symbol(attr_name, typ)))
    

    def visitMethodDecl(self, ast: MethodDecl, classes):
        cname = classes[1]
        method_name = ast.name.name
        if len(classes[0][cname]) > 0 and self.lookup(method_name, classes[0][cname], lambda sym: sym.sym.name):
            raise Redeclared(Method(), method_name)
        
        env = [[Symbol(p.variable.name, p.varType) for p in ast.param]] + [classes[0]]
        for i in range(len(env[0]) - 1):
            cur = env[0][i]
            rest = env[0][i+1:]
            if self.lookup(cur.name, rest, lambda sym: sym.name):
                raise Redeclared(Parameter(), cur.name)
            
        partype = [p.varType for p in ast.param]
        rettype = self.visit(ast.body, env)

        is_static = isinstance(ast.kind, Static)
        classes[0][cname].append(MemSymbol(is_static, Symbol(method_name, MType(partype, rettype))))


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

        if isinstance(ast.varType, ClassType):
            if not self.lookup(ast.varType.classname.name, stack[-1], lambda x: x):
                raise Undeclared(Class(), ast.varType.classname.name)

        if ast.varInit:
            self.visit(ast.varInit, stack)

        stack[0].append(Symbol(varname, ast.varType, False))


    def visitConstDecl(self, ast: ConstDecl, stack):
        constname = ast.constant.name
        if self.lookup(constname, stack[0], lambda sym: sym.name):
            raise Redeclared(Constant(), constname)
        stack[0].append(Symbol(constname, ast.varType, False))

        # TODO: Check static evaluation
        def check_static_eval(expr):
            pass

        check_static_eval(ast.value)

        # if ast.constType == self.visit(ast.value, c):
        #     return Symbol(ast.constant.name, ast.constType, self.visit(ast.value, c))
        # else:
        #     raise TypeMismatchInStatement(ast)

        return Symbol(ast.constant.name, ast.constType)


    def visitAssign(self, ast: Assign, c):
        self.visit(ast.lhs, c)
        self.visit(ast.exp, c)
        return None


    def visitCallStmt(self, ast: CallStmt, c):
        method_name = ast.method.name
        
        if ast.obj.name == "io" and self.lookup(method_name, StaticChecker.global_envi, lambda sym: sym.name):
            pass
        else:
            raise Undeclared(Method(), method_name)
        
        #ast.param

        return None

    

    def visitIf(self, ast: If, c):
        return None

    def visitFor(self, ast: For, c):
        return None

    def visitReturn(self, ast: Return, c):
        return None

    def visitBreak(self, ast: Break, c):
        return None

    def visitContinue(self, ast: Continue, c):
        return None

    def visitCallExpr(self, ast: CallExpr, c): 
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Method(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return res.mtype.rettype
    

    def visitId(self, ast: Id, c):
        not_glob_env = c[:-1]
        for scope in not_glob_env:
            res = self.lookup(ast.name, scope, lambda sym: sym.name)
            if res: return res
        raise Undeclared(Identifier(), ast.name)


    def visitBinaryOp(self, ast: BinaryOp, c):
        return None

    def visitUnaryOp(self, ast: UnaryOp, c):
        return None

    def visitNewExpr(self, ast: NewExpr, c):
        return None

    def visitArrayCell(self, ast: ArrayCell, c):
        return None

    def visitFieldAccess(self, ast: FieldAccess, stack):
        rettype = VoidType()
        if isinstance(ast.obj, Id):
            if not self.lookup(ast.obj.name, stack[-1], lambda x: x):
                raise Undeclared(Class(), ast.varType.classname.name)
            name = self.lookup(ast.fieldname, stack[-1][ast.obj.name], lambda sym: sym.name)
            if not name:
                raise Undeclared(Attribute(), ast.fieldname.name)
            else:
                rettype = name.mtype
        elif isinstance(ast.obj, FieldAccess):
            self.visit(ast.obj, stack)
            name = self.lookup(ast.fieldname, stack[-1][ast.obj.fieldname], lambda sym: sym.name)
            if not name:
                raise Undeclared(Attribute(), ast.fieldname.name)
            else:
                rettype = name.mtype
        return rettype

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
