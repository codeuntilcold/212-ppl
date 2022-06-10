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
from abc import ABC

class CodeGenerator():
    def __init__(self):
        self.libName = "io"

    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None

    def init(self):
        return [
            Symbol("$readInt", MType(list(), IntType()), CName(self.libName)),
            Symbol("$writeInt", MType([IntType()], VoidType()), CName(self.libName)),
            Symbol("$writeIntLn", MType([IntType()], VoidType()), CName(self.libName)),

            Symbol("$readFloat", MType(list(), FloatType()), CName(self.libName)),
            Symbol("$writeFloat", MType([FloatType()], VoidType()), CName(self.libName)),
            Symbol("$writeFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),

            Symbol("$writeBool", MType([BoolType()], VoidType()), CName(self.libName)),
            Symbol("$writeBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),

            Symbol("$writeString", MType([StringType()], VoidType()), CName(self.libName)),
            Symbol("$writeStringLn", MType([StringType()], VoidType()), CName(self.libName)),
        ]

    def gen(self, ast, dir_):
        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class Symbol():
    def __init__(self, name, mtype, value):
        self.name = name
        self.mtype = mtype
        self.value = value

class StringType(Type):
    def __str__(self):
        return "StringType"
    def accept(self, v, param):
        return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
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
    def __init__(self, frame: Frame, sym: List[Symbol]):
        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame: Frame, sym: List[Symbol], isLeft: bool, isFirst: bool):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value: int):
        self.value = value

class CName(Val):
    def __init__(self, value: str):
        self.value = value


def retrieveType(origin):
    return ArrayPointerType(retrieveType(origin.eleType)) if type(origin) is ArrayType else origin

def hasReturnStmt(ast):
    if isinstance(ast, Block):
        return any(hasReturnStmt(stmt) for stmt in ast.inst)
    elif isinstance(ast, Return):
        return True
    elif isinstance(ast, If):
        has = hasReturnStmt(ast.thenStmt)
        if ast.elseStmt:
            has = has or hasReturnStmt(ast.elseStmt)
        return has
    elif isinstance(ast, For):
        return hasReturnStmt(ast.loop)
    else:
        return False

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree: Program, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "D96Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

        self.currClassName = None
        self.currMethodSym = None
        self.classes = {}

    """
            HELPERS
    """
    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None
    
    def generate(self):
        result = {}
        for decl in self.astTree.decl:
            classname = decl.classname.name
            result[classname] = {}
            for mem in decl.memlist:
                if isinstance(mem, AttributeDecl):
                    name = mem.decl.variable.name if isinstance(mem.decl, VarDecl) else \
                        mem.decl.constant.name
                    typ = mem.decl.varType if isinstance(mem.decl, VarDecl) else \
                        mem.decl.constType
                    result[classname][name] = typ
                elif isinstance(mem, MethodDecl):
                    name = mem.name.name
                    par = [p.varType for p in mem.param]
                    ret = VoidType()
                    result[classname][name] = MType(par, ret)
        return result
    
    def class_mapping(self, classname):
        if classname == 'Program': classname = 'D96Class'
        return classname

    """
            VISITORS
    """
    def visitProgram(self, ast: Program, c):
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        
        e = SubBody(None, self.env)
        for classdecl in ast.decl:
            self.visit(classdecl, e)
        
        # generate default constructor
        syms = c
        self.currMethodSym = Symbol("<init>", MType([], VoidType()), CName(self.className))
        self.genMETHOD(MethodDecl(Instance(), Id("<init>"), [], Block([
            # CallStmt(Id("Program"), Id("main"), [])
        ])), syms, Frame("<init>", VoidType()))

        self.emit.emitEPILOG()


    def genMETHOD(self, decl: MethodDecl, syms: List[Symbol], frame: Frame):
        method_name = decl.name.name
        is_init = method_name == "<init>"
        is_main = method_name == "main"
        is_static = '$' in method_name
        returnType = VoidType() if is_main else \
                     self.currMethodSym.mtype.rettype
        is_proc = type(returnType) is VoidType

        # Workaround for type inference
        self.emit.printout("TEMPORARY METHOD DIRECTIVE PLACEHOLDER")

        frame.enterScope(is_proc)

        sub = SubBody(frame, syms)

        # Generate code for parameter declarations
        if is_init:
            self.emit.printout(self.emit.emitVAR(
                frame.getNewIndex(), "this", ClassType(self.className), 
                frame.getStartLabel(), frame.getEndLabel(), frame))
        elif is_main:
            self.emit.printout(self.emit.emitVAR(
                frame.getNewIndex(), "args", ArrayPointerType(StringType()), 
                frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            # Generate Self if this is not static
            # if not is_static:
            #     self.emit.printout(self.emit.emitVAR(
            #         frame.getNewIndex(), "this", ClassType(self.currClassName), 
            #         frame.getStartLabel(), frame.getEndLabel(), frame))

            [self.visit(par, sub) for par in decl.param]
            

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if is_init:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        else:
            self.visit(decl.body, sub)

        # Re-confirm return type after (maybe) encountering return statement
        returnType = VoidType() if is_main else \
                     self.currMethodSym.mtype.rettype

        # End method
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

        
        partype = [ArrayPointerType(StringType())] if is_main else \
                  self.currMethodSym.mtype.partype
        mtype = MType(partype, returnType)
        
        self.emit.replace(
            "TEMPORARY METHOD DIRECTIVE PLACEHOLDER",
            self.emit.emitMETHOD(method_name, mtype, not is_init, frame)
        )


    def visitClassDecl(self, ast: ClassDecl, o: SubBody):
        self.currClassName = ast.classname.name
        self.classes[self.currClassName] = []
        [self.visit(x, o) for x in ast.memlist]


    def visitMethodDecl(self, ast: MethodDecl, o: SubBody):
        method_name = ast.name.name
        partype = [retrieveType(par.varType) for par in ast.param]

        # Default return type
        self.currMethodSym = Symbol(
            method_name, MType(partype, VoidType()), CName(self.class_mapping(self.currClassName))
        )
        self.classes[self.currClassName].append(self.currMethodSym)

        frame = Frame(method_name, self.currMethodSym.mtype.rettype)
        self.genMETHOD(ast, o.sym, frame)


    def visitAttributeDecl(self, ast: AttributeDecl, o: SubBody):
        is_const = not isinstance(ast.decl, VarDecl)
        is_static = isinstance(ast.kind, Static)

        if not is_const:
            name = ast.decl.variable.name
            typ = ast.decl.varType
            val = ast.decl.varInit
        else:
            name = ast.decl.constant.name
            typ = ast.decl.constType
            val = ast.decl.value

        val = val.value if isinstance(val, Literal) else val
        self.emit.printout(self.emit.emitFIELD(name, typ, is_static, is_const, val))

        if is_static:
            self.env.append(Symbol(name, typ, CName(self.currClassName)))
            # if val: self.visit(Assign(FieldAccess(Id(self.currClassName), Id(name)), val), o)
        else:
            self.classes[self.currClassName].append(
                Symbol(name, typ, CName(self.currClassName))
            )
            # if val: self.visit(Assign(FieldAccess(SelfLiteral(), Id(name)), val), o)


    def visitVarDecl(self, ast: VarDecl, o: SubBody):
        frame = o.frame
        varName = ast.variable.name
        varType = ast.varType
        idx = frame.getNewIndex()
        frame.push()
        self.emit.printout(self.emit.emitVAR(
            idx, varName, retrieveType(varType),
            frame.getStartLabel(), frame.getEndLabel(), frame
        ))
        
        o.sym = [Symbol(varName, varType, Index(idx))] + o.sym
        if ast.varInit and not isinstance(varType, ArrayType):
            self.visit(Assign(ast.variable, ast.varInit), o)
        elif isinstance(varType, ArrayType):
            size = varType.size
            et = retrieveType(varType.eleType)
            self.emit.printout(self.emit.emitPUSHICONST(size, frame))
            self.emit.printout(self.emit.emitNEWARRAY(et))
            
            if ast.varInit:
                for idx, val in enumerate(ast.varInit.value):
                    self.emit.printout(self.emit.emitDUP(frame))
                    self.emit.printout(self.emit.emitPUSHICONST(idx, frame))
                    vc, vt = self.visit(val, Access(o.frame, o.sym, False, True))
                    self.emit.printout(vc)
                    self.emit.printout(self.emit.emitASTORE(et, frame))
            self.emit.printout(self.emit.emitWRITEVAR(varName, retrieveType(varType), idx, frame))


    def visitConstDecl(self, ast: ConstDecl, o: SubBody):
        self.visit(VarDecl(ast.constant, ast.constType, ast.value), o)


    def visitAssign(self, ast: Assign, o: SubBody):
        frame = o.frame
        nenv = o.sym

        expCode, expType = self.visit(ast.exp, Access(frame, nenv, False, True))
        lhsCode, lhsType = self.visit(ast.lhs, Access(frame, nenv, True, True))
        if type(lhsType) is FloatType and type(expType) is IntType:
            expCode = expCode + self.emit.emitI2F(frame)
        
        if isinstance(ast.lhs, FieldAccess) and '$' not in ast.lhs.fieldname.name:
                # ... objectref, value -> result
            field_name = ast.lhs.fieldname.name
            field_type = self.lookup(field_name, self.classes[lhsType.cname], lambda sym: sym.name).mtype
            self.emit.printout(lhsCode + expCode + self.emit.emitPUTFIELD(field_name, field_type, o.frame))
        elif isinstance(ast.lhs, ArrayCell):
            # 1D array
            # lhsCode: [ref, idx, iastore]
            ref, idx, iastore = lhsCode[0], lhsCode[1], lhsCode[2]
            self.emit.printout(ref + idx + expCode + iastore)
        else:
            self.emit.printout(expCode + lhsCode)
        


    def visitBlock(self, ast: Block, o: SubBody):
        [self.visit(x, o) for x in ast.inst]


    def visitIf(self, ast: If, o: SubBody):
        frame = o.frame
        expCode, _ = self.visit(ast.expr, Access(frame, o.sym, False, True))
        self.emit.printout(expCode)

        false_lbl = str(frame.getNewLabel())
        exit_lbl = str(frame.getNewLabel())

        self.emit.printout(self.emit.emitIFFALSE(false_lbl, frame))

        frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.visit(ast.thenStmt, SubBody(o.frame, [] + o.sym))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()
        
        if ast.elseStmt:
            if not hasReturnStmt(ast.thenStmt):
                self.emit.printout(self.emit.emitGOTO(exit_lbl, frame))
                
            self.emit.printout(self.emit.emitLABEL(false_lbl, frame))
            frame.enterScope(False)
            self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
            self.visit(ast.elseStmt, SubBody(o.frame, [] + o.sym))
            self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
            frame.exitScope()

            self.emit.printout(self.emit.emitLABEL(exit_lbl, frame))
        else:
            self.emit.printout(self.emit.emitLABEL(false_lbl, frame))
            

    def visitFor(self, ast: For, o: SubBody):
        frame = o.frame
        nenv = o.sym

        exp1Code, _ = self.visit(ast.expr1, Access(frame, nenv, False, True))
        exp2Code, _ = self.visit(ast.expr2, Access(frame, nenv, False, True))
        exp3Code, _ = self.visit(ast.expr3, Access(frame, nenv, False, True))
        lhsWCode, _ = self.visit(ast.id, Access(frame, nenv, True, True))
        lhsRCode, _ = self.visit(ast.id, Access(frame, nenv, False, False))
        
        labelS = str(frame.getNewLabel())
        labelE = str(frame.getNewLabel())

        # Init value
        self.emit.printout(exp1Code)
        self.emit.printout(lhsWCode)

        # Compare e1 and e2, save on top of stack
        self.emit.printout(exp1Code)
        self.emit.printout(exp2Code)
        self.emit.printout(self.emit.emitREOP('<=', IntType(), frame))

        frame.enterLoop()
        # Loop
        self.emit.printout(self.emit.emitLABEL(labelS, frame))
        # 1. Condition
        lgt = str(frame.getNewLabel())
        llt = str(frame.getNewLabel())
        self.emit.printout(self.emit.emitDUP(frame))
        self.emit.printout(self.emit.emitIFFALSE(lgt, frame))

        self.emit.printout(lhsRCode)
        self.emit.printout(exp2Code)
        self.emit.printout(self.emit.emitIFICMPGT(labelE, frame))
        self.emit.printout(self.emit.emitGOTO(llt, frame))

        self.emit.printout(self.emit.emitLABEL(lgt, frame))
        self.emit.printout(lhsRCode)
        self.emit.printout(exp2Code)
        self.emit.printout(self.emit.emitIFICMPLT(labelE, frame))

        self.emit.printout(self.emit.emitLABEL(llt, frame))

        # 2. Statements
        self.visit(ast.loop, o)

        # 3. Update index
        lgt = str(frame.getNewLabel())
        llt = str(frame.getNewLabel())
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))
        self.emit.printout(self.emit.emitDUP(frame))
        self.emit.printout(self.emit.emitIFFALSE(lgt, frame))

        self.emit.printout(lhsRCode)
        self.emit.printout(exp3Code)
        self.emit.printout(self.emit.emitADDOP('+', IntType(), frame))
        self.emit.printout(lhsWCode)
        self.emit.printout(self.emit.emitGOTO(llt, frame))

        self.emit.printout(self.emit.emitLABEL(lgt, frame))
        self.emit.printout(lhsRCode)
        self.emit.printout(exp3Code)
        self.emit.printout(self.emit.emitADDOP('-', IntType(), frame))
        self.emit.printout(lhsWCode)

        self.emit.printout(self.emit.emitLABEL(llt, frame))

        self.emit.printout(self.emit.emitGOTO(labelS, frame))
        self.emit.printout(self.emit.emitLABEL(labelE, frame))
        
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))

        frame.exitLoop()


    def visitBreak(self, ast: Break, o: SubBody):
        self.emit.printout(self.emit.emitGOTO(str(o.frame.getBreakLabel()), o.frame))


    def visitContinue(self, ast: Continue, o: SubBody):
        self.emit.printout(self.emit.emitGOTO(str(o.frame.getContinueLabel()), o.frame))


    def visitReturn(self, ast: Return, o: SubBody):
        frame = o.frame
        nenv = o.sym
        if ast.expr:
            expCode, expType = self.visit(ast.expr, Access(frame, nenv, False, True))
            self.currMethodSym.mtype.rettype = expType
            self.emit.printout(expCode)
            self.emit.printout(self.emit.emitRETURN(expType, frame))
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))


    def visitCallStmt(self, ast: CallStmt, o: SubBody):
        frame = o.frame
        nenv = o.sym
        method_name = ast.method.name
        sym = self.lookup(method_name, nenv, lambda x: x.name)
        if sym:
            cname = sym.value.value
            mtype = sym.mtype
        else:
            sym = self.lookup(method_name, self.classes[self.currClassName], lambda x: x.name)
            cname = sym.value.value
            mtype = sym.mtype

        in_ = ''
        for x in ast.param:
            parCode, _ = self.visit(x, Access(frame, nenv, False, True))
            in_ += parCode
        self.emit.printout(in_)
        if cname == "io":
            method_name = method_name.replace("$write", "put")
            method_name = method_name.replace("$read", "get")
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + method_name, mtype, frame))


    def visitCallExpr(self, ast: CallExpr, o: Access):
        method_name = ast.method.name
        sym = self.lookup(method_name, o.sym, lambda x: x.name)
        if sym:
            cname = sym.value.value
            mtype = sym.mtype
        else:
            class_name = self.currClassName
            if '$' in method_name:
                class_name = ast.obj.name
            sym = self.lookup(method_name, self.classes[class_name], lambda x: x.name)
            cname = sym.value.value
            mtype = sym.mtype

        code = ''
        for x in ast.param:
            parCode, _ = self.visit(x, Access(o.frame, o.sym, False, True))
            code += parCode
        return code + self.emit.emitINVOKESTATIC(self.className + "/" + method_name, mtype, o.frame), mtype.rettype


    def visitFieldAccess(self, ast: FieldAccess, o: Access):
        field_name = ast.fieldname.name
        is_static = '$' in field_name
        
        if not o.isLeft:
            if is_static:
                for sym in o.sym:
                    if sym.name == field_name and sym.value.value == ast.obj.name:
                        field_type = sym.mtype
                        class_name = self.class_mapping(ast.obj.name)
                        return self.emit.emitGETSTATIC(class_name + "/" + field_name, field_type, o.frame), field_type
            else:
                code, cls = self.visit(ast.obj, Access(o.frame, o.sym, False, True))
                self.emit.printout(code)
                field_type = self.lookup(field_name, (cls.cname), lambda sym: sym.name).mtype
                return code + self.emit.emitGETFIELD(field_name, field_type, o.frame), field_type
        else:
            if is_static:
                for sym in o.sym:
                    if sym.name == field_name and sym.value.value == ast.obj.name:
                        field_type = sym.mtype
                        class_name = self.class_mapping(ast.obj.name)
                        return self.emit.emitPUTSTATIC(class_name + "/" + field_name, field_type, o.frame), field_type
            else:
                return self.visit(ast.obj, Access(o.frame, o.sym, False, True))


    def visitId(self, ast: Id, o: Access):
        frame = o.frame
        symbols = o.sym
        isLeft = o.isLeft
        isFirst = o.isFirst

        sym = self.lookup(ast.name, symbols, lambda x: x.name)

        # recover status of stack in frame
        if not isFirst and isLeft: frame.push()
        elif not isFirst and not isLeft: frame.pop()

        isArrayType = type(sym.mtype) is ArrayType
        emitType = retrieveType(sym.mtype)
        if sym.value is None:
            if isLeft and not isArrayType: retCode = self.emit.emitPUTSTATIC(self.className + "/" + sym.name, emitType, frame)
            else: retCode = self.emit.emitGETSTATIC(self.className + "/" + sym.name, emitType, frame)
        else:
            if isLeft and not isArrayType: retCode = self.emit.emitWRITEVAR(sym.name, emitType, sym.value.value, frame)
            else: retCode = self.emit.emitREADVAR(sym.name, emitType, sym.value.value, frame)

        return retCode, sym.mtype


    def visitArrayCell(self, ast: ArrayCell, o: Access):
        frame = o.frame
        symbols = o.sym
        isLeft = o.isLeft

        arrCode, arrType = self.visit(ast.arr, Access(frame, symbols, True, True))
        arrType = retrieveType(arrType)
        for idx in ast.idx:
            idxCode, _ = self.visit(idx, Access(frame, symbols, False, True))

        if isLeft:
            return [arrCode, idxCode, self.emit.emitASTORE(arrType.eleType, frame)], arrType.eleType
        
        return arrCode + idxCode + self.emit.emitALOAD(arrType.eleType, frame), arrType.eleType


    
    def visitBinaryOp(self, ast: BinaryOp, o: Access):
        frame = o.frame
        op = ast.op

        lCode, lType = self.visit(ast.left, o)
        rCode, rType = self.visit(ast.right, o)

        if op in ['+', '-', '*', '/', '%', '!=', '==', '>', '<', '>=', '<=']:
            mType = FloatType() if FloatType in [type(lType), type(rType)] else IntType()
            if type(lType) is IntType and type(mType) != type(lType): lCode = lCode + self.emit.emitI2F(frame)
            if type(rType) is IntType and type(mType) != type(rType): rCode = rCode + self.emit.emitI2F(frame)

            if op in ['+', '-']:
                return lCode + rCode + self.emit.emitADDOP(op, mType, frame), mType
            if op in ['*', '/']:
                return lCode + rCode + self.emit.emitMULOP(op, mType, frame), mType
            if op == '%':
                return lCode + rCode + self.emit.emitMOD(frame), mType
            else:
                return lCode + rCode + self.emit.emitREOP(op, mType, frame), BoolType()
        elif op in ['||', '&&']:
            # Short-circuit evaluation
            mType = BoolType()
            true_lbl = str(frame.getNewLabel())
            false_lbl = str(frame.getNewLabel())
            exit_lbl = str(frame.getNewLabel())
            code = lCode
            if op == '||':
                code += self.emit.emitIFTRUE(true_lbl, frame)
                code += rCode
                code += self.emit.emitIFFALSE(false_lbl, frame)

                code += self.emit.emitLABEL(true_lbl, frame)
                code += self.emit.emitPUSHICONST(1, frame)
                code += self.emit.emitGOTO(exit_lbl, frame)

                code += self.emit.emitLABEL(false_lbl, frame)
                code += self.emit.emitPUSHICONST(0, frame)

                code += self.emit.emitLABEL(exit_lbl, frame)
            elif op == '&&':
                code += self.emit.emitIFFALSE(false_lbl, frame)
                code += rCode
                code += self.emit.emitIFFALSE(false_lbl, frame)
                code += self.emit.emitPUSHICONST(1, frame)
                code += self.emit.emitGOTO(exit_lbl, frame)
                code += self.emit.emitLABEL(false_lbl, frame)
                code += self.emit.emitPUSHICONST(0, frame)
                code += self.emit.emitLABEL(exit_lbl, frame)
            return code, mType
        else:
            # TODO
            return lCode + rCode, StringType() if op == '+.' else BoolType()


    def visitUnaryOp(self, ast: UnaryOp, o: Access):
        frame = o.frame
        op = ast.op
        bCode, bType = self.visit(ast.body, o)
        if op == '-': return bCode + self.emit.emitNEGOP(bType, frame), bType
        if op == '!': return bCode + self.emit.emitNOT(bType, frame), bType


    def visitNewExpr(self, ast: NewExpr, o: Access):
        c = ''
        for expr in ast.param:
            code, _ = self.visit(expr, o)
            c += code
        return c + self.emit.emitINVOKESPECIAL(o.frame, ast.classname.name + "/Constructor", ClassType(ast.classname.name)), ClassType(ast.classname.name)


    def visitIntLiteral(self, ast: IntLiteral, o: Access):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()


    def visitFloatLiteral(self, ast: FloatLiteral, o: Access):
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), FloatType()


    def visitStringLiteral(self, ast: StringLiteral, o: Access):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()


    def visitBooleanLiteral(self, ast: BooleanLiteral, o: Access):
        return self.emit.emitPUSHICONST(str(ast.value).lower(), o.frame), BoolType()


    def visitArrayLiteral(self, ast: ArrayLiteral, o: Access):

        return '', ArrayPointerType(IntType())
        code = ''

        def dim(ele):
            if isinstance(ele, ArrayLiteral):
                return [len(ele.value)] + dim(ele.value[0])
            elif isinstance(ele, list):
                return [len(ele)] + dim(ele[0])
            else:
                return []
        dimension = dim(ast.value)
        # print(ast.value)
        print(dimension)
  
        for ele in ast.value:
            # Push elements onto stack
            c, t = self.visit(ele, o)
            code += c
        
        return '', ArrayPointerType(IntType())


    def visitNullLiteral(self, ast: NullLiteral, o: Access):
        return self.emit.emitNULL(), VoidType()


    def visitSelfLiteral(self, ast: SelfLiteral, o: Access):
        return self.emit.emitREADVAR("this", ClassType(self.className), 0, o.frame), ClassType(self.className)
