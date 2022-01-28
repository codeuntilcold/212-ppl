# Generated from d:\1_University\HK212\prin_prog_lang\LAB\initial\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write(":\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\3\2\3\3\3\3\5\3\30\n\3\3\3\5\3\33")
        buf.write("\n\3\3\3\5\3\36\n\3\3\4\3\4\3\4\7\4#\n\4\f\4\16\4&\13")
        buf.write("\4\5\4(\n\4\3\4\3\4\3\5\6\5-\n\5\r\5\16\5.\3\5\3\5\3\6")
        buf.write("\3\6\3\7\3\7\3\b\3\b\3\t\3\t\2\2\n\3\2\5\2\7\3\t\4\13")
        buf.write("\5\r\6\17\7\21\b\3\2\7\3\2\62;\3\2\63;\3\2\62\62\4\2\62")
        buf.write(";aa\5\2\13\f\17\17\"\"\2=\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3\23\3")
        buf.write("\2\2\2\5\35\3\2\2\2\7\'\3\2\2\2\t,\3\2\2\2\13\62\3\2\2")
        buf.write("\2\r\64\3\2\2\2\17\66\3\2\2\2\218\3\2\2\2\23\24\t\2\2")
        buf.write("\2\24\4\3\2\2\2\25\27\t\3\2\2\26\30\t\2\2\2\27\26\3\2")
        buf.write("\2\2\27\30\3\2\2\2\30\32\3\2\2\2\31\33\t\2\2\2\32\31\3")
        buf.write("\2\2\2\32\33\3\2\2\2\33\36\3\2\2\2\34\36\t\4\2\2\35\25")
        buf.write("\3\2\2\2\35\34\3\2\2\2\36\6\3\2\2\2\37(\t\4\2\2 $\t\3")
        buf.write("\2\2!#\t\5\2\2\"!\3\2\2\2#&\3\2\2\2$\"\3\2\2\2$%\3\2\2")
        buf.write("\2%(\3\2\2\2&$\3\2\2\2\'\37\3\2\2\2\' \3\2\2\2()\3\2\2")
        buf.write("\2)*\b\4\2\2*\b\3\2\2\2+-\t\6\2\2,+\3\2\2\2-.\3\2\2\2")
        buf.write(".,\3\2\2\2./\3\2\2\2/\60\3\2\2\2\60\61\b\5\3\2\61\n\3")
        buf.write("\2\2\2\62\63\13\2\2\2\63\f\3\2\2\2\64\65\13\2\2\2\65\16")
        buf.write("\3\2\2\2\66\67\13\2\2\2\67\20\3\2\2\289\13\2\2\29\22\3")
        buf.write("\2\2\2\t\2\27\32\35$\'.\4\3\4\2\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PHPINT = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5
    UNTERMINATED_COMMENT = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "PHPINT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "DIGIT", "IPCOM", "PHPINT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[2] = self.PHPINT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def PHPINT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    if '_' in self.text:
                        self.text = self.text.replace('_','')
                
     


