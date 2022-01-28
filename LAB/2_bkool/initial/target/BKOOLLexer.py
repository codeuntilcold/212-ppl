# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\'\n\5\3\6\6")
        buf.write("\6*\n\6\r\6\16\6+\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\2\2\13\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\3\2\4\4\2C\\c|\5\2\13\f\17\17\"\"\29\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3\25\3\2")
        buf.write("\2\2\5\27\3\2\2\2\7\31\3\2\2\2\t&\3\2\2\2\13)\3\2\2\2")
        buf.write("\r-\3\2\2\2\17/\3\2\2\2\21\61\3\2\2\2\23\65\3\2\2\2\25")
        buf.write("\26\7*\2\2\26\4\3\2\2\2\27\30\7+\2\2\30\6\3\2\2\2\31\32")
        buf.write("\7d\2\2\32\33\7q\2\2\33\34\7f\2\2\34\35\7{\2\2\35\b\3")
        buf.write("\2\2\2\36\37\7k\2\2\37 \7p\2\2 \'\7v\2\2!\"\7h\2\2\"#")
        buf.write("\7n\2\2#$\7q\2\2$%\7c\2\2%\'\7v\2\2&\36\3\2\2\2&!\3\2")
        buf.write("\2\2\'\n\3\2\2\2(*\t\2\2\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2")
        buf.write("\2+,\3\2\2\2,\f\3\2\2\2-.\7.\2\2.\16\3\2\2\2/\60\7=\2")
        buf.write("\2\60\20\3\2\2\2\61\62\t\3\2\2\62\63\3\2\2\2\63\64\b\t")
        buf.write("\2\2\64\22\3\2\2\2\65\66\13\2\2\2\66\67\b\n\3\2\67\24")
        buf.write("\3\2\2\2\5\2&+\4\b\2\2\3\n\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    TYPE = 4
    ID = 5
    COMMA = 6
    SEMI = 7
    WS = 8
    ERROR_CHAR = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'body'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "TYPE", "ID", "COMMA", "SEMI", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "TYPE", "ID", "COMMA", "SEMI", 
                  "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[8] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


