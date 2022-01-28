# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classDecls.
    def visitClassDecls(self, ctx:D96Parser.ClassDeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classDecl.
    def visitClassDecl(self, ctx:D96Parser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#memDeclList.
    def visitMemDeclList(self, ctx:D96Parser.MemDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#memDecl.
    def visitMemDecl(self, ctx:D96Parser.MemDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attrDecl.
    def visitAttrDecl(self, ctx:D96Parser.AttrDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attrs.
    def visitAttrs(self, ctx:D96Parser.AttrsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#memIds.
    def visitMemIds(self, ctx:D96Parser.MemIdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attrsInit.
    def visitAttrsInit(self, ctx:D96Parser.AttrsInitContext):
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayType.
    def visitArrayType(self, ctx:D96Parser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitiveType.
    def visitPrimitiveType(self, ctx:D96Parser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)



del D96Parser