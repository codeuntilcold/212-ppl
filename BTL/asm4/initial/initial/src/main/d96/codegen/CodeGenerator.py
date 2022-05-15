'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
            Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
            Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
            Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
        ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)


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


def retrieveType(origin):
    return ArrayPointerType(origin.eleType) if type(origin) is ArrayType else origin


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "D96Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast: Program, c):
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        
        e = SubBody(None, self.env)
        for x in ast.decl:
            e = self.visit(x, e)
        
        # generate default constructor
        self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(), None, Block(list() + list())), c, Frame("<init>", VoidType()))
        self.emit.emitEPILOG()
        return c

    def visitClassDecl(self, ast: ClassDecl, o: SubBody):
        subctx = o

        for x in ast.memlist:
            self.visit(x, subctx)

    def visitMethodDecl(self, ast: MethodDecl, o: SubBody):
        subctxt = o
        frame = Frame(ast.name, ast.returnType)

        self.genMETHOD(ast, subctxt.sym, frame)
        # return SubBody(None, [Symbol(ast.name, MType(list(), ast.returnType), CName(self.className))] + subctxt.sym)

    def genMETHOD(self, decl: MethodDecl, o: List[Symbol], frame: Frame):

        glenv = o

        methodName = decl.name.name
        isInit = decl.returnType is None and methodName == "<init>"
        isMain = methodName == "main" and len(decl.param) == 0 and type(decl.returnType) is VoidType
        returnType = VoidType() if isInit else decl.returnType
        intype = [ArrayPointerType(StringType())] if isMain else [retrieveType(x.varType) for x in decl.param]
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", 
                ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", 
                ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        body = decl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()


    def visitCallStmt(self, ast: CallStmt, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
        ctype = sym.mtype

        in_ = ("", list())
        for x in ast.param:
            parCode, parType = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + parCode, in_[1].append(parType))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))

        
    def visitBinaryOp(self, ast: BinaryOp, o):
        ctxt = o
        frame = ctxt.frame
        op = ast.op

        if op == '+':
            lcode, ltype = self.visit(ast.left, ctxt)
            rcode, rtype = self.visit(ast.right, ctxt)

            mtype = ltype
            if type(ltype) is not type(rtype):
                mtype = FloatType()
                if type(ltype) is IntType: lcode = lcode + self.emit.emitI2F(frame)
                else: rcode = rcode + self.emit.emitI2F(frame)

            return lcode + rcode + self.emit.emitADDOP(op, mtype, frame), mtype


    def visitIntLiteral(self, ast: IntLiteral, o):
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, o):
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()
