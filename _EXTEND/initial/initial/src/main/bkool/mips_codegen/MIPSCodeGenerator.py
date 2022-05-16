# from .MIPSMachineCode import MIPSCode
from AST import *
from StaticCheck import Symbol
from .MIPSEmitter import MIPSEmitter

class StringType(Type):
    def __str__(self):
        return "StringType"
    def accept(self, v, param):
        return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype
    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))
    def accept(self, v, param):
        return None

class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None

class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]
        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int
        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String
        self.value = value

class MIPSCodeGenerator:

    def init(self):
        return [
            # Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
            # Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
            # Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
            # Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
        ]

    def gen(self, ast, dir_):

        global_env = self.init()
        global_codegen = MIPSCodeGenVisitor(ast, global_env, dir_)
        global_codegen.visit(ast, None)


class MIPSCodeGenVisitor:
    
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.path = dir_
        self.className = "D96"
        self.emit = MIPSEmitter(self.path + "/" + self.className + ".asm")

    def visit(self,ast,param):
        return ast.accept(self,param)


    def visitProgram(self, ast: Program, c):
        # self.emit.printout(self.emit.emitPROLOG())

        for x in ast.decl:
            self.visit(x, c)
        
        self.emit.emitEPILOG()


    def visitClassDecl(self, ast: ClassDecl, o):
        for x in ast.memlist:
            self.visit(x, o)


    def visitMethodDecl(self, ast: MethodDecl, o):
        self.emit.printout(self.emit.emitLABEL(ast.name.name))
        
        n_var = len(ast.param) + sum(type(stmt) in (VarDecl, ConstDecl) for stmt in ast.body.inst)        
        scope = SubBody(None, [])

        self.emit.printout(self.emit.emitUPONENTRANCE(n_var + 1))
        for x in ast.body.inst:
            self.visit(x, scope)
        self.emit.printout(self.emit.emitUPONEXIT(n_var + 1))
        
    
    def visitVarDecl(self, ast: VarDecl, o):
        # o: SubBody
        o.sym
        idx = len(o.sym)

        # First only consider initialized variables in main method
        if ast.varInit:
            code, _ = self.visit(ast.varInit, o)
            self.emit.printout(code)
            self.emit.printout(self.emit.emitSTOREINDEX(idx))

        o.sym.append(Symbol(ast.variable.name, ast.varType, Index(idx)))


    def visitAssign(self, ast: Assign, o):
        rc, _ = self.visit(ast.exp, o)
        self.emit.printout(rc)
        for sym in o.sym:
            if ast.lhs.name == sym.name:
                index = sym.value.value
                self.emit.printout(self.emit.emitSTOREINDEX(index))
        

    def visitCallStmt(self, ast: CallStmt, o):
        for x in ast.param:
            code, typ = self.visit(x, o)
            self.emit.printout(code)
            is_float = type(typ) == FloatType
    
        self.emit.printout(self.emit.emitPRINTFLOAT() if is_float else self.emit.emitPRINTINT())
        

    def visitBinaryOp(self, ast: BinaryOp, o):
        op = ast.op
        lc, lt = self.visit(ast.left, o)
        rc, rt = self.visit(ast.right, o)

        if op in '+-':
            if type(lt) == FloatType or type(rt) == FloatType:
                code = lc + self.emit.emitPUSHACC() + rc + self.emit.emitADDOP(op)
                if type(lt) != type(rt):
                    code += self.emit.emitMERGEFLOATINT()
                return code, FloatType()
            else:
                code = lc + self.emit.emitPUSHACC() + rc + self.emit.emitADDOP(op)
                return code, IntType()
        elif op in '*/':
            code = lc + self.emit.emitPUSHACC() + rc + self.emit.emitMULOP(op)
            return code, IntType()
        elif op in ['+.']:
            pass


    def visitId(self, ast: Id, o):
        for sym in o.sym:
            if ast.name == sym.name:
                idx = sym.value.value
        return self.emit.emitLOADINDEX(idx), IntType()


    def visitIntLiteral(self, ast: IntLiteral, o):
        return self.emit.emitLOADACC(ast.value), IntType()


    def visitFloatLiteral(self, ast: FloatLiteral, o):
        return self.emit.emitLOADACCF(str(ast.value)), FloatType()
