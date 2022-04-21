
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
    def __init__(self, name, mtype, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value


class MemSymbol():
    def __init__(self, kind, is_const, sym):
        self.kind = kind
        self.is_const = is_const or False
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
        # TBD: Check for Undeclared/Redeclared first then main ???
        env = [{ StaticChecker.libname: StaticChecker.global_envi }]
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

        if cname in c[0]:
            raise Redeclared(Class(), cname)
        if parent_cname and not parent_cname in c[0]:
            raise Undeclared(Class(), parent_cname)
        
        c[0][cname] = [] # Holds an array of symbols
        return [self.visit(mem, c[0][cname]) for mem in ast.memlist]
    

    def visitAttributeDecl(self, ast: AttributeDecl, c):
        if isinstance(ast.decl, VarDecl):
            attr_name = ast.decl.variable.name  
            if len(c) > 0 and self.lookup(attr_name, c, lambda sym: sym.sym.name):
                raise Redeclared(Attribute(), attr_name)
            c.append(MemSymbol(ast.kind, False, self.visit(ast.decl, c)))
        else:
            attr_name = ast.decl.constant.name
            if len(c) > 0 and self.lookup(attr_name, c, lambda sym: sym.sym.name):
                raise Redeclared(Attribute(), attr_name)
            c.append(MemSymbol(ast.kind, True, self.visit(ast.decl, c)))
    

    def visitMethodDecl(self, ast: MethodDecl, c):
        method_name = ast.name.name
        if len(c) > 0 and self.lookup(method_name, c, lambda sym: sym.sym.name):
            raise Redeclared(Method(), method_name)
        
        env = [[]] + c
        partype = [p.varType for p in ast.param]
        rettype = self.visit(ast.body, env)

        c.append(MemSymbol(ast.kind, False, Symbol(method_name, MType(partype, rettype))))


    def visitBlock(self, ast: Block, c):
        for stmt in ast.inst:
            self.visit(stmt, c)

    def visitVarDecl(self, ast: VarDecl, c):
        return Symbol(ast.variable.name, ast.varType, None)#self.visit(ast.varInit, c))

    def visitConstDecl(self, ast: ConstDecl, c):
        # TODO: Check static evaluation
        def check_static_eval(expr):
            pass

        check_static_eval(ast.value)

        # if ast.constType == self.visit(ast.value, c):
        #     return Symbol(ast.constant.name, ast.constType, self.visit(ast.value, c))
        # else:
        #     raise TypeMismatchInStatement(ast)

        return Symbol(ast.constant.name, ast.constType)

    def visitCallStmt(self, ast: CallStmt, c):
        method_name = ast.method.name
        
        if ast.obj.name == "io" and self.lookup(method_name, StaticChecker.global_envi, lambda sym: sym.name):
            pass
        else:
            raise Undeclared(Method(), method_name)
        
        #ast.param

        return None

    def visitAssign(self, ast: Assign, c):
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
        return None

    def visitBinaryOp(self, ast: BinaryOp, c):
        return None

    def visitUnaryOp(self, ast: UnaryOp, c):
        return None

    def visitNewExpr(self, ast: NewExpr, c):
        return None

    def visitArrayCell(self, ast: ArrayCell, c):
        return None

    def visitFieldAccess(self, ast: FieldAccess, c):
        return None

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
