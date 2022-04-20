
# io::putInt():
#     // allocate stack
#     // load var in
#     // call function to print
#     // return to flow

# main:
#     // accumulator set to 5
#     // accumulator add 10
#     // save accumulator to parameter
#     // call io.putInt
#     // terminate main


# from .MIPSMachineCode import MIPSCode
from AST import *
from .MIPSEmitter import MIPSEmitter

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


class Register:
    ZERO    = '$zero'
    AT      = '$at'
    V0      = '$v0'
    V1      = '$v1'
    A0      = '$a0'
    A1      = '$a1'
    A2      = '$a2'
    A3      = '$a3'

    T0      = '$t0'
    T1      = '$t1'
    T2      = '$t2'
    T3      = '$t3'
    T4      = '$t4'
    T5      = '$t5'
    T6      = '$t6'
    T7      = '$t7'
    T8      = '$t8'
    T9      = '$t9'

    S0      = '$s0'
    S1      = '$s1'
    S2      = '$s2'
    S3      = '$s3'
    S4      = '$s4'
    S5      = '$s5'
    S6      = '$s6'
    S7      = '$s7'

    K0      = '$k0'
    K1      = '$k1'

    GP = '$gp'
    SP = '$sp'
    FP = '$fp'
    RA = '$ra'


class MIPSCodeGenVisitor:
    
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.path = dir_
        self.className = "BKOOLClass"
        self.emit = MIPSEmitter(self.path + "/" + self.className + ".asm")

    def visit(self,ast,param):
        return ast.accept(self,param)


    def visitProgram(self, ast: Program, c):
        self.emit.printout(self.emit.emitPROLOG())

        for x in ast.decl:
            self.visit(x, c)
        
        self.emit.emitEPILOG()

    def visitClassDecl(self, ast: ClassDecl, o):
        for x in ast.memlist:
            self.visit(x, o)

    def visitMethodDecl(self, ast: MethodDecl, o):
        for x in ast.body.inst:
            self.visit(x, o)
    

    def visitCallStmt(self, ast: CallStmt, o):
        for x in ast.param:
            is_float = type(self.visit(x, o)) == FloatType
    
        self.emit.printout(self.emit.emitPRINTFLOAT() if is_float else self.emit.emitPRINTINT())
        
    def visitBinaryOp(self, ast: BinaryOp, o):
        op = ast.op

        if op == '+':
            ltype = self.visit(ast.left, o)
            rtype = self.visit(ast.right, o)

            if type(ltype) == FloatType or type(rtype) == FloatType:
                if type(ltype) != type(rtype):
                    self.emit.printout(self.emit.emitMERGEFLOATINT())
                return FloatType()
            else:
                return IntType()


    def visitIntLiteral(self, ast: IntLiteral, o):
        self.emit.printout(self.emit.emitADDINT(ast.value))
        return IntType()


    def visitFloatLiteral(self, ast: FloatLiteral, o):
        self.emit.printout(self.emit.emitADDFLOAT(str(ast.value)))
        return FloatType()
