# Generated from d:\1_University\HK212\prin_prog_lang\LAB\bkool\initial\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("F\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\5\3\36\n\3\3\4\3\4\5\4\"\n\4\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\5\7\60\n\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\5\b9\n\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\5")
        buf.write("\nB\n\n\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2")
        buf.write("\2\2@\2\26\3\2\2\2\4\35\3\2\2\2\6!\3\2\2\2\b#\3\2\2\2")
        buf.write("\n\'\3\2\2\2\f,\3\2\2\2\168\3\2\2\2\20:\3\2\2\2\22A\3")
        buf.write("\2\2\2\24C\3\2\2\2\26\27\5\4\3\2\27\30\7\2\2\3\30\3\3")
        buf.write("\2\2\2\31\32\5\6\4\2\32\33\5\4\3\2\33\36\3\2\2\2\34\36")
        buf.write("\5\6\4\2\35\31\3\2\2\2\35\34\3\2\2\2\36\5\3\2\2\2\37\"")
        buf.write("\5\b\5\2 \"\5\n\6\2!\37\3\2\2\2! \3\2\2\2\"\7\3\2\2\2")
        buf.write("#$\7\6\2\2$%\5\22\n\2%&\7\t\2\2&\t\3\2\2\2\'(\7\6\2\2")
        buf.write("()\7\7\2\2)*\5\f\7\2*+\5\24\13\2+\13\3\2\2\2,/\7\3\2\2")
        buf.write("-\60\5\16\b\2.\60\3\2\2\2/-\3\2\2\2/.\3\2\2\2\60\61\3")
        buf.write("\2\2\2\61\62\7\4\2\2\62\r\3\2\2\2\63\64\5\20\t\2\64\65")
        buf.write("\7\t\2\2\65\66\5\16\b\2\669\3\2\2\2\679\5\20\t\28\63\3")
        buf.write("\2\2\28\67\3\2\2\29\17\3\2\2\2:;\7\6\2\2;<\5\22\n\2<\21")
        buf.write("\3\2\2\2=>\7\7\2\2>?\7\b\2\2?B\5\22\n\2@B\7\7\2\2A=\3")
        buf.write("\2\2\2A@\3\2\2\2B\23\3\2\2\2CD\7\5\2\2D\25\3\2\2\2\7\35")
        buf.write("!/8A")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'body'", "<INVALID>", "<INVALID>", 
                     "','", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TYPE", "ID", "COMMA", "SEMI", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_funcdecl = 4
    RULE_paramdecl = 5
    RULE_paramlist = 6
    RULE_param = 7
    RULE_idlist = 8
    RULE_body = 9

    ruleNames =  [ "program", "decls", "decl", "vardecl", "funcdecl", "paramdecl", 
                   "paramlist", "param", "idlist", "body" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    TYPE=4
    ID=5
    COMMA=6
    SEMI=7
    WS=8
    ERROR_CHAR=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decls(self):
            return self.getTypedRuleContext(BKOOLParser.DeclsContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.decls()
            self.state = 21
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(BKOOLParser.DeclContext,0)


        def decls(self):
            return self.getTypedRuleContext(BKOOLParser.DeclsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decls




    def decls(self):

        localctx = BKOOLParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.decl()
                self.state = 24
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(BKOOLParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decl




    def decl(self):

        localctx = BKOOLParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(BKOOLParser.TYPE, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(BKOOLParser.TYPE)
            self.state = 34
            self.idlist()
            self.state = 35
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(BKOOLParser.TYPE, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def paramdecl(self):
            return self.getTypedRuleContext(BKOOLParser.ParamdeclContext,0)


        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcdecl




    def funcdecl(self):

        localctx = BKOOLParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(BKOOLParser.TYPE)
            self.state = 38
            self.match(BKOOLParser.ID)
            self.state = 39
            self.paramdecl()
            self.state = 40
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramdecl




    def paramdecl(self):

        localctx = BKOOLParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paramdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(BKOOLParser.T__0)
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.TYPE]:
                self.state = 43
                self.paramlist()
                pass
            elif token in [BKOOLParser.T__1]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 47
            self.match(BKOOLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramlist




    def paramlist(self):

        localctx = BKOOLParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paramlist)
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.param()
                self.state = 50
                self.match(BKOOLParser.SEMI)
                self.state = 51
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(BKOOLParser.TYPE, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(BKOOLParser.TYPE)
            self.state = 57
            self.idlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idlist




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_idlist)
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(BKOOLParser.ID)
                self.state = 60
                self.match(BKOOLParser.COMMA)
                self.state = 61
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKOOLParser.RULE_body




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(BKOOLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





