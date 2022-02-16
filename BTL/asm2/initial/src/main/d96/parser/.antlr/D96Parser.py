# Generated from d:\1_University\HK212\prin_prog_lang\BTL\asm2\initial\src\main\d96\parser\D96.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u020f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5")
        buf.write("\3j\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\5\4z\n\4\3\5\3\5\3\5\3\5\5\5\u0080\n\5\3\6")
        buf.write("\3\6\5\6\u0084\n\6\3\7\3\7\3\7\5\7\u0089\n\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\t\u0096\n\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00a4\n")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\5\13\u00b6\n\13\3\f\3\f\5")
        buf.write("\f\u00ba\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00c1\n\r\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\5\20\u00cf\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u00d6\n")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\5\22\u00dd\n\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\7\23\u00e5\n\23\f\23\16\23\u00e8")
        buf.write("\13\23\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00f0\n\24\f")
        buf.write("\24\16\24\u00f3\13\24\3\25\3\25\3\25\3\25\3\25\3\25\7")
        buf.write("\25\u00fb\n\25\f\25\16\25\u00fe\13\25\3\26\3\26\3\26\5")
        buf.write("\26\u0103\n\26\3\27\3\27\3\27\5\27\u0108\n\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u0112\n\30\f\30\16")
        buf.write("\30\u0115\13\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\7\31\u0124\n\31\f\31\16\31\u0127")
        buf.write("\13\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\5\32\u0134\n\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\5\33\u013d\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\5\34\u014b\n\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\5\35\u015d\n\35\3\36\3\36\3\36\3\37\3")
        buf.write("\37\3\37\5\37\u0165\n\37\3 \3 \3 \3 \3!\3!\3!\3!\5!\u016f")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5")
        buf.write("\"\u017d\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u0189\n")
        buf.write("#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u019b")
        buf.write("\n$\3%\3%\3%\3%\3%\3%\3%\3%\5%\u01a5\n%\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\5")
        buf.write("&\u01bd\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\5\'\u01cf\n\'\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\5(\u01d9\n(\3)\3)\3)\3)\3)\3*\3*\3*\5*\u01e3\n*\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u01f5")
        buf.write("\n+\3,\3,\3-\3-\3-\3-\3-\3.\3.\5.\u0200\n.\3/\3/\3/\3")
        buf.write("/\3/\5/\u0207\n/\3\60\3\60\5\60\u020b\n\60\3\61\3\61\3")
        buf.write("\61\2\7$&(.\60\62\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`\2\n\3\2")
        buf.write("\4\5\3\2\37 \3\2$)\3\2!\"\3\2\32\33\3\2\34\36\3\2\24\27")
        buf.write("\3\2\66\67\2\u0218\2b\3\2\2\2\4i\3\2\2\2\6y\3\2\2\2\b")
        buf.write("\177\3\2\2\2\n\u0083\3\2\2\2\f\u0085\3\2\2\2\16\u008c")
        buf.write("\3\2\2\2\20\u0095\3\2\2\2\22\u00a3\3\2\2\2\24\u00b5\3")
        buf.write("\2\2\2\26\u00b9\3\2\2\2\30\u00c0\3\2\2\2\32\u00c2\3\2")
        buf.write("\2\2\34\u00c6\3\2\2\2\36\u00ce\3\2\2\2 \u00d5\3\2\2\2")
        buf.write("\"\u00dc\3\2\2\2$\u00de\3\2\2\2&\u00e9\3\2\2\2(\u00f4")
        buf.write("\3\2\2\2*\u0102\3\2\2\2,\u0107\3\2\2\2.\u0109\3\2\2\2")
        buf.write("\60\u0116\3\2\2\2\62\u0133\3\2\2\2\64\u013c\3\2\2\2\66")
        buf.write("\u014a\3\2\2\28\u015c\3\2\2\2:\u015e\3\2\2\2<\u0161\3")
        buf.write("\2\2\2>\u0166\3\2\2\2@\u016e\3\2\2\2B\u017c\3\2\2\2D\u0188")
        buf.write("\3\2\2\2F\u019a\3\2\2\2H\u01a4\3\2\2\2J\u01bc\3\2\2\2")
        buf.write("L\u01ce\3\2\2\2N\u01d8\3\2\2\2P\u01da\3\2\2\2R\u01e2\3")
        buf.write("\2\2\2T\u01f4\3\2\2\2V\u01f6\3\2\2\2X\u01f8\3\2\2\2Z\u01ff")
        buf.write("\3\2\2\2\\\u0206\3\2\2\2^\u020a\3\2\2\2`\u020c\3\2\2\2")
        buf.write("bc\5\4\3\2cd\7\2\2\3d\3\3\2\2\2ef\5\6\4\2fg\5\4\3\2gj")
        buf.write("\3\2\2\2hj\5\6\4\2ie\3\2\2\2ih\3\2\2\2j\5\3\2\2\2kl\7")
        buf.write("\3\2\2lm\7\66\2\2mn\7/\2\2no\5\b\5\2op\7\60\2\2pz\3\2")
        buf.write("\2\2qr\7\3\2\2rs\7\66\2\2st\7\64\2\2tu\7\66\2\2uv\7/\2")
        buf.write("\2vw\5\b\5\2wx\7\60\2\2xz\3\2\2\2yk\3\2\2\2yq\3\2\2\2")
        buf.write("z\7\3\2\2\2{|\5\n\6\2|}\5\b\5\2}\u0080\3\2\2\2~\u0080")
        buf.write("\3\2\2\2\177{\3\2\2\2\177~\3\2\2\2\u0080\t\3\2\2\2\u0081")
        buf.write("\u0084\5\f\7\2\u0082\u0084\5\24\13\2\u0083\u0081\3\2\2")
        buf.write("\2\u0083\u0082\3\2\2\2\u0084\13\3\2\2\2\u0085\u0088\t")
        buf.write("\2\2\2\u0086\u0089\5\16\b\2\u0087\u0089\5\22\n\2\u0088")
        buf.write("\u0086\3\2\2\2\u0088\u0087\3\2\2\2\u0089\u008a\3\2\2\2")
        buf.write("\u008a\u008b\7\65\2\2\u008b\r\3\2\2\2\u008c\u008d\5\20")
        buf.write("\t\2\u008d\u008e\7\64\2\2\u008e\u008f\5R*\2\u008f\17\3")
        buf.write("\2\2\2\u0090\u0091\5`\61\2\u0091\u0092\7\63\2\2\u0092")
        buf.write("\u0093\5\20\t\2\u0093\u0096\3\2\2\2\u0094\u0096\5`\61")
        buf.write("\2\u0095\u0090\3\2\2\2\u0095\u0094\3\2\2\2\u0096\21\3")
        buf.write("\2\2\2\u0097\u0098\5`\61\2\u0098\u0099\7\63\2\2\u0099")
        buf.write("\u009a\5\22\n\2\u009a\u009b\7\63\2\2\u009b\u009c\5 \21")
        buf.write("\2\u009c\u00a4\3\2\2\2\u009d\u009e\5`\61\2\u009e\u009f")
        buf.write("\7\64\2\2\u009f\u00a0\5R*\2\u00a0\u00a1\7,\2\2\u00a1\u00a2")
        buf.write("\5 \21\2\u00a2\u00a4\3\2\2\2\u00a3\u0097\3\2\2\2\u00a3")
        buf.write("\u009d\3\2\2\2\u00a4\23\3\2\2\2\u00a5\u00a6\5`\61\2\u00a6")
        buf.write("\u00a7\7-\2\2\u00a7\u00a8\5\26\f\2\u00a8\u00a9\7.\2\2")
        buf.write("\u00a9\u00aa\5\34\17\2\u00aa\u00b6\3\2\2\2\u00ab\u00ac")
        buf.write("\7\22\2\2\u00ac\u00ad\7-\2\2\u00ad\u00ae\5\26\f\2\u00ae")
        buf.write("\u00af\7.\2\2\u00af\u00b0\5\34\17\2\u00b0\u00b6\3\2\2")
        buf.write("\2\u00b1\u00b2\7\23\2\2\u00b2\u00b3\7-\2\2\u00b3\u00b4")
        buf.write("\7.\2\2\u00b4\u00b6\5\34\17\2\u00b5\u00a5\3\2\2\2\u00b5")
        buf.write("\u00ab\3\2\2\2\u00b5\u00b1\3\2\2\2\u00b6\25\3\2\2\2\u00b7")
        buf.write("\u00ba\5\30\r\2\u00b8\u00ba\3\2\2\2\u00b9\u00b7\3\2\2")
        buf.write("\2\u00b9\u00b8\3\2\2\2\u00ba\27\3\2\2\2\u00bb\u00bc\5")
        buf.write("\32\16\2\u00bc\u00bd\7\65\2\2\u00bd\u00be\5\30\r\2\u00be")
        buf.write("\u00c1\3\2\2\2\u00bf\u00c1\5\32\16\2\u00c0\u00bb\3\2\2")
        buf.write("\2\u00c0\u00bf\3\2\2\2\u00c1\31\3\2\2\2\u00c2\u00c3\5")
        buf.write("@!\2\u00c3\u00c4\7\64\2\2\u00c4\u00c5\5R*\2\u00c5\33\3")
        buf.write("\2\2\2\u00c6\u00c7\7/\2\2\u00c7\u00c8\5\36\20\2\u00c8")
        buf.write("\u00c9\7\60\2\2\u00c9\35\3\2\2\2\u00ca\u00cb\58\35\2\u00cb")
        buf.write("\u00cc\5\36\20\2\u00cc\u00cf\3\2\2\2\u00cd\u00cf\3\2\2")
        buf.write("\2\u00ce\u00ca\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf\37\3")
        buf.write("\2\2\2\u00d0\u00d1\5\"\22\2\u00d1\u00d2\t\3\2\2\u00d2")
        buf.write("\u00d3\5\"\22\2\u00d3\u00d6\3\2\2\2\u00d4\u00d6\5\"\22")
        buf.write("\2\u00d5\u00d0\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6!\3\2")
        buf.write("\2\2\u00d7\u00d8\5$\23\2\u00d8\u00d9\t\4\2\2\u00d9\u00da")
        buf.write("\5$\23\2\u00da\u00dd\3\2\2\2\u00db\u00dd\5$\23\2\u00dc")
        buf.write("\u00d7\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd#\3\2\2\2\u00de")
        buf.write("\u00df\b\23\1\2\u00df\u00e0\5&\24\2\u00e0\u00e6\3\2\2")
        buf.write("\2\u00e1\u00e2\f\4\2\2\u00e2\u00e3\t\5\2\2\u00e3\u00e5")
        buf.write("\5&\24\2\u00e4\u00e1\3\2\2\2\u00e5\u00e8\3\2\2\2\u00e6")
        buf.write("\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7%\3\2\2\2\u00e8")
        buf.write("\u00e6\3\2\2\2\u00e9\u00ea\b\24\1\2\u00ea\u00eb\5(\25")
        buf.write("\2\u00eb\u00f1\3\2\2\2\u00ec\u00ed\f\4\2\2\u00ed\u00ee")
        buf.write("\t\6\2\2\u00ee\u00f0\5(\25\2\u00ef\u00ec\3\2\2\2\u00f0")
        buf.write("\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2")
        buf.write("\u00f2\'\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f5\b\25")
        buf.write("\1\2\u00f5\u00f6\5*\26\2\u00f6\u00fc\3\2\2\2\u00f7\u00f8")
        buf.write("\f\4\2\2\u00f8\u00f9\t\7\2\2\u00f9\u00fb\5*\26\2\u00fa")
        buf.write("\u00f7\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2")
        buf.write("\u00fc\u00fd\3\2\2\2\u00fd)\3\2\2\2\u00fe\u00fc\3\2\2")
        buf.write("\2\u00ff\u0100\7#\2\2\u0100\u0103\5*\26\2\u0101\u0103")
        buf.write("\5,\27\2\u0102\u00ff\3\2\2\2\u0102\u0101\3\2\2\2\u0103")
        buf.write("+\3\2\2\2\u0104\u0105\7\33\2\2\u0105\u0108\5,\27\2\u0106")
        buf.write("\u0108\5.\30\2\u0107\u0104\3\2\2\2\u0107\u0106\3\2\2\2")
        buf.write("\u0108-\3\2\2\2\u0109\u010a\b\30\1\2\u010a\u010b\5\60")
        buf.write("\31\2\u010b\u0113\3\2\2\2\u010c\u010d\f\4\2\2\u010d\u010e")
        buf.write("\7\61\2\2\u010e\u010f\5 \21\2\u010f\u0110\7\62\2\2\u0110")
        buf.write("\u0112\3\2\2\2\u0111\u010c\3\2\2\2\u0112\u0115\3\2\2\2")
        buf.write("\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114/\3\2\2")
        buf.write("\2\u0115\u0113\3\2\2\2\u0116\u0117\b\31\1\2\u0117\u0118")
        buf.write("\5\62\32\2\u0118\u0125\3\2\2\2\u0119\u011a\f\5\2\2\u011a")
        buf.write("\u011b\7*\2\2\u011b\u0124\7\66\2\2\u011c\u011d\f\4\2\2")
        buf.write("\u011d\u011e\7*\2\2\u011e\u011f\7\66\2\2\u011f\u0120\7")
        buf.write("-\2\2\u0120\u0121\5^\60\2\u0121\u0122\7.\2\2\u0122\u0124")
        buf.write("\3\2\2\2\u0123\u0119\3\2\2\2\u0123\u011c\3\2\2\2\u0124")
        buf.write("\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2")
        buf.write("\u0126\61\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u0129\7\66")
        buf.write("\2\2\u0129\u012a\7+\2\2\u012a\u0134\7\67\2\2\u012b\u012c")
        buf.write("\7\66\2\2\u012c\u012d\7+\2\2\u012d\u012e\7\67\2\2\u012e")
        buf.write("\u012f\7-\2\2\u012f\u0130\5^\60\2\u0130\u0131\7.\2\2\u0131")
        buf.write("\u0134\3\2\2\2\u0132\u0134\5\64\33\2\u0133\u0128\3\2\2")
        buf.write("\2\u0133\u012b\3\2\2\2\u0133\u0132\3\2\2\2\u0134\63\3")
        buf.write("\2\2\2\u0135\u0136\7\16\2\2\u0136\u0137\7\66\2\2\u0137")
        buf.write("\u0138\7-\2\2\u0138\u0139\5^\60\2\u0139\u013a\7.\2\2\u013a")
        buf.write("\u013d\3\2\2\2\u013b\u013d\5\66\34\2\u013c\u0135\3\2\2")
        buf.write("\2\u013c\u013b\3\2\2\2\u013d\65\3\2\2\2\u013e\u013f\7")
        buf.write("-\2\2\u013f\u0140\5 \21\2\u0140\u0141\7.\2\2\u0141\u014b")
        buf.write("\3\2\2\2\u0142\u014b\7\66\2\2\u0143\u014b\7\r\2\2\u0144")
        buf.write("\u014b\7\31\2\2\u0145\u014b\78\2\2\u0146\u014b\79\2\2")
        buf.write("\u0147\u014b\7:\2\2\u0148\u014b\7;\2\2\u0149\u014b\5X")
        buf.write("-\2\u014a\u013e\3\2\2\2\u014a\u0142\3\2\2\2\u014a\u0143")
        buf.write("\3\2\2\2\u014a\u0144\3\2\2\2\u014a\u0145\3\2\2\2\u014a")
        buf.write("\u0146\3\2\2\2\u014a\u0147\3\2\2\2\u014a\u0148\3\2\2\2")
        buf.write("\u014a\u0149\3\2\2\2\u014b\67\3\2\2\2\u014c\u015d\5:\36")
        buf.write("\2\u014d\u015d\5D#\2\u014e\u015d\5F$\2\u014f\u015d\5J")
        buf.write("&\2\u0150\u0151\7\17\2\2\u0151\u015d\7\65\2\2\u0152\u0153")
        buf.write("\7\20\2\2\u0153\u015d\7\65\2\2\u0154\u0155\7\21\2\2\u0155")
        buf.write("\u015d\7\65\2\2\u0156\u0157\7\21\2\2\u0157\u0158\5 \21")
        buf.write("\2\u0158\u0159\7\65\2\2\u0159\u015d\3\2\2\2\u015a\u015d")
        buf.write("\5L\'\2\u015b\u015d\5\34\17\2\u015c\u014c\3\2\2\2\u015c")
        buf.write("\u014d\3\2\2\2\u015c\u014e\3\2\2\2\u015c\u014f\3\2\2\2")
        buf.write("\u015c\u0150\3\2\2\2\u015c\u0152\3\2\2\2\u015c\u0154\3")
        buf.write("\2\2\2\u015c\u0156\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015b")
        buf.write("\3\2\2\2\u015d9\3\2\2\2\u015e\u015f\5<\37\2\u015f\u0160")
        buf.write("\7\65\2\2\u0160;\3\2\2\2\u0161\u0164\t\2\2\2\u0162\u0165")
        buf.write("\5> \2\u0163\u0165\5B\"\2\u0164\u0162\3\2\2\2\u0164\u0163")
        buf.write("\3\2\2\2\u0165=\3\2\2\2\u0166\u0167\5@!\2\u0167\u0168")
        buf.write("\7\64\2\2\u0168\u0169\5R*\2\u0169?\3\2\2\2\u016a\u016b")
        buf.write("\7\66\2\2\u016b\u016c\7\63\2\2\u016c\u016f\5@!\2\u016d")
        buf.write("\u016f\7\66\2\2\u016e\u016a\3\2\2\2\u016e\u016d\3\2\2")
        buf.write("\2\u016fA\3\2\2\2\u0170\u0171\7\66\2\2\u0171\u0172\7\63")
        buf.write("\2\2\u0172\u0173\5B\"\2\u0173\u0174\7\63\2\2\u0174\u0175")
        buf.write("\5 \21\2\u0175\u017d\3\2\2\2\u0176\u0177\7\66\2\2\u0177")
        buf.write("\u0178\7\64\2\2\u0178\u0179\5R*\2\u0179\u017a\7,\2\2\u017a")
        buf.write("\u017b\5 \21\2\u017b\u017d\3\2\2\2\u017c\u0170\3\2\2\2")
        buf.write("\u017c\u0176\3\2\2\2\u017dC\3\2\2\2\u017e\u017f\5N(\2")
        buf.write("\u017f\u0180\7,\2\2\u0180\u0181\5 \21\2\u0181\u0182\7")
        buf.write("\65\2\2\u0182\u0189\3\2\2\2\u0183\u0184\5P)\2\u0184\u0185")
        buf.write("\7,\2\2\u0185\u0186\5 \21\2\u0186\u0187\7\65\2\2\u0187")
        buf.write("\u0189\3\2\2\2\u0188\u017e\3\2\2\2\u0188\u0183\3\2\2\2")
        buf.write("\u0189E\3\2\2\2\u018a\u018b\7\6\2\2\u018b\u018c\7-\2\2")
        buf.write("\u018c\u018d\5 \21\2\u018d\u018e\7.\2\2\u018e\u018f\5")
        buf.write("\34\17\2\u018f\u0190\5H%\2\u0190\u019b\3\2\2\2\u0191\u0192")
        buf.write("\7\6\2\2\u0192\u0193\7-\2\2\u0193\u0194\5 \21\2\u0194")
        buf.write("\u0195\7.\2\2\u0195\u0196\5\34\17\2\u0196\u0197\5H%\2")
        buf.write("\u0197\u0198\7\7\2\2\u0198\u0199\5\34\17\2\u0199\u019b")
        buf.write("\3\2\2\2\u019a\u018a\3\2\2\2\u019a\u0191\3\2\2\2\u019b")
        buf.write("G\3\2\2\2\u019c\u019d\7\b\2\2\u019d\u019e\7-\2\2\u019e")
        buf.write("\u019f\5 \21\2\u019f\u01a0\7.\2\2\u01a0\u01a1\5\34\17")
        buf.write("\2\u01a1\u01a2\5H%\2\u01a2\u01a5\3\2\2\2\u01a3\u01a5\3")
        buf.write("\2\2\2\u01a4\u019c\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5I")
        buf.write("\3\2\2\2\u01a6\u01a7\7\t\2\2\u01a7\u01a8\7-\2\2\u01a8")
        buf.write("\u01a9\5N(\2\u01a9\u01aa\7\n\2\2\u01aa\u01ab\5 \21\2\u01ab")
        buf.write("\u01ac\7\f\2\2\u01ac\u01ad\5 \21\2\u01ad\u01ae\7.\2\2")
        buf.write("\u01ae\u01af\5\34\17\2\u01af\u01bd\3\2\2\2\u01b0\u01b1")
        buf.write("\7\t\2\2\u01b1\u01b2\7-\2\2\u01b2\u01b3\5N(\2\u01b3\u01b4")
        buf.write("\7\n\2\2\u01b4\u01b5\5 \21\2\u01b5\u01b6\7\f\2\2\u01b6")
        buf.write("\u01b7\5 \21\2\u01b7\u01b8\7\13\2\2\u01b8\u01b9\5 \21")
        buf.write("\2\u01b9\u01ba\7.\2\2\u01ba\u01bb\5\34\17\2\u01bb\u01bd")
        buf.write("\3\2\2\2\u01bc\u01a6\3\2\2\2\u01bc\u01b0\3\2\2\2\u01bd")
        buf.write("K\3\2\2\2\u01be\u01bf\5\60\31\2\u01bf\u01c0\7*\2\2\u01c0")
        buf.write("\u01c1\7\66\2\2\u01c1\u01c2\7-\2\2\u01c2\u01c3\5^\60\2")
        buf.write("\u01c3\u01c4\7.\2\2\u01c4\u01c5\7\65\2\2\u01c5\u01cf\3")
        buf.write("\2\2\2\u01c6\u01c7\7\66\2\2\u01c7\u01c8\7+\2\2\u01c8\u01c9")
        buf.write("\7\67\2\2\u01c9\u01ca\7-\2\2\u01ca\u01cb\5^\60\2\u01cb")
        buf.write("\u01cc\7.\2\2\u01cc\u01cd\7\65\2\2\u01cd\u01cf\3\2\2\2")
        buf.write("\u01ce\u01be\3\2\2\2\u01ce\u01c6\3\2\2\2\u01cfM\3\2\2")
        buf.write("\2\u01d0\u01d9\7\66\2\2\u01d1\u01d2\5\60\31\2\u01d2\u01d3")
        buf.write("\7*\2\2\u01d3\u01d4\7\66\2\2\u01d4\u01d9\3\2\2\2\u01d5")
        buf.write("\u01d6\7\66\2\2\u01d6\u01d7\7+\2\2\u01d7\u01d9\7\67\2")
        buf.write("\2\u01d8\u01d0\3\2\2\2\u01d8\u01d1\3\2\2\2\u01d8\u01d5")
        buf.write("\3\2\2\2\u01d9O\3\2\2\2\u01da\u01db\5.\30\2\u01db\u01dc")
        buf.write("\7\61\2\2\u01dc\u01dd\5 \21\2\u01dd\u01de\7\62\2\2\u01de")
        buf.write("Q\3\2\2\2\u01df\u01e3\5V,\2\u01e0\u01e3\5T+\2\u01e1\u01e3")
        buf.write("\7\66\2\2\u01e2\u01df\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2")
        buf.write("\u01e1\3\2\2\2\u01e3S\3\2\2\2\u01e4\u01e5\7\30\2\2\u01e5")
        buf.write("\u01e6\7\61\2\2\u01e6\u01e7\5T+\2\u01e7\u01e8\7\63\2\2")
        buf.write("\u01e8\u01e9\6+\b\2\u01e9\u01ea\78\2\2\u01ea\u01eb\7\62")
        buf.write("\2\2\u01eb\u01f5\3\2\2\2\u01ec\u01ed\7\30\2\2\u01ed\u01ee")
        buf.write("\7\61\2\2\u01ee\u01ef\5V,\2\u01ef\u01f0\7\63\2\2\u01f0")
        buf.write("\u01f1\6+\t\2\u01f1\u01f2\78\2\2\u01f2\u01f3\7\62\2\2")
        buf.write("\u01f3\u01f5\3\2\2\2\u01f4\u01e4\3\2\2\2\u01f4\u01ec\3")
        buf.write("\2\2\2\u01f5U\3\2\2\2\u01f6\u01f7\t\b\2\2\u01f7W\3\2\2")
        buf.write("\2\u01f8\u01f9\7\30\2\2\u01f9\u01fa\7-\2\2\u01fa\u01fb")
        buf.write("\5Z.\2\u01fb\u01fc\7.\2\2\u01fcY\3\2\2\2\u01fd\u0200\5")
        buf.write("\\/\2\u01fe\u0200\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff\u01fe")
        buf.write("\3\2\2\2\u0200[\3\2\2\2\u0201\u0202\5 \21\2\u0202\u0203")
        buf.write("\7\63\2\2\u0203\u0204\5\\/\2\u0204\u0207\3\2\2\2\u0205")
        buf.write("\u0207\5 \21\2\u0206\u0201\3\2\2\2\u0206\u0205\3\2\2\2")
        buf.write("\u0207]\3\2\2\2\u0208\u020b\5\\/\2\u0209\u020b\3\2\2\2")
        buf.write("\u020a\u0208\3\2\2\2\u020a\u0209\3\2\2\2\u020b_\3\2\2")
        buf.write("\2\u020c\u020d\t\t\2\2\u020da\3\2\2\2)iy\177\u0083\u0088")
        buf.write("\u0095\u00a3\u00b5\u00b9\u00c0\u00ce\u00d5\u00dc\u00e6")
        buf.write("\u00f1\u00fc\u0102\u0107\u0113\u0123\u0125\u0133\u013c")
        buf.write("\u014a\u015c\u0164\u016e\u017c\u0188\u019a\u01a4\u01bc")
        buf.write("\u01ce\u01d8\u01e2\u01f4\u01ff\u0206\u020a")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Class'", "'Val'", "'Var'", "'If'", "'Else'", 
                     "'Elseif'", "'Foreach'", "'In'", "'By'", "'..'", "'Self'", 
                     "'New'", "'Break'", "'Continue'", "'Return'", "'Constructor'", 
                     "'Destructor'", "'String'", "'Boolean'", "'Int'", "'Float'", 
                     "'Array'", "'Null'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'+.'", "'==.'", "'&&'", "'||'", "'!'", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'.'", "'::'", "'='", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "':'", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "VAL", "VAR", "IF", "ELSE", 
                      "ELSEIF", "FOREACH", "IN", "BY", "DOTDOT", "SELF", 
                      "NEW", "BREAK", "CONTINUE", "RETURN", "CONSTRUCTOR", 
                      "DESTRUCTOR", "STRINGTYPE", "BOOLTYPE", "INTTYPE", 
                      "FLOATTYPE", "ARRAY", "NULL", "ADDOP", "SUBOP", "MULOP", 
                      "DIVOP", "MODOP", "CONCAT", "STRCOMP", "AND", "OR", 
                      "NOT", "EQ", "NE", "LT", "LTE", "GT", "GTE", "DOT", 
                      "DBCOLON", "ASSIGNOP", "LP", "RP", "LCB", "RCB", "LSB", 
                      "RSB", "COMMA", "COLON", "SEMI", "ID", "STATIC_ID", 
                      "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "COMMENT", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classDecls = 1
    RULE_classDecl = 2
    RULE_memDeclList = 3
    RULE_memDecl = 4
    RULE_attrDecl = 5
    RULE_attrs = 6
    RULE_memIds = 7
    RULE_attrsInit = 8
    RULE_methodDecl = 9
    RULE_paramList = 10
    RULE_params = 11
    RULE_param = 12
    RULE_blockStat = 13
    RULE_statList = 14
    RULE_expr = 15
    RULE_expr1 = 16
    RULE_expr2 = 17
    RULE_expr3 = 18
    RULE_expr4 = 19
    RULE_expr5 = 20
    RULE_expr6 = 21
    RULE_expr7 = 22
    RULE_expr8 = 23
    RULE_expr9 = 24
    RULE_expr10 = 25
    RULE_operand = 26
    RULE_stat = 27
    RULE_declStat = 28
    RULE_varDecl = 29
    RULE_variables = 30
    RULE_ids = 31
    RULE_varsInit = 32
    RULE_assignStat = 33
    RULE_ifStat = 34
    RULE_elseifList = 35
    RULE_forStat = 36
    RULE_methodCall = 37
    RULE_scalarVar = 38
    RULE_indexExpr = 39
    RULE_typeDecl = 40
    RULE_arrayType = 41
    RULE_primitiveType = 42
    RULE_arrayLit = 43
    RULE_exprList = 44
    RULE_exprs = 45
    RULE_argList = 46
    RULE_memId = 47

    ruleNames =  [ "program", "classDecls", "classDecl", "memDeclList", 
                   "memDecl", "attrDecl", "attrs", "memIds", "attrsInit", 
                   "methodDecl", "paramList", "params", "param", "blockStat", 
                   "statList", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "expr8", "expr9", "expr10", 
                   "operand", "stat", "declStat", "varDecl", "variables", 
                   "ids", "varsInit", "assignStat", "ifStat", "elseifList", 
                   "forStat", "methodCall", "scalarVar", "indexExpr", "typeDecl", 
                   "arrayType", "primitiveType", "arrayLit", "exprList", 
                   "exprs", "argList", "memId" ]

    EOF = Token.EOF
    CLASS=1
    VAL=2
    VAR=3
    IF=4
    ELSE=5
    ELSEIF=6
    FOREACH=7
    IN=8
    BY=9
    DOTDOT=10
    SELF=11
    NEW=12
    BREAK=13
    CONTINUE=14
    RETURN=15
    CONSTRUCTOR=16
    DESTRUCTOR=17
    STRINGTYPE=18
    BOOLTYPE=19
    INTTYPE=20
    FLOATTYPE=21
    ARRAY=22
    NULL=23
    ADDOP=24
    SUBOP=25
    MULOP=26
    DIVOP=27
    MODOP=28
    CONCAT=29
    STRCOMP=30
    AND=31
    OR=32
    NOT=33
    EQ=34
    NE=35
    LT=36
    LTE=37
    GT=38
    GTE=39
    DOT=40
    DBCOLON=41
    ASSIGNOP=42
    LP=43
    RP=44
    LCB=45
    RCB=46
    LSB=47
    RSB=48
    COMMA=49
    COLON=50
    SEMI=51
    ID=52
    STATIC_ID=53
    INTLIT=54
    FLOATLIT=55
    BOOLLIT=56
    STRINGLIT=57
    ILLEGAL_ESCAPE=58
    UNCLOSE_STRING=59
    COMMENT=60
    WS=61
    ERROR_CHAR=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    ZEROLIT_ARR = ['0', '00', '0b0', '0B0', '0x0', '0X0']



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDecls(self):
            return self.getTypedRuleContext(D96Parser.ClassDeclsContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.classDecls()
            self.state = 97
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDecl(self):
            return self.getTypedRuleContext(D96Parser.ClassDeclContext,0)


        def classDecls(self):
            return self.getTypedRuleContext(D96Parser.ClassDeclsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classDecls




    def classDecls(self):

        localctx = D96Parser.ClassDeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDecls)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.classDecl()
                self.state = 100
                self.classDecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.classDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def memDeclList(self):
            return self.getTypedRuleContext(D96Parser.MemDeclListContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_classDecl




    def classDecl(self):

        localctx = D96Parser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classDecl)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(D96Parser.CLASS)
                self.state = 106
                self.match(D96Parser.ID)
                self.state = 107
                self.match(D96Parser.LCB)
                self.state = 108
                self.memDeclList()
                self.state = 109
                self.match(D96Parser.RCB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.match(D96Parser.CLASS)
                self.state = 112
                self.match(D96Parser.ID)
                self.state = 113
                self.match(D96Parser.COLON)
                self.state = 114
                self.match(D96Parser.ID)
                self.state = 115
                self.match(D96Parser.LCB)
                self.state = 116
                self.memDeclList()
                self.state = 117
                self.match(D96Parser.RCB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemDeclListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memDecl(self):
            return self.getTypedRuleContext(D96Parser.MemDeclContext,0)


        def memDeclList(self):
            return self.getTypedRuleContext(D96Parser.MemDeclListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_memDeclList




    def memDeclList(self):

        localctx = D96Parser.MemDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_memDeclList)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.STATIC_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.memDecl()
                self.state = 122
                self.memDeclList()
                pass
            elif token in [D96Parser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrDecl(self):
            return self.getTypedRuleContext(D96Parser.AttrDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(D96Parser.MethodDeclContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_memDecl




    def memDecl(self):

        localctx = D96Parser.MemDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_memDecl)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.attrDecl()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.STATIC_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.methodDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def attrs(self):
            return self.getTypedRuleContext(D96Parser.AttrsContext,0)


        def attrsInit(self):
            return self.getTypedRuleContext(D96Parser.AttrsInitContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attrDecl




    def attrDecl(self):

        localctx = D96Parser.AttrDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attrDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 132
                self.attrs()
                pass

            elif la_ == 2:
                self.state = 133
                self.attrsInit()
                pass


            self.state = 136
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memIds(self):
            return self.getTypedRuleContext(D96Parser.MemIdsContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typeDecl(self):
            return self.getTypedRuleContext(D96Parser.TypeDeclContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attrs




    def attrs(self):

        localctx = D96Parser.AttrsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attrs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.memIds()
            self.state = 139
            self.match(D96Parser.COLON)
            self.state = 140
            self.typeDecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemIdsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memId(self):
            return self.getTypedRuleContext(D96Parser.MemIdContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def memIds(self):
            return self.getTypedRuleContext(D96Parser.MemIdsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_memIds




    def memIds(self):

        localctx = D96Parser.MemIdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_memIds)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.memId()
                self.state = 143
                self.match(D96Parser.COMMA)
                self.state = 144
                self.memIds()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.memId()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrsInitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memId(self):
            return self.getTypedRuleContext(D96Parser.MemIdContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def attrsInit(self):
            return self.getTypedRuleContext(D96Parser.AttrsInitContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typeDecl(self):
            return self.getTypedRuleContext(D96Parser.TypeDeclContext,0)


        def ASSIGNOP(self):
            return self.getToken(D96Parser.ASSIGNOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attrsInit




    def attrsInit(self):

        localctx = D96Parser.AttrsInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attrsInit)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.memId()
                self.state = 150
                self.match(D96Parser.COMMA)
                self.state = 151
                self.attrsInit()
                self.state = 152
                self.match(D96Parser.COMMA)
                self.state = 153
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.memId()
                self.state = 156
                self.match(D96Parser.COLON)
                self.state = 157
                self.typeDecl()
                self.state = 158
                self.match(D96Parser.ASSIGNOP)
                self.state = 159
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memId(self):
            return self.getTypedRuleContext(D96Parser.MemIdContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def paramList(self):
            return self.getTypedRuleContext(D96Parser.ParamListContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def blockStat(self):
            return self.getTypedRuleContext(D96Parser.BlockStatContext,0)


        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_methodDecl




    def methodDecl(self):

        localctx = D96Parser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_methodDecl)
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.STATIC_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.memId()
                self.state = 164
                self.match(D96Parser.LP)
                self.state = 165
                self.paramList()
                self.state = 166
                self.match(D96Parser.RP)
                self.state = 167
                self.blockStat()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(D96Parser.CONSTRUCTOR)
                self.state = 170
                self.match(D96Parser.LP)
                self.state = 171
                self.paramList()
                self.state = 172
                self.match(D96Parser.RP)
                self.state = 173
                self.blockStat()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 175
                self.match(D96Parser.DESTRUCTOR)
                self.state = 176
                self.match(D96Parser.LP)
                self.state = 177
                self.match(D96Parser.RP)
                self.state = 178
                self.blockStat()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params(self):
            return self.getTypedRuleContext(D96Parser.ParamsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_paramList




    def paramList(self):

        localctx = D96Parser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramList)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.params()
                pass
            elif token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(D96Parser.ParamContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def params(self):
            return self.getTypedRuleContext(D96Parser.ParamsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_params




    def params(self):

        localctx = D96Parser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_params)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.param()
                self.state = 186
                self.match(D96Parser.SEMI)
                self.state = 187
                self.params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
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

        def ids(self):
            return self.getTypedRuleContext(D96Parser.IdsContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typeDecl(self):
            return self.getTypedRuleContext(D96Parser.TypeDeclContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param




    def param(self):

        localctx = D96Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.ids()
            self.state = 193
            self.match(D96Parser.COLON)
            self.state = 194
            self.typeDecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def statList(self):
            return self.getTypedRuleContext(D96Parser.StatListContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_blockStat




    def blockStat(self):

        localctx = D96Parser.BlockStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_blockStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(D96Parser.LCB)
            self.state = 197
            self.statList()
            self.state = 198
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self):
            return self.getTypedRuleContext(D96Parser.StatContext,0)


        def statList(self):
            return self.getTypedRuleContext(D96Parser.StatListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statList




    def statList(self):

        localctx = D96Parser.StatListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_statList)
        try:
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.IF, D96Parser.FOREACH, D96Parser.SELF, D96Parser.NEW, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.RETURN, D96Parser.ARRAY, D96Parser.NULL, D96Parser.LP, D96Parser.LCB, D96Parser.ID, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.stat()
                self.state = 201
                self.statList()
                pass
            elif token in [D96Parser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr1Context,i)


        def CONCAT(self):
            return self.getToken(D96Parser.CONCAT, 0)

        def STRCOMP(self):
            return self.getToken(D96Parser.STRCOMP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.expr1()
                self.state = 207
                _la = self._input.LA(1)
                if not(_la==D96Parser.CONCAT or _la==D96Parser.STRCOMP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 208
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr2Context,i)


        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

        def NE(self):
            return self.getToken(D96Parser.NE, 0)

        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def LT(self):
            return self.getToken(D96Parser.LT, 0)

        def GTE(self):
            return self.getToken(D96Parser.GTE, 0)

        def LTE(self):
            return self.getToken(D96Parser.LTE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr1




    def expr1(self):

        localctx = D96Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.expr2(0)
                self.state = 214
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQ) | (1 << D96Parser.NE) | (1 << D96Parser.LT) | (1 << D96Parser.LTE) | (1 << D96Parser.GT) | (1 << D96Parser.GTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 215
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(D96Parser.Expr2Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 223
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 224
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 225
                    self.expr3(0) 
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def ADDOP(self):
            return self.getToken(D96Parser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(D96Parser.SUBOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 239
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 234
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 235
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADDOP or _la==D96Parser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 236
                    self.expr4(0) 
                self.state = 241
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def MULOP(self):
            return self.getToken(D96Parser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(D96Parser.DIVOP, 0)

        def MODOP(self):
            return self.getToken(D96Parser.MODOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 250
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 245
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 246
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULOP) | (1 << D96Parser.DIVOP) | (1 << D96Parser.MODOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 247
                    self.expr5() 
                self.state = 252
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr5




    def expr5(self):

        localctx = D96Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr5)
        try:
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(D96Parser.NOT)
                self.state = 254
                self.expr5()
                pass
            elif token in [D96Parser.SELF, D96Parser.NEW, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SUBOP, D96Parser.LP, D96Parser.ID, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBOP(self):
            return self.getToken(D96Parser.SUBOP, 0)

        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr6




    def expr6(self):

        localctx = D96Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr6)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(D96Parser.SUBOP)
                self.state = 259
                self.expr6()
                pass
            elif token in [D96Parser.SELF, D96Parser.NEW, D96Parser.ARRAY, D96Parser.NULL, D96Parser.LP, D96Parser.ID, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.expr7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr7



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 266
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 267
                    self.match(D96Parser.LSB)
                    self.state = 268
                    self.expr()
                    self.state = 269
                    self.match(D96Parser.RSB) 
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def argList(self):
            return self.getTypedRuleContext(D96Parser.ArgListContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr8



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 289
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 279
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 280
                        self.match(D96Parser.DOT)
                        self.state = 281
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 282
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 283
                        self.match(D96Parser.DOT)
                        self.state = 284
                        self.match(D96Parser.ID)
                        self.state = 285
                        self.match(D96Parser.LP)
                        self.state = 286
                        self.argList()
                        self.state = 287
                        self.match(D96Parser.RP)
                        pass

             
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DBCOLON(self):
            return self.getToken(D96Parser.DBCOLON, 0)

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def argList(self):
            return self.getTypedRuleContext(D96Parser.ArgListContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr9




    def expr9(self):

        localctx = D96Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr9)
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(D96Parser.ID)
                self.state = 295
                self.match(D96Parser.DBCOLON)
                self.state = 296
                self.match(D96Parser.STATIC_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.match(D96Parser.ID)
                self.state = 298
                self.match(D96Parser.DBCOLON)
                self.state = 299
                self.match(D96Parser.STATIC_ID)
                self.state = 300
                self.match(D96Parser.LP)
                self.state = 301
                self.argList()
                self.state = 302
                self.match(D96Parser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 304
                self.expr10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def argList(self):
            return self.getTypedRuleContext(D96Parser.ArgListContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def operand(self):
            return self.getTypedRuleContext(D96Parser.OperandContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr10




    def expr10(self):

        localctx = D96Parser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr10)
        try:
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.match(D96Parser.NEW)
                self.state = 308
                self.match(D96Parser.ID)
                self.state = 309
                self.match(D96Parser.LP)
                self.state = 310
                self.argList()
                self.state = 311
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.SELF, D96Parser.ARRAY, D96Parser.NULL, D96Parser.LP, D96Parser.ID, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(D96Parser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

        def arrayLit(self):
            return self.getTypedRuleContext(D96Parser.ArrayLitContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_operand




    def operand(self):

        localctx = D96Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_operand)
        try:
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(D96Parser.LP)
                self.state = 317
                self.expr()
                self.state = 318
                self.match(D96Parser.RP)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 321
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 322
                self.match(D96Parser.NULL)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 323
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 324
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 325
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 8)
                self.state = 326
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 9)
                self.state = 327
                self.arrayLit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declStat(self):
            return self.getTypedRuleContext(D96Parser.DeclStatContext,0)


        def assignStat(self):
            return self.getTypedRuleContext(D96Parser.AssignStatContext,0)


        def ifStat(self):
            return self.getTypedRuleContext(D96Parser.IfStatContext,0)


        def forStat(self):
            return self.getTypedRuleContext(D96Parser.ForStatContext,0)


        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(D96Parser.MethodCallContext,0)


        def blockStat(self):
            return self.getTypedRuleContext(D96Parser.BlockStatContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stat




    def stat(self):

        localctx = D96Parser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stat)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.declStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.assignStat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 332
                self.ifStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 333
                self.forStat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 334
                self.match(D96Parser.BREAK)
                self.state = 335
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 336
                self.match(D96Parser.CONTINUE)
                self.state = 337
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 338
                self.match(D96Parser.RETURN)
                self.state = 339
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 340
                self.match(D96Parser.RETURN)
                self.state = 341
                self.expr()
                self.state = 342
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 344
                self.methodCall()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 345
                self.blockStat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclStatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(D96Parser.VarDeclContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_declStat




    def declStat(self):

        localctx = D96Parser.DeclStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_declStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.varDecl()
            self.state = 349
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def variables(self):
            return self.getTypedRuleContext(D96Parser.VariablesContext,0)


        def varsInit(self):
            return self.getTypedRuleContext(D96Parser.VarsInitContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_varDecl




    def varDecl(self):

        localctx = D96Parser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 352
                self.variables()
                pass

            elif la_ == 2:
                self.state = 353
                self.varsInit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ids(self):
            return self.getTypedRuleContext(D96Parser.IdsContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typeDecl(self):
            return self.getTypedRuleContext(D96Parser.TypeDeclContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variables




    def variables(self):

        localctx = D96Parser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_variables)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.ids()
            self.state = 357
            self.match(D96Parser.COLON)
            self.state = 358
            self.typeDecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def ids(self):
            return self.getTypedRuleContext(D96Parser.IdsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_ids




    def ids(self):

        localctx = D96Parser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_ids)
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.match(D96Parser.ID)
                self.state = 361
                self.match(D96Parser.COMMA)
                self.state = 362
                self.ids()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.match(D96Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsInitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def varsInit(self):
            return self.getTypedRuleContext(D96Parser.VarsInitContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typeDecl(self):
            return self.getTypedRuleContext(D96Parser.TypeDeclContext,0)


        def ASSIGNOP(self):
            return self.getToken(D96Parser.ASSIGNOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_varsInit




    def varsInit(self):

        localctx = D96Parser.VarsInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_varsInit)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.match(D96Parser.ID)
                self.state = 367
                self.match(D96Parser.COMMA)
                self.state = 368
                self.varsInit()
                self.state = 369
                self.match(D96Parser.COMMA)
                self.state = 370
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.match(D96Parser.ID)
                self.state = 373
                self.match(D96Parser.COLON)
                self.state = 374
                self.typeDecl()
                self.state = 375
                self.match(D96Parser.ASSIGNOP)
                self.state = 376
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalarVar(self):
            return self.getTypedRuleContext(D96Parser.ScalarVarContext,0)


        def ASSIGNOP(self):
            return self.getToken(D96Parser.ASSIGNOP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def indexExpr(self):
            return self.getTypedRuleContext(D96Parser.IndexExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assignStat




    def assignStat(self):

        localctx = D96Parser.AssignStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_assignStat)
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.scalarVar()
                self.state = 381
                self.match(D96Parser.ASSIGNOP)
                self.state = 382
                self.expr()
                self.state = 383
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.indexExpr()
                self.state = 386
                self.match(D96Parser.ASSIGNOP)
                self.state = 387
                self.expr()
                self.state = 388
                self.match(D96Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def blockStat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.BlockStatContext)
            else:
                return self.getTypedRuleContext(D96Parser.BlockStatContext,i)


        def elseifList(self):
            return self.getTypedRuleContext(D96Parser.ElseifListContext,0)


        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_ifStat




    def ifStat(self):

        localctx = D96Parser.IfStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_ifStat)
        try:
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.match(D96Parser.IF)
                self.state = 393
                self.match(D96Parser.LP)
                self.state = 394
                self.expr()
                self.state = 395
                self.match(D96Parser.RP)
                self.state = 396
                self.blockStat()
                self.state = 397
                self.elseifList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
                self.match(D96Parser.IF)
                self.state = 400
                self.match(D96Parser.LP)
                self.state = 401
                self.expr()
                self.state = 402
                self.match(D96Parser.RP)
                self.state = 403
                self.blockStat()
                self.state = 404
                self.elseifList()
                self.state = 405
                self.match(D96Parser.ELSE)
                self.state = 406
                self.blockStat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseifListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def blockStat(self):
            return self.getTypedRuleContext(D96Parser.BlockStatContext,0)


        def elseifList(self):
            return self.getTypedRuleContext(D96Parser.ElseifListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseifList




    def elseifList(self):

        localctx = D96Parser.ElseifListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_elseifList)
        try:
            self.state = 418
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                self.match(D96Parser.ELSEIF)
                self.state = 411
                self.match(D96Parser.LP)
                self.state = 412
                self.expr()
                self.state = 413
                self.match(D96Parser.RP)
                self.state = 414
                self.blockStat()
                self.state = 415
                self.elseifList()
                pass
            elif token in [D96Parser.VAL, D96Parser.VAR, D96Parser.IF, D96Parser.ELSE, D96Parser.FOREACH, D96Parser.SELF, D96Parser.NEW, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.RETURN, D96Parser.ARRAY, D96Parser.NULL, D96Parser.LP, D96Parser.LCB, D96Parser.RCB, D96Parser.ID, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def scalarVar(self):
            return self.getTypedRuleContext(D96Parser.ScalarVarContext,0)


        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def DOTDOT(self):
            return self.getToken(D96Parser.DOTDOT, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def blockStat(self):
            return self.getTypedRuleContext(D96Parser.BlockStatContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_forStat




    def forStat(self):

        localctx = D96Parser.ForStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_forStat)
        try:
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.match(D96Parser.FOREACH)
                self.state = 421
                self.match(D96Parser.LP)
                self.state = 422
                self.scalarVar()
                self.state = 423
                self.match(D96Parser.IN)
                self.state = 424
                self.expr()
                self.state = 425
                self.match(D96Parser.DOTDOT)
                self.state = 426
                self.expr()
                self.state = 427
                self.match(D96Parser.RP)
                self.state = 428
                self.blockStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.match(D96Parser.FOREACH)
                self.state = 431
                self.match(D96Parser.LP)
                self.state = 432
                self.scalarVar()
                self.state = 433
                self.match(D96Parser.IN)
                self.state = 434
                self.expr()
                self.state = 435
                self.match(D96Parser.DOTDOT)
                self.state = 436
                self.expr()
                self.state = 437
                self.match(D96Parser.BY)
                self.state = 438
                self.expr()
                self.state = 439
                self.match(D96Parser.RP)
                self.state = 440
                self.blockStat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def argList(self):
            return self.getTypedRuleContext(D96Parser.ArgListContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def DBCOLON(self):
            return self.getToken(D96Parser.DBCOLON, 0)

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_methodCall




    def methodCall(self):

        localctx = D96Parser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_methodCall)
        try:
            self.state = 460
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.expr8(0)
                self.state = 445
                self.match(D96Parser.DOT)
                self.state = 446
                self.match(D96Parser.ID)
                self.state = 447
                self.match(D96Parser.LP)
                self.state = 448
                self.argList()
                self.state = 449
                self.match(D96Parser.RP)
                self.state = 450
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                self.match(D96Parser.ID)
                self.state = 453
                self.match(D96Parser.DBCOLON)
                self.state = 454
                self.match(D96Parser.STATIC_ID)
                self.state = 455
                self.match(D96Parser.LP)
                self.state = 456
                self.argList()
                self.state = 457
                self.match(D96Parser.RP)
                self.state = 458
                self.match(D96Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarVarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def DBCOLON(self):
            return self.getToken(D96Parser.DBCOLON, 0)

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_scalarVar




    def scalarVar(self):

        localctx = D96Parser.ScalarVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_scalarVar)
        try:
            self.state = 470
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.expr8(0)
                self.state = 464
                self.match(D96Parser.DOT)
                self.state = 465
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 467
                self.match(D96Parser.ID)
                self.state = 468
                self.match(D96Parser.DBCOLON)
                self.state = 469
                self.match(D96Parser.STATIC_ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_indexExpr




    def indexExpr(self):

        localctx = D96Parser.IndexExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_indexExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.expr7(0)

            self.state = 473
            self.match(D96Parser.LSB)
            self.state = 474
            self.expr()
            self.state = 475
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(D96Parser.PrimitiveTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(D96Parser.ArrayTypeContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_typeDecl




    def typeDecl(self):

        localctx = D96Parser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_typeDecl)
        try:
            self.state = 480
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.STRINGTYPE, D96Parser.BOOLTYPE, D96Parser.INTTYPE, D96Parser.FLOATTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.primitiveType()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.arrayType()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 479
                self.match(D96Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def arrayType(self):
            return self.getTypedRuleContext(D96Parser.ArrayTypeContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def primitiveType(self):
            return self.getTypedRuleContext(D96Parser.PrimitiveTypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arrayType




    def arrayType(self):

        localctx = D96Parser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_arrayType)
        try:
            self.state = 498
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.match(D96Parser.ARRAY)
                self.state = 483
                self.match(D96Parser.LSB)
                self.state = 484
                self.arrayType()
                self.state = 485
                self.match(D96Parser.COMMA)
                self.state = 486
                if not self.getCurrentToken().text not in self.ZEROLIT_ARR:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self.getCurrentToken().text not in self.ZEROLIT_ARR")
                self.state = 487
                self.match(D96Parser.INTLIT)
                self.state = 488
                self.match(D96Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 490
                self.match(D96Parser.ARRAY)
                self.state = 491
                self.match(D96Parser.LSB)
                self.state = 492
                self.primitiveType()
                self.state = 493
                self.match(D96Parser.COMMA)
                self.state = 494
                if not self.getCurrentToken().text not in self.ZEROLIT_ARR:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self.getCurrentToken().text not in self.ZEROLIT_ARR")
                self.state = 495
                self.match(D96Parser.INTLIT)
                self.state = 496
                self.match(D96Parser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLTYPE(self):
            return self.getToken(D96Parser.BOOLTYPE, 0)

        def INTTYPE(self):
            return self.getToken(D96Parser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(D96Parser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(D96Parser.STRINGTYPE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitiveType




    def primitiveType(self):

        localctx = D96Parser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.STRINGTYPE) | (1 << D96Parser.BOOLTYPE) | (1 << D96Parser.INTTYPE) | (1 << D96Parser.FLOATTYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def exprList(self):
            return self.getTypedRuleContext(D96Parser.ExprListContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arrayLit




    def arrayLit(self):

        localctx = D96Parser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self.match(D96Parser.ARRAY)
            self.state = 503
            self.match(D96Parser.LP)
            self.state = 504
            self.exprList()
            self.state = 505
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprs(self):
            return self.getTypedRuleContext(D96Parser.ExprsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exprList




    def exprList(self):

        localctx = D96Parser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_exprList)
        try:
            self.state = 509
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SELF, D96Parser.NEW, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SUBOP, D96Parser.NOT, D96Parser.LP, D96Parser.ID, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.exprs()
                pass
            elif token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def exprs(self):
            return self.getTypedRuleContext(D96Parser.ExprsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exprs




    def exprs(self):

        localctx = D96Parser.ExprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_exprs)
        try:
            self.state = 516
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.expr()
                self.state = 512
                self.match(D96Parser.COMMA)
                self.state = 513
                self.exprs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprs(self):
            return self.getTypedRuleContext(D96Parser.ExprsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_argList




    def argList(self):

        localctx = D96Parser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_argList)
        try:
            self.state = 520
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SELF, D96Parser.NEW, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SUBOP, D96Parser.NOT, D96Parser.LP, D96Parser.ID, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.exprs()
                pass
            elif token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemIdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_memId




    def memId(self):

        localctx = D96Parser.MemIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_memId)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.STATIC_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.expr2_sempred
        self._predicates[18] = self.expr3_sempred
        self._predicates[19] = self.expr4_sempred
        self._predicates[22] = self.expr7_sempred
        self._predicates[23] = self.expr8_sempred
        self._predicates[41] = self.arrayType_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def arrayType_sempred(self, localctx:ArrayTypeContext, predIndex:int):
            if predIndex == 6:
                return self.getCurrentToken().text not in self.ZEROLIT_ARR
         

            if predIndex == 7:
                return self.getCurrentToken().text not in self.ZEROLIT_ARR
         




