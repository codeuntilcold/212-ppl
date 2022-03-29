# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classdecl.
    def visitClassdecl(self, ctx:BKOOLParser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#memberlist.
    def visitMemberlist(self, ctx:BKOOLParser.MemberlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#member.
    def visitMember(self, ctx:BKOOLParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute.
    def visitAttribute(self, ctx:BKOOLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutableattribute.
    def visitMutableattribute(self, ctx:BKOOLParser.MutableattributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutableattribute.
    def visitImmutableattribute(self, ctx:BKOOLParser.ImmutableattributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attributes.
    def visitAttributes(self, ctx:BKOOLParser.AttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method.
    def visitMethod(self, ctx:BKOOLParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramlist.
    def visitParamlist(self, ctx:BKOOLParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#params.
    def visitParams(self, ctx:BKOOLParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ids.
    def visitIds(self, ctx:BKOOLParser.IdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typedecl.
    def visitTypedecl(self, ctx:BKOOLParser.TypedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#primitype.
    def visitPrimitype(self, ctx:BKOOLParser.PrimitypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arraytype.
    def visitArraytype(self, ctx:BKOOLParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classtype.
    def visitClasstype(self, ctx:BKOOLParser.ClasstypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp.
    def visitExp(self, ctx:BKOOLParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp1.
    def visitExp1(self, ctx:BKOOLParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp2.
    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp3.
    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp4.
    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp5.
    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp6.
    def visitExp6(self, ctx:BKOOLParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp7.
    def visitExp7(self, ctx:BKOOLParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp8.
    def visitExp8(self, ctx:BKOOLParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp9.
    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp10.
    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#explist.
    def visitExplist(self, ctx:BKOOLParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exps.
    def visitExps(self, ctx:BKOOLParser.ExpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#operands.
    def visitOperands(self, ctx:BKOOLParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockstatement.
    def visitBlockstatement(self, ctx:BKOOLParser.BlockstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecllist.
    def visitVardecllist(self, ctx:BKOOLParser.VardecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecl.
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutablevar.
    def visitMutablevar(self, ctx:BKOOLParser.MutablevarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutablevar.
    def visitImmutablevar(self, ctx:BKOOLParser.ImmutablevarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#variables.
    def visitVariables(self, ctx:BKOOLParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statementlist.
    def visitStatementlist(self, ctx:BKOOLParser.StatementlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statement.
    def visitStatement(self, ctx:BKOOLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignstatement.
    def visitAssignstatement(self, ctx:BKOOLParser.AssignstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutableattr.
    def visitMutableattr(self, ctx:BKOOLParser.MutableattrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#localvar.
    def visitLocalvar(self, ctx:BKOOLParser.LocalvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#eleofarray.
    def visitEleofarray(self, ctx:BKOOLParser.EleofarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ifstatement.
    def visitIfstatement(self, ctx:BKOOLParser.IfstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#forstatement.
    def visitForstatement(self, ctx:BKOOLParser.ForstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#breakstatement.
    def visitBreakstatement(self, ctx:BKOOLParser.BreakstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continuestatement.
    def visitContinuestatement(self, ctx:BKOOLParser.ContinuestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#returnstatement.
    def visitReturnstatement(self, ctx:BKOOLParser.ReturnstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodinvostatement.
    def visitMethodinvostatement(self, ctx:BKOOLParser.MethodinvostatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arraylit.
    def visitArraylit(self, ctx:BKOOLParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arraylitlist.
    def visitArraylitlist(self, ctx:BKOOLParser.ArraylitlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayintlit.
    def visitArrayintlit(self, ctx:BKOOLParser.ArrayintlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayfloatlit.
    def visitArrayfloatlit(self, ctx:BKOOLParser.ArrayfloatlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arraystringlit.
    def visitArraystringlit(self, ctx:BKOOLParser.ArraystringlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayboolit.
    def visitArrayboolit(self, ctx:BKOOLParser.ArrayboolitContext):
        return self.visitChildren(ctx)



del BKOOLParser