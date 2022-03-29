from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from functools import reduce


class ASTGeneration(BKOOLVisitor):


    def visitProgram(self,ctx:BKOOLParser.ProgramContext):
        return Program(reduce(lambda x,y: x + [self.visit(y)],ctx.classdecl(),[]))

        
    def visitClassdecl(self,ctx:BKOOLParser.ClassdeclContext):
        if ctx.getChildCount() == 5:
            return ClassDecl(Id(ctx.ID(0).getText()), self.visit(ctx.memberlist()))
        else:
            return ClassDecl(Id(ctx.ID(0).getText()), self.visit(ctx.memberlist()), Id(ctx.ID(1).getText()))


    def visitMemberlist(self,ctx:BKOOLParser.MemberlistContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.member()) + self.visit(ctx.memberlist())
        else:
            return []


    def visitMember(self,ctx:BKOOLParser.MemberContext):        
        if ctx.attribute():
            return self.visit(ctx.attribute())
        else:
            return [self.visit(ctx.method())]


    def visitAttribute(self,ctx:BKOOLParser.AttributeContext):
        if ctx.mutableattribute():
            if ctx.mutableattribute().getChildCount() == 4:
                return list(map(lambda x: AttributeDecl(Static(),x),self.visit(ctx.mutableattribute())))
            else:
                return list(map(lambda x: AttributeDecl(Instance(),x),self.visit(ctx.mutableattribute())))
        else:
            if ctx.immutableattribute().getChildCount() == 5:
                return list(map(lambda x: AttributeDecl(Static(),x),self.visit(ctx.immutableattribute())))
            else:
                return list(map(lambda x: AttributeDecl(Instance(),x),self.visit(ctx.immutableattribute())))

    
    def visitMutableattribute(self,ctx:BKOOLParser.MutableattributeContext):
        return list(map(lambda x: VarDecl(x[0],self.visit(ctx.typedecl()),x[1]),self.visit(ctx.attributes())))
    
    
    def visitImmutableattribute(self,ctx:BKOOLParser.ImmutableattributeContext):
        return list(map(lambda x: ConstDecl(x[0],self.visit(ctx.typedecl()),x[1]),self.visit(ctx.attributes())))
    
    
    def visitAttributes(self,ctx:BKOOLParser.AttributesContext):
        if ctx.getChildCount() == 5:
            return [(Id(ctx.ID().getText()),self.visit(ctx.exp()))] + self.visit(ctx.attributes())
        elif ctx.getChildCount() == 3 and ctx.attributes():
            return [(Id(ctx.ID().getText()),None)] + self.visit(ctx.attributes())
        elif ctx.getChildCount() == 3 and ctx.attributes() is None:
            return [(Id(ctx.ID().getText()),self.visit(ctx.exp()))]
        else:
            return [(Id(ctx.ID().getText()),None)]
    
    
    def visitMethod(self,ctx:BKOOLParser.MethodContext):                 
        if ctx.getChildCount() == 7:
            name = Id(ctx.ID().getText())
            kind = Static()
            param = self.visit(ctx.paramlist())
            rttype = self.visit(ctx.typedecl())
            body = self.visit(ctx.blockstatement())                                                             
            return MethodDecl(kind,name,param,rttype,body)
        elif ctx.getChildCount() == 6:
            name = Id(ctx.ID().getText())
            kind = Instance()
            param = self.visit(ctx.paramlist())
            rttype = self.visit(ctx.typedecl())
            body = self.visit(ctx.blockstatement())                                                               
            return MethodDecl(kind,name,param,rttype,body)
        else:
            name = Id("<init>")
            kind = Instance()
            param = self.visit(ctx.paramlist())
            rttype = None                                                             
            body = self.visit(ctx.blockstatement())                                                               
            return MethodDecl(kind,name,param,rttype,body)

    
    def visitParamlist(self,ctx:BKOOLParser.ParamlistContext):              
        if ctx.getChildCount() == 1:
            return self.visit(ctx.params())
        else:
            return []


    def visitParams(self,ctx:BKOOLParser.ParamsContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.param()) + self.visit(ctx.params())
        else:
            return self.visit(ctx.param())

    
    def visitParam(self,ctx:BKOOLParser.ParamContext):
        var = self.visit(ctx.ids())
        typ = self.visit(ctx.typedecl())
        return list(map(lambda x: VarDecl(x,typ),var))                                                # chua duoc su dung toParam()
    

    def visitIds(self,ctx:BKOOLParser.IdsContext):
        if ctx.getChildCount() == 3:
            return [Id(ctx.ID().getText())] + self.visit(ctx.ids())
        else:
            return [Id(ctx.ID().getText())]


    def visitTypedecl(self,ctx:BKOOLParser.TypedeclContext):
        if ctx.primitype():
            return self.visit(ctx.primitype())
        elif ctx.arraytype():
            return self.visit(ctx.arraytype())
        else:
            return self.visit(ctx.classtype())

    
    def visitPrimitype(self,ctx:BKOOLParser.PrimitypeContext):      
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
    
    def visitArraytype(self,ctx:BKOOLParser.ArraytypeContext):       
        return ArrayType(int(ctx.INTLIT().getText()),self.visit(ctx.getChild(0)))


    def visitClasstype(self,ctx:BKOOLParser.ClasstypeContext):   
        return ClassType(Id(ctx.ID().getText()))


    def visitExp(self,ctx:BKOOLParser.ExpContext):               
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.COMPAREOP().getText(),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))
        else: 
            return self.visit(ctx.exp1(0))

    
    def visitExp1(self,ctx:BKOOLParser.Exp1Context):             
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.EQOP().getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
        else: 
            return self.visit(ctx.exp2(0))
    
    
    def visitExp2(self,ctx:BKOOLParser.Exp2Context):             
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.LOGICOP().getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))
        else: 
            return self.visit(ctx.exp3())
    
    
    def visitExp3(self,ctx:BKOOLParser.Exp3Context):             
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.AMOP().getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
        else: 
            return self.visit(ctx.exp4())
    
    
    def visitExp4(self,ctx:BKOOLParser.Exp4Context):              
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.MDOP().getText(),self.visit(ctx.exp4()),self.visit(ctx.exp5()))
        else: 
            return self.visit(ctx.exp5())
    
    
    def visitExp5(self,ctx:BKOOLParser.Exp5Context):              
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.CONCATOP().getText(),self.visit(ctx.exp5()),self.visit(ctx.exp6()))
        else: 
            return self.visit(ctx.exp6())
    
    
    def visitExp6(self,ctx:BKOOLParser.Exp6Context):                
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.NOTOP().getText(),self.visit(ctx.exp6()))
        else:
            return self.visit(ctx.exp7())
    
    
    def visitExp7(self,ctx:BKOOLParser.Exp7Context):               
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.AMOP().getText(),self.visit(ctx.exp7()))
        else:
            return self.visit(ctx.exp8())
    
    
    def visitExp8(self,ctx:BKOOLParser.Exp8Context):                  
        if ctx.getChildCount() != 1:
            return ArrayCell(self.visit(ctx.exp9()),self.visit(ctx.exp()))
        else:
            return self.visit(ctx.exp9())
    
    
    def visitExp9(self,ctx:BKOOLParser.Exp9Context):                   
        if ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.exp9()),Id(ctx.ID().getText()))
        elif ctx.getChildCount() == 6:
            return CallExpr(self.visit(ctx.exp9()),Id(ctx.ID().getText()),self.visit(ctx.explist()))
        else:
            return self.visit(ctx.exp10())
    
    
    def visitExp10(self,ctx:BKOOLParser.Exp10Context):                 
        if ctx.getChildCount() != 1:
            return NewExpr(Id(ctx.ID().getText()),self.visit(ctx.explist()))
        else:
            return self.visit(ctx.operands()) 
    
    
    def visitExplist(self,ctx:BKOOLParser.ExplistContext):              
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exps())
        else: 
            return []
    
    
    def visitExps(self,ctx:BKOOLParser.ExpsContext):       
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.exp())] + self.visit(ctx.exps())
        else:
            return [self.visit(ctx.exp())]

    
    def visitOperands(self,ctx:BKOOLParser.OperandsContext):               
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
            return BooleanLiteral(bool(ctx.BOOLLIT().getText() == 'true'))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
        else:   
            return self.visit(ctx.exp())
    
    
    def visitBlockstatement(self,ctx:BKOOLParser.BlockstatementContext):
        return Block(self.visit(ctx.vardecllist()) + self.visit(ctx.statementlist()))

    # vardecllist: vardecl SEMI vardecllist | vardecl SEMI | ;
    def visitVardecllist(self,ctx:BKOOLParser.VardecllistContext):      
        if ctx.getChildCount() == 3:
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecllist())
        else:
            return []

    
    def visitVardecl(self,ctx:BKOOLParser.VardeclContext):
        if ctx.mutablevar():
            return list(map(lambda x: x,self.visit(ctx.mutablevar())))
        else:
            return list(map(lambda x: x,self.visit(ctx.immutablevar())))

    
    def visitMutablevar(self,ctx:BKOOLParser.MutablevarContext):
        return list(map(lambda x: VarDecl(x[0],self.visit(ctx.typedecl()),x[1]),self.visit(ctx.variables())))

    
    def visitImmutablevar(self,ctx:BKOOLParser.ImmutablevarContext):
        return list(map(lambda x: ConstDecl(x[0],self.visit(ctx.typedecl()),x[1]),self.visit(ctx.variables())))

    
    def visitVariables(self,ctx:BKOOLParser.VariablesContext):
        if ctx.getChildCount() == 5:
            return [(Id(ctx.ID().getText()),self.visit(ctx.exp()))] + self.visit(ctx.variables())
        elif ctx.getChildCount() == 3 and ctx.variables():
            return [(Id(ctx.ID().getText()),None)] + self.visit(ctx.variables())
        elif ctx.getChildCount() == 1:
            return [(Id(ctx.ID().getText()),None)]
        else:
            return [(Id(ctx.ID().getText()),self.visit(ctx.exp()))]

    
    def visitStatementlist(self,ctx:BKOOLParser.StatementlistContext):    
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.statement())] + self.visit(ctx.statementlist())
        else:
            return []

    
    def visitStatement(self,ctx:BKOOLParser.StatementContext):            
        return self.visit(ctx.getChild(0))
    
    
    def visitAssignstatement(self,ctx:BKOOLParser.AssignstatementContext):  
        if ctx.localvar():
            return Assign(self.visit(ctx.localvar()),self.visit(ctx.exp()))
        elif ctx.eleofarray():
            return Assign(self.visit(ctx.eleofarray()),self.visit(ctx.exp()))
        elif ctx.mutableattr():
            return Assign(self.visit(ctx.mutableattr()),self.visit(ctx.exp()))
        else:
            return Assign(FieldAccess(SelfLiteral(),Id(ctx.ID().getText())),self.visit(ctx.exp()))

    
    def visitMutableattr(self,ctx:BKOOLParser.MutableattrContext):      
        return FieldAccess(self.visit(ctx.exp()),Id(ctx.ID().getText()))

    
    def visitLocalvar(self,ctx:BKOOLParser.LocalvarContext):           
        return Id(ctx.ID().getText())

    
    def visitEleofarray(self,ctx:BKOOLParser.EleofarrayContext):      
        return ArrayCell(self.visit(ctx.exp(0)),self.visit(ctx.exp(1)))

    
    def visitIfstatement(self,ctx:BKOOLParser.IfstatementContext):         
        if ctx.ELSE():
            return If(self.visit(ctx.exp()),self.visit(ctx.statement(0)),self.visit(ctx.statement(1)))
        else:
            return If(self.visit(ctx.exp()),self.visit(ctx.statement(0)))
    
    
    def visitForstatement(self,ctx:BKOOLParser.ForstatementContext):        
        if ctx.TO():
            return For(Id(ctx.ID().getText()),self.visit(ctx.exp(0)),self.visit(ctx.exp(1)),True,self.visit(ctx.statement()))
        else:
            return For(Id(ctx.ID().getText()),self.visit(ctx.exp(0)),self.visit(ctx.exp(1)),False,self.visit(ctx.statement()))

    
    def visitBreakstatement(self,ctx:BKOOLParser.BreakstatementContext):    
        return Break()
    

    def visitContinuestatement(self,ctx:BKOOLParser.ContinuestatementContext):
        return Continue()
    

    def visitReturnstatement(self,ctx:BKOOLParser.ReturnstatementContext):   
        return Return(self.visit(ctx.exp()))
    

    def visitMethodinvostatement(self,ctx:BKOOLParser.MethodinvostatementContext):
        return CallStmt(self.visit(ctx.exp()),Id(ctx.ID().getText()),self.visit(ctx.explist()))


    def visitArraylit(self,ctx:BKOOLParser.ArraylitContext):       
        return ArrayLiteral(self.visit(ctx.arraylitlist()))

    
    def visitArraylitlist(self,ctx:BKOOLParser.ArraylitlistContext):  
        if ctx.arrayintlit():
            return self.visit(ctx.arrayintlit())
        elif ctx.arrayfloatlit():
            return self.visit(ctx.arrayfloatlit())
        elif ctx.arraystringlit():
            return self.visit(ctx.arraystringlit())
        else:
            return self.visit(ctx.arrayboolit())
    
    
    def visitArrayintlit(self,ctx:BKOOLParser.ArrayintlitContext): 
        if ctx.getChildCount() == 3:
            return [IntLiteral(int(ctx.INTLIT().getText()))] + self.visit(ctx.arraylitlist())
        else:
            return [IntLiteral(int(ctx.INTLIT().getText()))]
    
    
    def visitArrayfloatlit(self,ctx:BKOOLParser.ArrayfloatlitContext):
        if ctx.getChildCount() == 3:
            return [FloatLiteral(float(ctx.FLOATLIT().getText()))] + self.visit(ctx.arraylitlist())
        else:
            return [FloatLiteral(float(ctx.FLOATLIT().getText()))]
    
    
    def visitArraystringlit(self,ctx:BKOOLParser.ArraystringlitContext):
        if ctx.getChildCount() == 3:
            return [StringLiteral(ctx.STRINGLIT().getText())] + self.visit(ctx.arraylitlist())
        else:
            return [StringLiteral(ctx.STRINGLIT().getText())]
    
    
    def visitArrayboolit(self,ctx:BKOOLParser.ArrayboolitContext):  
        if ctx.getChildCount() == 3:
            return [BooleanLiteral(ctx.BOOLLIT().getText() == 'true')] + self.visit(ctx.arraylitlist())
        else:
            return [BooleanLiteral(ctx.BOOLLIT().getText() == 'true')]
