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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paramList.
    def visitParamList(self, ctx:D96Parser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#params.
    def visitParams(self, ctx:D96Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#param.
    def visitParam(self, ctx:D96Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#blockStat.
    def visitBlockStat(self, ctx:D96Parser.BlockStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statList.
    def visitStatList(self, ctx:D96Parser.StatListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx:D96Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx:D96Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx:D96Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr4.
    def visitExpr4(self, ctx:D96Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr5.
    def visitExpr5(self, ctx:D96Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr6.
    def visitExpr6(self, ctx:D96Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr7.
    def visitExpr7(self, ctx:D96Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr8.
    def visitExpr8(self, ctx:D96Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr9.
    def visitExpr9(self, ctx:D96Parser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr10.
    def visitExpr10(self, ctx:D96Parser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operand.
    def visitOperand(self, ctx:D96Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stat.
    def visitStat(self, ctx:D96Parser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#declStat.
    def visitDeclStat(self, ctx:D96Parser.DeclStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#varDecl.
    def visitVarDecl(self, ctx:D96Parser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variables.
    def visitVariables(self, ctx:D96Parser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ids.
    def visitIds(self, ctx:D96Parser.IdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#varsInit.
    def visitVarsInit(self, ctx:D96Parser.VarsInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assignStat.
    def visitAssignStat(self, ctx:D96Parser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ifStat.
    def visitIfStat(self, ctx:D96Parser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseifList.
    def visitElseifList(self, ctx:D96Parser.ElseifListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#forStat.
    def visitForStat(self, ctx:D96Parser.ForStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#methodCall.
    def visitMethodCall(self, ctx:D96Parser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalarVar.
    def visitScalarVar(self, ctx:D96Parser.ScalarVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexExpr.
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exprList.
    def visitExprList(self, ctx:D96Parser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exprs.
    def visitExprs(self, ctx:D96Parser.ExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#argList.
    def visitArgList(self, ctx:D96Parser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#memId.
    def visitMemId(self, ctx:D96Parser.MemIdContext):
        return Id(ctx.getChild(0).getText())    # may have $ in name?
