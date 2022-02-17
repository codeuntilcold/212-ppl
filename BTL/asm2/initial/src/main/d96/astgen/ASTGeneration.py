from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
    
    # List[ClassDecl]
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return Program(self.visit(ctx.classDecls()))


    # Visit a parse tree produced by D96Parser#classDecls.
    def visitClassDecls(self, ctx:D96Parser.ClassDeclsContext):
        return [self.visit(ctx.classDecl())] + self.visit(ctx.classDecls()) if ctx.getChildCount() == 2 else [self.visit(ctx.classDecl())]


    # Visit a parse tree produced by D96Parser#classDecl.
    def visitClassDecl(self, ctx:D96Parser.ClassDeclContext):
        if ctx.getChildCount() == 5:
            return ClassDecl(
                Id(ctx.ID(0).getText()),
                self.visit(ctx.memDeclList()),
            )
        else:
            return ClassDecl(
                Id(ctx.ID(0).getText()),
                self.visit(ctx.memDeclList()),
                Id(ctx.ID(1).getText())
            )


    # Visit a parse tree produced by D96Parser#memDeclList.
    def visitMemDeclList(self, ctx:D96Parser.MemDeclListContext):
        return [] if ctx.getChildCount() == 0 else self.visit(ctx.memDecl()) + self.visit(ctx.memDeclList())


    # Visit a parse tree produced by D96Parser#memDecl.
    def visitMemDecl(self, ctx:D96Parser.MemDeclContext):
        return self.visit(ctx.attrDecl()) if ctx.attrDecl() else self.visit(ctx.methodDecl())


    # Visit a parse tree produced by D96Parser#attrDecl.
    def visitAttrDecl(self, ctx:D96Parser.AttrDeclContext):
        attrs = self.visit(ctx.attrs()) if ctx.attrs() else self.visit(ctx.attrsInit())
        return [ 
            AttributeDecl(
                Static() if decl[0].name[0] == '$' else Instance(), 
                ConstDecl(decl[0], decl[1], decl[2]) if ctx.VAL() else VarDecl(decl[0], decl[1], decl[2])
            ) for decl in attrs
        ]

    # Visit a parse tree produced by D96Parser#attrs.
    def visitAttrs(self, ctx:D96Parser.AttrsContext):
        # [ (Id(), Type(), None) ]
        idents = self.visit(ctx.memIds())
        typ = self.visit(ctx.typeDecl())
        return [ (idname, typ, None) for idname in idents ]


    # Visit a parse tree produced by D96Parser#memIds.
    def visitMemIds(self, ctx:D96Parser.MemIdsContext):
        return [self.visit(ctx.memId())] if ctx.getChildCount() == 1 else [self.visit(ctx.memId())] + self.visit(ctx.memIds())


    # Visit a parse tree produced by D96Parser#attrsInit.
    def visitAttrsInit(self, ctx:D96Parser.AttrsInitContext):
        # [ (Id(), Type(), Expr()) ]
        ident = self.visit(ctx.memId())
        rhs = self.visit(ctx.expr())
        if ctx.attrsInit():
            rest = self.visit(ctx.attrsInit())
            typ = rest[0][1]
            return [ (ident, typ, rhs) ] + rest
        else:
            return [( ident, self.visit(ctx.typeDecl()), rhs )]


    # Visit a parse tree produced by D96Parser#methodDecl.
    def visitMethodDecl(self, ctx:D96Parser.MethodDeclContext):
        if ctx.CONSTRUCTOR(): 
            return MethodDecl( 
                Instance(),
                Id("Constructor"),
                self.visit(ctx.paramList()),
                self.visit(ctx.blockStat())
            )
        elif ctx.DESTRUCTOR():
            return MethodDecl(
                Instance(),
                Id("Destructor"),
                [],
                self.visit(ctx.blockStat())
            )
        else:
            funcname = self.visit(ctx.memId())
            return MethodDecl(
                Static() if funcname.name[0] == '$' else Instance(),
                funcname,
                self.visit(ctx.paramList()),
                self.visit(ctx.blockStat())
            )

    # Visit a parse tree produced by D96Parser#paramList.
    def visitParamList(self, ctx:D96Parser.ParamListContext):
        return [] if ctx.getChildCount() == 0 else self.visit(ctx.params())


    # Visit a parse tree produced by D96Parser#params.
    def visitParams(self, ctx:D96Parser.ParamsContext):
        return [self.visit(ctx.param())] if ctx.getChildCount() == 1 else [self.visit(ctx.param())] + self.visit(ctx.params())


    # Visit a parse tree produced by D96Parser#param.
    def visitParam(self, ctx:D96Parser.ParamContext):
        idents = self.visit(ctx.ids())
        return [VarDecl(
            name,
            self.visit(ctx.typeDecl()),
        ) for name in idents]


    # Visit a parse tree produced by D96Parser#blockStat.
    def visitBlockStat(self, ctx:D96Parser.BlockStatContext):
        return self.visit(ctx.statList())


    # Visit a parse tree produced by D96Parser#statList.
    def visitStatList(self, ctx:D96Parser.StatListContext):
        return [] if ctx.getChildCount() == 0 else self.visit(ctx.stat()) + self.visit(ctx.statList())


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visit(ctx.expr1(0)) if ctx.getChildCount() == 1 else BinaryOp(
            ctx.getChild(1).getText(),
            self.visit(ctx.expr1(0)),
            self.visit(ctx.expr1(1))
        )


    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx:D96Parser.Expr1Context):
        return self.visit(ctx.expr2(0)) if ctx.getChildCount() == 1 else BinaryOp(
            ctx.getChild(1).getText(),
            self.visit(ctx.expr2(0)),
            self.visit(ctx.expr2(1))
        )


    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx:D96Parser.Expr2Context):
        return self.visit(ctx.expr3()) if ctx.getChildCount() == 1 else BinaryOp(
            ctx.getChild(1).getText(),
            self.visit(ctx.expr2()),
            self.visit(ctx.expr3())
        )


    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx:D96Parser.Expr3Context):
        return self.visit(ctx.expr4()) if ctx.getChildCount() == 1 else BinaryOp(
            ctx.getChild(1).getText(),
            self.visit(ctx.expr3()),
            self.visit(ctx.expr4())
        )


    # Visit a parse tree produced by D96Parser#expr4.
    def visitExpr4(self, ctx:D96Parser.Expr4Context):
        return self.visit(ctx.expr5()) if ctx.getChildCount() == 1 else BinaryOp(
            ctx.getChild(1).getText(),
            self.visit(ctx.expr4()),
            self.visit(ctx.expr5())
        )


    # Visit a parse tree produced by D96Parser#expr5.
    def visitExpr5(self, ctx:D96Parser.Expr5Context):
        return self.visit(ctx.expr6()) if ctx.getChildCount() == 1 else UnaryOp(
            ctx.getChild(0).getText(),
            self.visit(ctx.expr5())
        )


    # Visit a parse tree produced by D96Parser#expr6.
    def visitExpr6(self, ctx:D96Parser.Expr6Context):
        return self.visit(ctx.expr7()) if ctx.getChildCount() == 1 else UnaryOp(
            ctx.getChild(0).getText(),
            self.visit(ctx.expr6())
        )



    """
        THIS IS WHY WE DONT MESS WITH THE MULTIVERSE
        THIS IS WHY WE DONT MESS WITH THE MULTIVERSE
        THIS IS WHY WE DONT MESS WITH THE MULTIVERSE
        THIS IS WHY WE DONT MESS WITH THE MULTIVERSE
        THIS IS WHY WE DONT MESS WITH THE MULTIVERSE
        THIS IS WHY WE DONT MESS WITH THE MULTIVERSE
        THIS IS WHY WE DONT MESS WITH THE MULTIVERSE
    """

    # Visit a parse tree produced by D96Parser#expr7.
    def visitExpr7(self, ctx:D96Parser.Expr7Context):
        if ctx.getChildCount() == 1:
            self.visit(ctx.expr8())
        else:
            return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr8.
    def visitExpr8(self, ctx:D96Parser.Expr8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr9())
        elif ctx.getChildCount() == 3:
            return FieldAccess( self.visit(ctx.expr8()), Id(ctx.ID().getText()) )
        else:
            return CallExpr( self.visit(ctx.expr8()), Id(ctx.ID().getText()), self.visit(ctx.argList()) )


    # Visit a parse tree produced by D96Parser#expr9.
    def visitExpr9(self, ctx:D96Parser.Expr9Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr10())
        elif ctx.getChildCount() == 3:
            return FieldAccess( Id(ctx.ID().getText()), Id(ctx.STATIC_ID().getText() ) )
        else:
            return CallExpr( Id(ctx.ID().getText()), Id(ctx.STATIC_ID().getText()), self.visit(ctx.argList()) )


    # Visit a parse tree produced by D96Parser#expr10.
    def visitExpr10(self, ctx:D96Parser.Expr10Context):
        return self.visit(ctx.operand()) if ctx.getChildCount() == 1 else NewExpr(
            Id(ctx.ID().getText()),
            self.visit(ctx.argList())
        )

    # Visit a parse tree produced by D96Parser#operand.
    def visitOperand(self, ctx:D96Parser.OperandContext):
        if ctx.getChildCount() == 3: return self.visit(ctx.expr())
        elif ctx.ID(): return Id(ctx.ID().getText())
        elif ctx.SELF(): return SelfLiteral()
        elif ctx.NULL(): return NullLiteral()
        elif ctx.INTLIT(): return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT(): return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT(): return BooleanLiteral(bool(ctx.BOOLLIT().getText()))
        elif ctx.STRINGLIT(): return StringLiteral(ctx.STRINGLIT().getText())
        else: return self.visit(ctx.arrayLit())


    # Visit a parse tree produced by D96Parser#stat.
    def visitStat(self, ctx:D96Parser.StatContext):
        if ctx.RETURN():
            return [Return()] if ctx.getChildCount() == 2 else [Return(self.visit(ctx.expr()))]
        elif ctx.BREAK(): return [Break()]
        elif ctx.CONTINUE(): return [Continue()]
        else: return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by D96Parser#declStat.
    def visitDeclStat(self, ctx:D96Parser.DeclStatContext):
        return self.visit(ctx.varDecl())


    # Visit a parse tree produced by D96Parser#varDecl.
    def visitVarDecl(self, ctx:D96Parser.VarDeclContext):
        variables = self.visit(ctx.variables()) if ctx.variables() else self.visit(ctx.varsInit())
        return [ 
            ConstDecl(decl[0], decl[1], decl[2]) if ctx.VAL() else VarDecl(decl[0], decl[1], decl[2])
            for decl in variables
        ]


    # Visit a parse tree produced by D96Parser#variables.
    def visitVariables(self, ctx:D96Parser.VariablesContext):
        # [ (Id(), Type(), None) ]
        idents = self.visit(ctx.ids())
        typ = self.visit(ctx.typeDecl())
        return [ (idname, typ, None) for idname in idents ]


    # Visit a parse tree produced by D96Parser#ids.
    def visitIds(self, ctx:D96Parser.IdsContext):
        return [ Id(ctx.ID().getText()) ] if ctx.getChildCount() == 1 else [ Id(ctx.ID().getText()) ] + self.visit(ctx.ids())


    # Visit a parse tree produced by D96Parser#varsInit.
    def visitVarsInit(self, ctx:D96Parser.VarsInitContext):
        # [ (Id(), Type(), Expr()) ]
        ident = Id(ctx.ID().getText())
        rhs = self.visit(ctx.expr())
        if ctx.varsInit():
            rest = self.visit(ctx.varsInit())
            typ = rest[0][1]
            return [ (ident, typ, rhs) ] + rest
        else:
            return [( ident, self.visit(ctx.typeDecl()), rhs )]


    # Visit a parse tree produced by D96Parser#assignStat.
    def visitAssignStat(self, ctx:D96Parser.AssignStatContext):
        return [Assign( self.visit(ctx.getChild(0)), self.visit(ctx.expr()) )]


    # Visit a parse tree produced by D96Parser#ifStat.
    def visitIfStat(self, ctx:D96Parser.IfStatContext):
        return [If( self.visit(ctx.expr()), self.visit(ctx.blockStat()), self.visit(ctx.elseifList()) )]


    # Visit a parse tree produced by D96Parser#elseifList.
    def visitElseifList(self, ctx:D96Parser.ElseifListContext):
        if ctx.getChildCount() == 0:
            return None
        elif ctx.ELSE():
            return self.visit(ctx.blockStat())
        else:
            return If( self.visit(ctx.expr()), self.visit(ctx.blockStat()), self.visit(ctx.elseifList()) )


    # Visit a parse tree produced by D96Parser#forStat.
    def visitForStat(self, ctx:D96Parser.ForStatContext):
        if ctx.getChildCount() == 9:
            return [For( self.visit(ctx.scalarVar()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.blockStat()) )]
        else:    
            return [For( self.visit(ctx.scalarVar()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.blockStat()), self.visit(ctx.expr(2)) )]


    # Visit a parse tree produced by D96Parser#methodCall.
    def visitMethodCall(self, ctx:D96Parser.MethodCallContext):
        if ctx.DOT():
            return [CallStmt( self.visit(ctx.expr8()), Id(ctx.ID().getText()), self.visit(ctx.argList()) )]
        else:
            return [CallStmt( Id(ctx.ID().getText()), Id(ctx.STATIC_ID().getText()), self.visit(ctx.argList()) )]


    # Visit a parse tree produced by D96Parser#scalarVar.
    def visitScalarVar(self, ctx:D96Parser.ScalarVarContext):
        if ctx.getChildCount() == 1: return Id(ctx.ID().getText())
        elif ctx.STATIC_ID(): return FieldAccess( Id(ctx.ID().getText()), Id(ctx.STATIC_ID().getText()) )
        else: return FieldAccess( self.visit(ctx.expr8()), Id(ctx.ID().getText()) )


    """
        THIS IS WHY WE DONT MESS WITH THE MULTIVERSE
        THIS IS WHY WE DONT MESS WITH THE MULTIVERSE
        THIS IS WHY WE DONT MESS WITH THE MULTIVERSE
        THIS IS WHY WE DONT MESS WITH THE MULTIVERSE
        THIS IS WHY WE DONT MESS WITH THE MULTIVERSE
        THIS IS WHY WE DONT MESS WITH THE MULTIVERSE
        THIS IS WHY WE DONT MESS WITH THE MULTIVERSE
    """
    def visitIndexExpr(self, ctx:D96Parser.IndexExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typeDecl.
    def visitTypeDecl(self, ctx:D96Parser.TypeDeclContext):
        return ClassType(Id(ctx.ID().getText())) if ctx.ID() else self.visit(ctx.getChild(0))


    # Visit a parse tree produced by D96Parser#arrayType.
    def visitArrayType(self, ctx:D96Parser.ArrayTypeContext):
        return ArrayType(
            int(ctx.INTLIT().getText()),
            self.visit(ctx.getChild(2))
        )


    # Visit a parse tree produced by D96Parser#primitiveType.
    def visitPrimitiveType(self, ctx:D96Parser.PrimitiveTypeContext):
        if ctx.BOOLTYPE(): return BoolType()
        elif ctx.INTTYPE(): return IntType()
        elif ctx.FLOATTYPE(): return FloatType()
        elif ctx.STRINGTYPE(): return StringType()


    # Visit a parse tree produced by D96Parser#arrayLit.
    def visitArrayLit(self, ctx:D96Parser.ArrayLitContext):
        return ArrayLiteral(self.visit(ctx.exprList()))


    # Visit a parse tree produced by D96Parser#exprList.
    def visitExprList(self, ctx:D96Parser.ExprListContext):
        return self.visit(ctx.exprs()) if ctx.getChildCount() else []


    # Visit a parse tree produced by D96Parser#exprs.
    def visitExprs(self, ctx:D96Parser.ExprsContext):
        return [self.visit(ctx.expr())] if ctx.getChildCount() == 1 else [self.visit(ctx.expr)] + self.visit(ctx.exprs())


    # Visit a parse tree produced by D96Parser#argList.
    def visitArgList(self, ctx:D96Parser.ArgListContext):
        return self.visit(ctx.exprs()) if ctx.getChildCount() else []


    # Visit a parse tree produced by D96Parser#memId.
    def visitMemId(self, ctx:D96Parser.MemIdContext):
        return Id(ctx.getChild(0).getText())    # may have $ in name?
