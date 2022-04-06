from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from functools import reduce
class ASTGeneration(BKOOLVisitor):

    '''
    # used for mutable (variable) or immutable (constant) declaration
    @dataclass
    class AttributeDecl(MemDecl):
        kind: SIKind #Instance or Static
        decl: StoreDecl # VarDecl for mutable or ConstDecl for immutable
        def __str__(self):
            return "AttributeDecl(" + str(self.kind) + ',' + str(self.decl) + ")" 

    # used for local constant declaration
    @dataclass
    class ConstDecl(StoreDecl):
        constant : Id
        constType : Type
        value : Expr
        def __str__(self):
            return "ConstDecl(" + str(self.constant) + "," + str(self.constType) + "," + str(self.value) + ")"  

    # used for local variable or parameter declaration 
    @dataclass
    class VarDecl(StoreDecl):
        variable : Id
        varType : Type
        varInit : Expr = None # None if there is no initial
        def __str__(self):
            return "VarDecl(" + str(self.variable) + "," + str(self.varType) + (","+ str(self.varInit) if self.varInit else "") + ")"
        def toParam(self):
            return "param(" + str(self.variable) + "," + str(self.varType) + ")"         
    '''

    '''
    #used for a class declaration
    @dataclass
    class ClassDecl(Decl):
        classname : Id
        memlist : List[MemDecl]
        parentname : Id = None # None if there is no parent
        def __str__(self):
            return "ClassDecl(" + str(self.classname) + (("," + str(self.parentname)) if self.parentname else "") + ",[" + ','.join(str(i) for i in self.memlist) + "])"
    '''

    def visitProgram(self,ctx:BKOOLParser.ProgramContext):             # xong
        return Program(reduce(lambda x,y: x + [self.visitClassdecl(y)],ctx.classdecl(),[]))
        
    # classdecl: (CLASS ID LP memberlist RP) | (CLASS ID EXTENDS ID LP memberlist RP) ; // ok
    def visitClassdecl(self,ctx:BKOOLParser.ClassdeclContext):             # xong
        if ctx.getChildCount() == 5:
            return ClassDecl(Id(ctx.ID(0).getText()),self.visitMemberlist(ctx.memberlist()))
        else:
            return ClassDecl(Id(ctx.ID(0).getText()),self.visitMemberlist(ctx.memberlist()),Id(ctx.ID(1).getText()))


    # memberlist: member memberlist | member | ;
    def visitMemberlist(self,ctx:BKOOLParser.MemberlistContext):             # xong
        if ctx.getChildCount() == 2:
            return self.visitMember(ctx.member()) + self.visitMemberlist(ctx.memberlist())
        elif ctx.getChildCount() == 1: 
            return self.visitMember(ctx.member())
        else:
            return []

    # member: attribute | method ;
    def visitMember(self,ctx:BKOOLParser.MemberContext):                    # xong 
        if ctx.attribute():
            return self.visitAttribute(ctx.attribute())
        else:
            return [self.visitMethod(ctx.method())]

    # attribute: mutableattribute | immutableattribute ;      
    def visitAttribute(self,ctx:BKOOLParser.AttributeContext):                             # xong        # list of Memdecl
        if ctx.mutableattribute():
            if ctx.mutableattribute().getChildCount() == 4:
                return list(map(lambda x: AttributeDecl(Static(),x),self.visitMutableattribute(ctx.mutableattribute())))
            else:
                return list(map(lambda x: AttributeDecl(Instance(),x),self.visitMutableattribute(ctx.mutableattribute())))
        else:
            if ctx.immutableattribute().getChildCount() == 5:
                return list(map(lambda x: AttributeDecl(Static(),x),self.visitImmutableattribute(ctx.immutableattribute())))
            else:
                return list(map(lambda x: AttributeDecl(Instance(),x),self.visitImmutableattribute(ctx.immutableattribute())))

    # mutableattribute: STATIC typedecl attributelist SEMI | typedecl attributelist SEMI; 
    def visitMutableattribute(self,ctx:BKOOLParser.MutableattributeContext):               # xong       # list
        return list(map(lambda x: VarDecl(x[0],self.visitTypedecl(ctx.typedecl()),x[1]),self.visitAttributelist(ctx.attributelist())))
    # immutableattribute: FINAL STATIC typedecl attributelist SEMI | STATIC FINAL typedecl attributelist SEMI | FINAL typedecl attributelist SEMI ; 
    def visitImmutableattribute(self,ctx:BKOOLParser.ImmutableattributeContext):           # xong       # list
        return list(map(lambda x: ConstDecl(x[0],self.visitTypedecl(ctx.typedecl()),x[1]),self.visitAttributelist(ctx.attributelist())))
    # attributelist: ID INITOP exp COMMA attributelist | ID COMMA attributelist | ID INITOP exp | ID;
    def visitAttributelist(self,ctx:BKOOLParser.AttributelistContext):             # xong       # list
        if ctx.getChildCount() == 5:
            return [(Id(ctx.ID().getText()),self.visitExp(ctx.exp()))] + self.visitAttributelist(ctx.attributelist())
        elif ctx.getChildCount() == 3 and ctx.attributelist():
            return [(Id(ctx.ID().getText()),None)] + self.visitAttributelist(ctx.attributelist())
        elif ctx.getChildCount() == 3 and ctx.attributelist() is None:
            return [(Id(ctx.ID().getText()),self.visitExp(ctx.exp()))]
        else:
            return [(Id(ctx.ID().getText()),None)]
    # method: STATIC typedecl ID LB paramlist RB blockstatement | typedecl ID LB paramlist RB blockstatement | ID LB paramlist RB blockstatement ;
    def visitMethod(self,ctx:BKOOLParser.MethodContext):                          # xong    
        if ctx.getChildCount() == 7:
            name = Id(ctx.ID().getText())
            kind = Static()
            param = self.visitParamlist(ctx.paramlist())                              # cho nay toParam() da duoc he thong su dung
            rttype = self.visitTypedecl(ctx.typedecl())
            body = self.visitBlockstatement(ctx.blockstatement())                                                             
            return MethodDecl(kind,name,param,rttype,body)
        elif ctx.getChildCount() == 6:
            name = Id(ctx.ID().getText())
            kind = Instance()
            param = self.visitParamlist(ctx.paramlist())                              # cho nay toParam() da duoc he thong su dung
            rttype = self.visitTypedecl(ctx.typedecl())
            body = self.visitBlockstatement(ctx.blockstatement())                                                               
            return MethodDecl(kind,name,param,rttype,body)
        else:
            name = Id("<init>")
            kind = Instance()
            param = self.visitParamlist(ctx.paramlist())                              # cho nay toParam() da duoc he thong su dung
            rttype = None                                                             
            body = self.visitBlockstatement(ctx.blockstatement())                                                               
            return MethodDecl(kind,name,param,rttype,body)
    # paramlist: param SEMI paramlistrest | param | ;
    def visitParamlist(self,ctx:BKOOLParser.ParamlistContext):                           # xong
        if ctx.getChildCount() == 3:
            return self.visitParam(ctx.param()) + self.visitParamlistrest(ctx.paramlistrest())
        elif ctx.getChildCount() == 1:
            return self.visitParam(ctx.param())
        else:
            return []

    # paramlistrest: param SEMI paramlistrest | param;
    def visitParamlistrest(self,ctx:BKOOLParser.ParamlistrestContext):                  # xong             # list
        if ctx.getChildCount() == 3:
            return self.visitParam(ctx.param()) + self.visitParamlistrest(ctx.paramlistrest())
        else:
            return self.visitParam(ctx.param())

    # param: typedecl idlist;
    def visitParam(self,ctx:BKOOLParser.ParamContext):                         # xong              # list
        var = self.visitIdlist(ctx.idlist())
        typ = self.visitTypedecl(ctx.typedecl())
        return list(map(lambda x: VarDecl(x,typ),var))                                                # chua duoc su dung toParam()
    
    def visitIdlist(self,ctx:BKOOLParser.IdlistContext):                        # xong            # list
        if ctx.getChildCount() == 3:
            return [Id(ctx.ID().getText())] + self.visitIdlist(ctx.idlist())
        else:
            return [Id(ctx.ID().getText())]

    # typedecl: primitype | arraytype | classtype;
    def visitTypedecl(self,ctx:BKOOLParser.TypedeclContext):                    # xong           # object
        if ctx.primitype():
            return self.visitPrimitype(ctx.primitype())
        elif ctx.arraytype():
            return self.visitArraytype(ctx.arraytype())
        else:
            return self.visitClasstype(ctx.classtype())

    #  primitype: INTTYPE | FLOATTYPE | BOOLTYPE | STRINGTYPE | VOIDTYPE ;
    def visitPrimitype(self,ctx:BKOOLParser.PrimitypeContext):                   # xong
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.BOOLTYPE():
            return BoolType()
        elif ctx.STRINGTYPE():
            return StringType()
        elif ctx.VOIDTYPE():
            return VoidType()
    
    def visitArraytype(self,ctx:BKOOLParser.ArraytypeContext):                    # xong
        return ArrayType(int(ctx.INTLIT().getText()),self.visitArraytypename(ctx.arraytypename()))

    # arraytypename: INTTYPE | FLOATTYPE | BOOLTYPE | STRINGTYPE | ID;
    def visitArraytypename(self,ctx:BKOOLParser.ClasstypeContext):            # xong
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.BOOLTYPE():
            return BoolType()
        elif ctx.STRINGTYPE():
            return StringType()
        elif ctx.VOIDTYPE():
            return VoidType()
        else:
            return ClassType(Id(ctx.ID().getText()))

    def visitClasstype(self,ctx:BKOOLParser.ClasstypeContext):                # xong
        return ClassType(Id(ctx.ID().getText()))

    # exp: exp1 COMPAREOP exp1 | exp1;
    def visitExp(self,ctx:BKOOLParser.ExpContext):                            # xong
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.COMPAREOP().getText(),self.visitExp1(ctx.exp1(0)),self.visitExp1(ctx.exp1(1)))
        else: 
            return self.visitExp1(ctx.exp1(0))

    # exp1: exp2 EQOP exp2 | exp2;
    def visitExp1(self,ctx:BKOOLParser.Exp1Context):                          # xong
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.EQOP().getText(),self.visitExp2(ctx.exp2(0)),self.visitExp2(ctx.exp2(1)))
        else: 
            return self.visitExp2(ctx.exp2(0))
    # exp2: exp2 LOGICOP exp3 | exp3;
    def visitExp2(self,ctx:BKOOLParser.Exp2Context):                          # xong
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.LOGICOP().getText(),self.visitExp2(ctx.exp2()),self.visitExp3(ctx.exp3()))
        else: 
            return self.visitExp3(ctx.exp3())
    # exp3: exp3 AMOP exp4 | exp4;
    def visitExp3(self,ctx:BKOOLParser.Exp3Context):                          # xong
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.AMOP().getText(),self.visitExp3(ctx.exp3()),self.visitExp4(ctx.exp4()))
        else: 
            return self.visitExp4(ctx.exp4())
    # exp4: exp4 MDOP exp5 | exp5;
    def visitExp4(self,ctx:BKOOLParser.Exp4Context):                           # xong
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.MDOP().getText(),self.visitExp4(ctx.exp4()),self.visitExp5(ctx.exp5()))
        else: 
            return self.visitExp5(ctx.exp5())
    # exp5: exp5 CONCATOP exp6 | exp6;
    def visitExp5(self,ctx:BKOOLParser.Exp5Context):                           # xong
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.CONCATOP().getText(),self.visitExp5(ctx.exp5()),self.visitExp6(ctx.exp6()))
        else: 
            return self.visitExp6(ctx.exp6())
    # exp6: NOTOP exp6 | exp7;
    def visitExp6(self,ctx:BKOOLParser.Exp6Context):                             # xong
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.NOTOP().getText(),self.visitExp6(ctx.exp6()))
        else:
            return self.visitExp7(ctx.exp7())
    # exp7: AMOP exp7 | exp8;
    def visitExp7(self,ctx:BKOOLParser.Exp7Context):                            # xong
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.AMOP().getText(),self.visitExp7(ctx.exp7()))
        else:
            return self.visitExp8(ctx.exp8())
    # exp8: exp9 (LSB exp RSB) | exp9;
    def visitExp8(self,ctx:BKOOLParser.Exp8Context):                               # xong
        if ctx.getChildCount() != 1:
            return ArrayCell(self.visitExp9(ctx.exp9()),self.visitExp(ctx.exp()))
        else:
            return self.visitExp9(ctx.exp9())
    # exp9: exp9 DOT ID | exp9 DOT ID LB explist RB | exp10;
    def visitExp9(self,ctx:BKOOLParser.Exp9Context):                                # xong
        if ctx.getChildCount() == 3:
            return FieldAccess(self.visitExp9(ctx.exp9()),Id(ctx.ID().getText()))
        elif ctx.getChildCount() == 6:
            return CallExpr(self.visitExp9(ctx.exp9()),Id(ctx.ID().getText()),self.visitExplist(ctx.explist()))
        else:
            return self.visitExp10(ctx.exp10())
    # exp10: NEW ID LB explist RB | operands;
    def visitExp10(self,ctx:BKOOLParser.Exp10Context):                              # xong
        if ctx.getChildCount() != 1:
            return NewExpr(Id(ctx.ID().getText()),self.visitExplist(ctx.explist()))
        else:
            return self.visitOperands(ctx.operands()) 
    # explist: exp COMMA explistrest | exp | ;
    def visitExplist(self,ctx:BKOOLParser.ExplistContext):                           # xong
        if ctx.getChildCount() == 3:
            return [self.visitExp(ctx.exp())] + self.visitExplistrest(ctx.explistrest())
        elif ctx.getChildCount() == 1:
            return [self.visitExp(ctx.exp())]
        else: 
            return []
    # explistrest: exp COMMA explistrest | exp;
    def visitExplistrest(self,ctx:BKOOLParser.ExplistrestContext):                    # xong
        if ctx.getChildCount() == 3:
            return [self.visitExp(ctx.exp())] + self.visitExplistrest(ctx.explistrest())
        else:
            return [self.visitExp(ctx.exp())]

    # operands: ID | THIS | NIL | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | LB exp RB | arraylit ;
    def visitOperands(self,ctx:BKOOLParser.OperandsContext):                            # xong
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.THIS():
            return SelfLiteral()
        elif ctx.NIL():
            return NullLiteral()
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            if ctx.BOOLLIT().getText() == 'true':
                return BooleanLiteral(bool(ctx.BOOLLIT().getText()))
            return BooleanLiteral(bool(False))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.arraylit():
            return self.visitArraylit(ctx.arraylit())
        else:   
            return self.visitExp(ctx.exp())
    
    # blockstatement: LP vardecllist statementlist RP;
    def visitBlockstatement(self,ctx:BKOOLParser.BlockstatementContext):            # xong
        return Block(self.visitVardecllist(ctx.vardecllist()),self.visitStatementlist(ctx.statementlist()))

    # vardecllist: vardecl SEMI vardecllist | vardecl SEMI | ;
    def visitVardecllist(self,ctx:BKOOLParser.VardecllistContext):                   # xong
        if ctx.getChildCount() == 3:
            return self.visitVardecl(ctx.vardecl()) + self.visitVardecllist(ctx.vardecllist())
        elif ctx.getChildCount() == 2:
            return self.visitVardecl(ctx.vardecl())
        else:
            return []

    # vardecl: mutablevar | immutablevar ;
    def visitVardecl(self,ctx:BKOOLParser.VardeclContext):                     # xong           # list of attributedecl
        if ctx.mutablevar():
            return list(map(lambda x: x,self.visitMutablevar(ctx.mutablevar())))
        else:
            return list(map(lambda x: x,self.visitImmutablevar(ctx.immutablevar())))

    # mutablevar: typedecl varlist;
    def visitMutablevar(self,ctx:BKOOLParser.MutablevarContext):                # xong          # list of vardecl
        return list(map(lambda x: VarDecl(x[0],self.visitTypedecl(ctx.typedecl()),x[1]),self.visitVarlist(ctx.varlist())))

    # immutablevar:  FINAL typedecl varlist 
    def visitImmutablevar(self,ctx:BKOOLParser.ImmutablevarContext):           # xong            # list of Constdecl
        return list(map(lambda x: ConstDecl(x[0],self.visitTypedecl(ctx.typedecl()),x[1]),self.visitVarlist(ctx.varlist())))

    # varlist: ID INITOP exp COMMA varlist | ID COMMA varlist | ID INITOP exp | ID; 
    def visitVarlist(self,ctx:BKOOLParser.VarlistContext):                      # xong          # list
        if ctx.getChildCount() == 5:
            return [(Id(ctx.ID().getText()),self.visitExp(ctx.exp()))] + self.visitVarlist(ctx.varlist())
        elif ctx.getChildCount() == 3 and ctx.varlist():
            return [(Id(ctx.ID().getText()),None)] + self.visitVarlist(ctx.varlist())
        elif ctx.getChildCount() == 1:
            return [(Id(ctx.ID().getText()),None)]
        else:
            return [(Id(ctx.ID().getText()),self.visitExp(ctx.exp()))]

    # statementlist: statement statementlist | statement | ;
    def visitStatementlist(self,ctx:BKOOLParser.StatementlistContext):                 # xong
        if ctx.getChildCount() == 2:
            return [self.visitStatement(ctx.statement())] + self.visitStatementlist(ctx.statementlist())
        elif ctx.getChildCount() == 1:
            return [self.visitStatement(ctx.statement())]
        else:
            return []

    # statement: blockstatement | assignstatement | ifstatement | forstatement | breakstatement | continuestatement | returnstatement | methodinvostatement ;
    def visitStatement(self,ctx:BKOOLParser.StatementContext):            # xong
        if ctx.blockstatement():
            return self.visitBlockstatement(ctx.blockstatement())
        elif ctx.assignstatement():
            return self.visitAssignstatement(ctx.assignstatement())
        elif ctx.ifstatement():
            return self.visitIfstatement(ctx.ifstatement())
        elif ctx.forstatement():
            return self.visitForstatement(ctx.forstatement())
        elif ctx.breakstatement():
            return self.visitBreakstatement(ctx.breakstatement())
        elif ctx.continuestatement():
            return self.visitContinuestatement(ctx.continuestatement())
        elif ctx.returnstatement():
            return self.visitReturnstatement(ctx.returnstatement())
        else:
            return self.visitMethodinvostatement(ctx.methodinvostatement())
    
    #assignstatement: localvar ASSIGNOP exp SEMI 
    #            | THIS DOT ID ASSIGNOP exp SEMI
    #            | eleofarray ASSIGNOP exp SEMI 
    #            | mutableattr  ASSIGNOP exp SEMI
    #            ;
    def visitAssignstatement(self,ctx:BKOOLParser.AssignstatementContext):               # xong
        if ctx.localvar():
            return Assign(self.visitLocalvar(ctx.localvar()),self.visitExp(ctx.exp()))
        elif ctx.eleofarray():
            return Assign(self.visitEleofarray(ctx.eleofarray()),self.visitExp(ctx.exp()))
        elif ctx.mutableattr():
            return Assign(self.visitMutableattr(ctx.mutableattr()),self.visitExp(ctx.exp()))
        else:
            return Assign(FieldAccess(SelfLiteral(),Id(ctx.ID().getText())),self.visitExp(ctx.exp()))

    # mutableattr: exp DOT ID ;
    def visitMutableattr(self,ctx:BKOOLParser.MutableattrContext):                   # xong
        return FieldAccess(self.visitExp(ctx.exp()),Id(ctx.ID().getText()))

    # localvar: ID;
    def visitLocalvar(self,ctx:BKOOLParser.LocalvarContext):                        # xong
        return Id(ctx.ID().getText())

    # eleofarray: exp LSB exp RSB;
    def visitEleofarray(self,ctx:BKOOLParser.EleofarrayContext):                   # xong
        return ArrayCell(self.visitExp(ctx.exp(0)),self.visitExp(ctx.exp(1)))

    # ifstatement: IF exp THEN statement | IF exp THEN statement ELSE statement;
    def visitIfstatement(self,ctx:BKOOLParser.IfstatementContext):                      # xong
        if ctx.ELSE():
            return If(self.visitExp(ctx.exp()),self.visitStatement(ctx.statement(0)),self.visitStatement(ctx.statement(1)))
        else:
            return If(self.visitExp(ctx.exp()),self.visitStatement(ctx.statement(0)))
    
    # forstatement: FOR ID ASSIGNOP exp TO exp DO statement | FOR ID ASSIGNOP exp DOWNTO exp DO statement ;
    def visitForstatement(self,ctx:BKOOLParser.ForstatementContext):                     # xong
        if ctx.TO():
            return For(Id(ctx.ID().getText()),self.visitExp(ctx.exp(0)),self.visitExp(ctx.exp(1)),True,self.visitStatement(ctx.statement()))
        else:
            return For(Id(ctx.ID().getText()),self.visitExp(ctx.exp(0)),self.visitExp(ctx.exp(1)),False,self.visitStatement(ctx.statement()))

    def visitBreakstatement(self,ctx:BKOOLParser.BreakstatementContext):                 # xong
        return Break()
    
    def visitContinuestatement(self,ctx:BKOOLParser.ContinuestatementContext):           # xong
        return Continue()
    # returnstatement: RETURN exp SEMI;
    def visitReturnstatement(self,ctx:BKOOLParser.ReturnstatementContext):               # xong 
        return Return(self.visitExp(ctx.exp()))
    # methodinvostatement: exp DOT ID LB explist RB SEMI;
    def visitMethodinvostatement(self,ctx:BKOOLParser.MethodinvostatementContext):        # xong
        return CallStmt(self.visitExp(ctx.exp()),Id(ctx.ID().getText()),self.visitExplist(ctx.explist()))

    # arraylit: LP arraylitlist RP;
    def visitArraylit(self,ctx:BKOOLParser.ArraylitContext):                    # xong
        return ArrayLiteral(self.visitArraylitlist(ctx.arraylitlist()))

    # arraylitlist: arrayintlit | arrayfloatlit | arraystringlit | arrayboolit;
    def visitArraylitlist(self,ctx:BKOOLParser.ArraylitlistContext):            # xong
        if ctx.arrayintlit():
            return self.visitArrayintlit(ctx.arrayintlit())
        elif ctx.arrayfloatlit():
            return self.visitArrayfloatlit(ctx.arrayfloatlit())
        elif ctx.arraystringlit():
            return self.visitArraystringlit(ctx.arraystringlit())
        else:
            return self.visitArrayboolit(ctx.arrayboolit())
    # arrayintlit: INTLIT COMMA arraylitlist | INTLIT;
    def visitArrayintlit(self,ctx:BKOOLParser.ArrayintlitContext):              # xong
        if ctx.getChildCount() == 3:
            return [IntLiteral(int(ctx.INTLIT().getText()))] + self.visitArraylitlist(ctx.arraylitlist())
        else:
            return [IntLiteral(int(ctx.INTLIT().getText()))]
    # arrayfloatlit: FLOATLIT COMMA arraylitlist | FLOATLIT;    
    def visitArrayfloatlit(self,ctx:BKOOLParser.ArrayfloatlitContext):          # xong
        if ctx.getChildCount() == 3:
            return [FloatLiteral(float(ctx.FLOATLIT().getText()))] + self.visitArraylitlist(ctx.arraylitlist())
        else:
            return [FloatLiteral(float(ctx.FLOATLIT().getText()))]
    # arraystringlit: STRINGLIT COMMA arraylitlist | STRINGLIT;
    def visitArraystringlit(self,ctx:BKOOLParser.ArraystringlitContext):        # xong
        if ctx.getChildCount() == 3:
            return [StringLiteral(ctx.STRINGLIT().getText())] + self.visitArraylitlist(ctx.arraylitlist())
        else:
            return [StringLiteral(ctx.STRINGLIT().getText())]
    # arrayboolit: BOOLLIT COMMA arraylitlist | BOOLLIT;
    def visitArrayboolit(self,ctx:BKOOLParser.ArrayboolitContext):               # xong
        if ctx.getChildCount() == 3:
            if ctx.BOOLLIT().getText() == 'true':
                return [BooleanLiteral(bool(True))] + self.visitArraylitlist(ctx.arraylitlist())
            else:
                return [BooleanLiteral(bool(False))] + self.visitArraylitlist(ctx.arraylitlist())
        else:
            if ctx.BOOLLIT().getText() == 'true':
                return [BooleanLiteral(bool(ctx.BOOLLIT().getText()))]
            else:
                return [BooleanLiteral(bool(False))]
