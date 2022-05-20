# from .MIPSMachineCode import MIPSCode
from AST import *
from .MIPSFrame import Frame
from StaticCheck import MType, Symbol
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
    def __init__(self, frame: Frame, sym: List[Symbol]):
        #frame: Frame
        #sym: List[Symbol]
        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame: Frame, sym: List[Symbol], isLeft, isFirst):
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
        self.libName = 'io'
        return [
            Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
            Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
            Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
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

        self.currentClassName = None
        self.currentMethodSym = None
        self.methodSyms = list()


    def visit(self,ast,param):
        return ast.accept(self,param)

    """
            HELPERS
    """


    """
            VISITORS
    """
    def visitProgram(self, ast: Program, c):
        for x in ast.decl:
            self.visit(x, c)
        
        self.emit.emitSOURCECODE()


    def visitClassDecl(self, ast: ClassDecl, o):
        self.currentClassName = ast.classname.name
        frame = Frame()
        for x in ast.memlist:
            self.visit(x, frame)


    def visitMethodDecl(self, ast: MethodDecl, o):
        self.methodSyms.append(Symbol(ast.name.name, MType([], VoidType()), CName(self.currentClassName)))
        self.currentMethodSym = self.methodSyms[-1]


        self.emit.printout(self.emit.emitLABEL(self.currentClassName + '_m_' + ast.name.name))
        
        # Count total num of var (including in sub-bodies)
        def count_local_var(ast):
            if isinstance(ast, Block):
                return sum(count_local_var(stmt) for stmt in ast.inst)
            elif isinstance(ast, If):
                return count_local_var(ast.thenStmt) + count_local_var(ast.elseStmt)
            elif isinstance(ast, For):
                return count_local_var(ast.loop)
            elif isinstance(ast, (VarDecl, ConstDecl)):
                return 1
            else: 
                return 0
        n_var = len(ast.param) + count_local_var(ast.body)

        self.emit.printout(self.emit.emitFRAMEALLOC(n_var + 2))

        frame = o
        scope = SubBody(frame, [[]] + [self.env])
        for x in ast.param:
            self.visit(x, scope)
        for x in ast.body.inst:
            self.visit(x, scope)
        
        self.emit.printout(self.emit.emitLABEL('\treturn_' + self.currentClassName + '_m_' + ast.name.name))
        self.emit.printout(self.emit.emitFRAMERESET(n_var + 2))

        if ast.name.name == 'main' and self.currentClassName == 'Program':
            pass
        else:
            self.emit.printout(self.emit.emitJRA())
    

    def visitAttributeDecl(self, ast: AttributeDecl, o):
        if isinstance(ast.kind, Static):
            if isinstance(ast.decl, VarDecl):
                name = self.currentClassName + '_a_' + ast.decl.variable.name
                typ = ast.decl.varType
                val = ast.decl.varInit
            else:
                name = self.currentClassName + '_a_' + ast.decl.constant.name
                typ = ast.decl.constType
                val = ast.decl.value
            self.emit.printvar(self.emit.emitATTRIBUTE(name, typ, val))
        
    
    def visitVarDecl(self, ast: VarDecl, o: SubBody):
        # o: SubBody
        idx = sum(len(scope) for scope in o.sym[:-1])

        # First only consider initialized variables in main method
        if ast.varInit:
            code, typ = self.visit(ast.varInit, o)
            self.emit.printout(code)
            self.emit.printout(self.emit.emitSTOREINDEX(idx, typ))

        o.sym[0].append(Symbol(ast.variable.name, ast.varType, Index(idx)))

    def visitConstDecl(self, ast: ConstDecl, o: SubBody):
        # o: SubBody
        idx = sum(len(scope) for scope in o.sym[:-1])

        # First only consider initialized variables in main method
        code, typ = self.visit(ast.value, o)
        self.emit.printout(code)
        self.emit.printout(self.emit.emitSTOREINDEX(idx, typ))

        o.sym[0].append(Symbol(ast.constant.name, ast.constType, Index(idx)))


    def visitAssign(self, ast: Assign, o):
        rc, _ = self.visit(ast.exp, o)
        self.emit.printout(rc)
        for scope in o.sym[:-1]:
            for sym in scope:
                if isinstance(ast.lhs, Id) and ast.lhs.name == sym.name:
                    index = sym.value.value
                    typ = sym.mtype
                    self.emit.printout(self.emit.emitSTOREINDEX(index, typ))


    def visitReturn(self, ast: Return, o):
        if ast.expr == NullLiteral():
            pass
        elif ast.expr:
            code, typ = self.visit(ast.expr, o)
            self.currentMethodSym.mtype.rettype = typ
            self.emit.printout(code)
            self.emit.printout(self.emit.emitLOADRETURN(typ))
            self.emit.printout(self.emit.emitJ('return_' + self.currentClassName + '_m_' + self.currentMethodSym.name))
    

    def visitFieldAccess(self, ast: FieldAccess, o):
        return '', IntType()


    def visitCallStmt(self, ast: CallStmt, o):
        # Actually calling method other than printing
        result = list()
        idx = 0
        for arg in ast.param:
            # Pass-by-value, result is in the accumulator
            code, typ = self.visit(arg, o)
            # Pre-allocate params before calling method
            result.append(code)
            result.append(self.emit.emitSTOREPARAM(idx, typ))
            idx += 1
    
        if ast.method.name == "putInt":
            result.append(self.emit.emitPUTINT())
        elif ast.method.name == "putIntLn":
            result.append(self.emit.emitPUTINTLN())
        elif ast.method.name == "putFloat":
            result.append(self.emit.emitPUTFLOAT())
        elif ast.method.name == "putFloatLn":
            result.append(self.emit.emitPUTFLOATLN())
        else:
            result.append(self.emit.emitJAL(self.currentClassName + '_m_' + ast.method.name))

        self.emit.printout(''.join(result))


    def visitCallExpr(self, ast: CallExpr, o):
        result = list()
        idx = 0
        for arg in ast.param:
            # Pass-by-value, result is in the accumulator
            code, typ = self.visit(arg, o)
            # Pre-allocate params before calling method
            result.append(code)
            result.append(self.emit.emitSTOREPARAM(idx, typ))
            idx += 1

        result.append(self.emit.emitJAL(self.currentClassName + '_m_' + ast.method.name))
        for sym in self.methodSyms:
            if sym.name == ast.method.name:
                return ''.join(result), sym.mtype.rettype


    def visitBlock(self, ast: Block, o):
        env = SubBody(o.frame, [[]] + o.sym)
        for stmt in ast.inst:
            self.visit(stmt, env)


    def visitIf(self, ast: If, o):
        code, _ = self.visit(ast.expr, o)
        falselabel = 'Label{}'.format(o.frame.getNewLabel())
        exitlabel = 'Label{}'.format(o.frame.getNewLabel())

        self.emit.printout(code)
        self.emit.printout(self.emit.emitIFFALSE(falselabel))
        self.visit(ast.thenStmt, o)
        if ast.elseStmt:
            self.emit.printout(self.emit.emitJ(exitlabel))
            self.emit.printout(self.emit.emitLABEL(falselabel))
            self.visit(ast.elseStmt, o)
            self.emit.printout(self.emit.emitLABEL(exitlabel))
        else:
            self.emit.printout(self.emit.emitLABEL(falselabel))


    def visitFor(self, ast: For, o: SubBody):
        typ = IntType()

        self.visit(Assign(ast.id, ast.expr1), o)
        o.frame.enterLoop()
        cont = 'Cont{}'.format(o.frame.getContinueLabel())
        brk = 'Break{}'.format(o.frame.getBreakLabel())

        # Save result on STACK, not TOP OF STACK
        self.emit.printout(''.join([
            self.visit(BinaryOp('<=', ast.expr1, ast.expr2), o)[0],
            self.emit.emitPUSHACC(typ),
        ]))

        # Compare
        lblInc = 'Label{}'.format(o.frame.getNewLabel())
        lblDec = 'Label{}'.format(o.frame.getNewLabel())
        self.emit.printout(''.join([
            self.emit.emitLABEL(cont),
            # Evaluate stack, if false jump to lblDec
            self.emit.emitLOADSTACKTOACC(),
            self.emit.emitIFFALSE(lblDec),
                self.visit(BinaryOp('<=', ast.id, ast.expr2), o)[0],
                self.emit.emitJ(lblInc),
            self.emit.emitLABEL(lblDec),
                self.visit(BinaryOp('>=', ast.id, ast.expr2), o)[0],
            self.emit.emitLABEL(lblInc),
            self.emit.emitIFFALSE(brk)
        ]))

        # Execute
        self.visit(ast.loop, o)
        
        # Increment
        lblIncr = 'Label{}'.format(o.frame.getNewLabel())
        lblDecr = 'Label{}'.format(o.frame.getNewLabel())
        self.emit.printout(self.emit.emitLOADSTACKTOACC())
        self.emit.printout(self.emit.emitIFFALSE(lblDecr))
        self.visit(Assign(ast.id, BinaryOp('+', ast.id, ast.expr3)), o)
        self.emit.printout(self.emit.emitJ(lblIncr))
        self.emit.printout(self.emit.emitLABEL(lblDecr))
        self.visit(Assign(ast.id, BinaryOp('-', ast.id, ast.expr3)), o)
        self.emit.printout(self.emit.emitLABEL(lblIncr))
        self.emit.printout(self.emit.emitJ(cont))

        # Exit loop
        self.emit.printout(self.emit.emitLABEL(brk))
        self.emit.printout(self.emit.emitPOPSTACK())
        o.frame.exitLoop()


    def visitBinaryOp(self, ast: BinaryOp, o):
        op = ast.op
        lc, lt = self.visit(ast.left, o)
        rc, rt = self.visit(ast.right, o)

        code = lc + self.emit.emitPUSHACC(lt) + rc

        if op in '+-*/%':
            rettype = IntType()
            if type(lt) == FloatType or type(rt) == FloatType:
                code += self.emit.emitI2F() if type(rt) == IntType else ''
                code += self.emit.emitI2FSTACK() if type(lt) == IntType else ''
                rettype = FloatType()
            code += self.emit.emitADDOP(op, rettype) if op in '+-' else self.emit.emitMULOP(op, rettype)
        elif op in ['||', '&&']:
            rettype = IntType()
            code += self.emit.emitBOOLOP(op)
        elif op in ['==', '!=']:
            rettype = IntType()
            code += self.emit.emitSEQ() if op == '==' else self.emit.emitSNE()
        elif op in ['>', '>=', '<', '<=']:
            # TODO: Compare floats
            rettype = IntType()
            if type(lt) == FloatType or type(rt) == FloatType:
                code += self.emit.emitI2F() if type(rt) == IntType else ''
                code += self.emit.emitI2FSTACK() if type(lt) == IntType else ''
                rettype = FloatType()
            code += self.emit.emitRELOP(op, rettype)
            rettype = IntType()
        elif op == '+.':
            return 'Not implemented', StringType()
        elif op == '==.':
            return 'Not implemented', IntType()

        return code, rettype

    def visitUnaryOp(self, ast: UnaryOp, o):
        code, typ = self.visit(ast.body, o)
        if ast.op == '-':
            return code + self.emit.emitNEG(typ), typ
        else:
            return code + self.emit.emitNOT(), BoolType()

    def visitId(self, ast: Id, o):
        for scope in o.sym[:-1]:
            for sym in scope:
                if ast.name == sym.name:
                    idx = sym.value.value
                    typ = sym.mtype
                    if isinstance(typ, BoolType): typ = IntType()
                    return self.emit.emitLOADINDEX(idx, typ), typ


    def visitIntLiteral(self, ast: IntLiteral, o):
        return self.emit.emitLOADACC(ast.value), IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, o):
        return self.emit.emitLOADACCF(str(ast.value)), FloatType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, o):
        return self.emit.emitLOADACC(1 if ast.value else 0), IntType()

    def visitStringLiteral(self, ast: StringLiteral, o):
        content = ast.value
        return "Not implemented\n", StringType()
