# Generated from d:\1_University\HK212\prin_prog_lang\_EXTEND\initial\initial\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01da\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\5\30\u010f\n\30\3\31\3\31\3\32\3\32\3\33\3")
        buf.write("\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3")
        buf.write("!\3\"\3\"\3#\3#\3#\3#\5#\u0129\n#\3$\3$\5$\u012d\n$\3")
        buf.write("%\3%\5%\u0131\n%\3&\3&\5&\u0135\n&\3\'\3\'\3\'\3\'\5\'")
        buf.write("\u013b\n\'\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3")
        buf.write(".\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\38\38\39\39\39\3:\3:\7:\u016a\n:\f:\16:\u016d\13:\3;")
        buf.write("\6;\u0170\n;\r;\16;\u0171\3<\3<\3<\3<\3<\3<\5<\u017a\n")
        buf.write("<\3<\3<\5<\u017e\n<\3<\3<\3<\5<\u0183\n<\3<\5<\u0186\n")
        buf.write("<\3=\3=\7=\u018a\n=\f=\16=\u018d\13=\3=\3=\3>\3>\7>\u0193")
        buf.write("\n>\f>\16>\u0196\13>\3>\3>\3>\3>\7>\u019c\n>\f>\16>\u019f")
        buf.write("\13>\3>\3>\5>\u01a3\n>\3?\3?\7?\u01a7\n?\f?\16?\u01aa")
        buf.write("\13?\3?\3?\3?\3@\3@\5@\u01b1\n@\3A\3A\3A\3B\3B\3B\5B\u01b9")
        buf.write("\nB\3C\6C\u01bc\nC\rC\16C\u01bd\3C\3C\3D\3D\3D\3D\7D\u01c6")
        buf.write("\nD\fD\16D\u01c9\13D\3D\3D\3D\3D\7D\u01cf\nD\fD\16D\u01d2")
        buf.write("\13D\5D\u01d4\nD\3D\3D\3E\3E\3E\3\u01c7\2F\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[")
        buf.write("/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177")
        buf.write("\2\u0081\2\u0083\2\u0085A\u0087B\u0089C\3\2\13\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4\2--//\5\2\f\f$$")
        buf.write("^^\t\2$$^^ddhhppttvv\5\2\13\f\16\17\"\"\4\2\f\f\17\17")
        buf.write("\2\u01f3\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\3\u008b\3\2\2\2\5\u0092\3\2\2")
        buf.write("\2\7\u009b\3\2\2\2\t\u00a1\3\2\2\2\13\u00a4\3\2\2\2\r")
        buf.write("\u00a7\3\2\2\2\17\u00ae\3\2\2\2\21\u00b2\3\2\2\2\23\u00b8")
        buf.write("\3\2\2\2\25\u00bd\3\2\2\2\27\u00c5\3\2\2\2\31\u00cc\3")
        buf.write("\2\2\2\33\u00d2\3\2\2\2\35\u00da\3\2\2\2\37\u00e1\3\2")
        buf.write("\2\2!\u00e7\3\2\2\2#\u00eb\3\2\2\2%\u00f0\3\2\2\2\'\u00f4")
        buf.write("\3\2\2\2)\u00f7\3\2\2\2+\u00fc\3\2\2\2-\u0101\3\2\2\2")
        buf.write("/\u010e\3\2\2\2\61\u0110\3\2\2\2\63\u0112\3\2\2\2\65\u0114")
        buf.write("\3\2\2\2\67\u0116\3\2\2\29\u0118\3\2\2\2;\u011a\3\2\2")
        buf.write("\2=\u011c\3\2\2\2?\u011e\3\2\2\2A\u0120\3\2\2\2C\u0122")
        buf.write("\3\2\2\2E\u0128\3\2\2\2G\u012c\3\2\2\2I\u0130\3\2\2\2")
        buf.write("K\u0134\3\2\2\2M\u013a\3\2\2\2O\u013c\3\2\2\2Q\u013e\3")
        buf.write("\2\2\2S\u0140\3\2\2\2U\u0142\3\2\2\2W\u0145\3\2\2\2Y\u0147")
        buf.write("\3\2\2\2[\u0149\3\2\2\2]\u014c\3\2\2\2_\u014f\3\2\2\2")
        buf.write("a\u0151\3\2\2\2c\u0153\3\2\2\2e\u0155\3\2\2\2g\u0157\3")
        buf.write("\2\2\2i\u015a\3\2\2\2k\u015c\3\2\2\2m\u015f\3\2\2\2o\u0162")
        buf.write("\3\2\2\2q\u0164\3\2\2\2s\u0167\3\2\2\2u\u016f\3\2\2\2")
        buf.write("w\u0173\3\2\2\2y\u0187\3\2\2\2{\u01a2\3\2\2\2}\u01a4\3")
        buf.write("\2\2\2\177\u01b0\3\2\2\2\u0081\u01b2\3\2\2\2\u0083\u01b8")
        buf.write("\3\2\2\2\u0085\u01bb\3\2\2\2\u0087\u01d3\3\2\2\2\u0089")
        buf.write("\u01d7\3\2\2\2\u008b\u008c\7t\2\2\u008c\u008d\7g\2\2\u008d")
        buf.write("\u008e\7v\2\2\u008e\u008f\7w\2\2\u008f\u0090\7t\2\2\u0090")
        buf.write("\u0091\7p\2\2\u0091\4\3\2\2\2\u0092\u0093\7e\2\2\u0093")
        buf.write("\u0094\7q\2\2\u0094\u0095\7p\2\2\u0095\u0096\7v\2\2\u0096")
        buf.write("\u0097\7k\2\2\u0097\u0098\7p\2\2\u0098\u0099\7w\2\2\u0099")
        buf.write("\u009a\7g\2\2\u009a\6\3\2\2\2\u009b\u009c\7d\2\2\u009c")
        buf.write("\u009d\7t\2\2\u009d\u009e\7g\2\2\u009e\u009f\7c\2\2\u009f")
        buf.write("\u00a0\7m\2\2\u00a0\b\3\2\2\2\u00a1\u00a2\7f\2\2\u00a2")
        buf.write("\u00a3\7q\2\2\u00a3\n\3\2\2\2\u00a4\u00a5\7v\2\2\u00a5")
        buf.write("\u00a6\7q\2\2\u00a6\f\3\2\2\2\u00a7\u00a8\7f\2\2\u00a8")
        buf.write("\u00a9\7q\2\2\u00a9\u00aa\7y\2\2\u00aa\u00ab\7p\2\2\u00ab")
        buf.write("\u00ac\7v\2\2\u00ac\u00ad\7q\2\2\u00ad\16\3\2\2\2\u00ae")
        buf.write("\u00af\7k\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1\7v\2\2\u00b1")
        buf.write("\20\3\2\2\2\u00b2\u00b3\7h\2\2\u00b3\u00b4\7n\2\2\u00b4")
        buf.write("\u00b5\7q\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7\7v\2\2\u00b7")
        buf.write("\22\3\2\2\2\u00b8\u00b9\7x\2\2\u00b9\u00ba\7q\2\2\u00ba")
        buf.write("\u00bb\7k\2\2\u00bb\u00bc\7f\2\2\u00bc\24\3\2\2\2\u00bd")
        buf.write("\u00be\7d\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7q\2\2\u00c0")
        buf.write("\u00c1\7n\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3\7c\2\2\u00c3")
        buf.write("\u00c4\7p\2\2\u00c4\26\3\2\2\2\u00c5\u00c6\7u\2\2\u00c6")
        buf.write("\u00c7\7v\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7k\2\2\u00c9")
        buf.write("\u00ca\7p\2\2\u00ca\u00cb\7i\2\2\u00cb\30\3\2\2\2\u00cc")
        buf.write("\u00cd\7e\2\2\u00cd\u00ce\7n\2\2\u00ce\u00cf\7c\2\2\u00cf")
        buf.write("\u00d0\7u\2\2\u00d0\u00d1\7u\2\2\u00d1\32\3\2\2\2\u00d2")
        buf.write("\u00d3\7g\2\2\u00d3\u00d4\7z\2\2\u00d4\u00d5\7v\2\2\u00d5")
        buf.write("\u00d6\7g\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8\7f\2\2\u00d8")
        buf.write("\u00d9\7u\2\2\u00d9\34\3\2\2\2\u00da\u00db\7u\2\2\u00db")
        buf.write("\u00dc\7v\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de\7v\2\2\u00de")
        buf.write("\u00df\7k\2\2\u00df\u00e0\7e\2\2\u00e0\36\3\2\2\2\u00e1")
        buf.write("\u00e2\7h\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4\7p\2\2\u00e4")
        buf.write("\u00e5\7c\2\2\u00e5\u00e6\7n\2\2\u00e6 \3\2\2\2\u00e7")
        buf.write("\u00e8\7p\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea\7y\2\2\u00ea")
        buf.write("\"\3\2\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed\7j\2\2\u00ed")
        buf.write("\u00ee\7k\2\2\u00ee\u00ef\7u\2\2\u00ef$\3\2\2\2\u00f0")
        buf.write("\u00f1\7p\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3\7n\2\2\u00f3")
        buf.write("&\3\2\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6\7h\2\2\u00f6")
        buf.write("(\3\2\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9\7j\2\2\u00f9")
        buf.write("\u00fa\7g\2\2\u00fa\u00fb\7p\2\2\u00fb*\3\2\2\2\u00fc")
        buf.write("\u00fd\7g\2\2\u00fd\u00fe\7n\2\2\u00fe\u00ff\7u\2\2\u00ff")
        buf.write("\u0100\7g\2\2\u0100,\3\2\2\2\u0101\u0102\7h\2\2\u0102")
        buf.write("\u0103\7q\2\2\u0103\u0104\7t\2\2\u0104.\3\2\2\2\u0105")
        buf.write("\u0106\7v\2\2\u0106\u0107\7t\2\2\u0107\u0108\7w\2\2\u0108")
        buf.write("\u010f\7g\2\2\u0109\u010a\7h\2\2\u010a\u010b\7c\2\2\u010b")
        buf.write("\u010c\7n\2\2\u010c\u010d\7u\2\2\u010d\u010f\7g\2\2\u010e")
        buf.write("\u0105\3\2\2\2\u010e\u0109\3\2\2\2\u010f\60\3\2\2\2\u0110")
        buf.write("\u0111\7=\2\2\u0111\62\3\2\2\2\u0112\u0113\7<\2\2\u0113")
        buf.write("\64\3\2\2\2\u0114\u0115\7\60\2\2\u0115\66\3\2\2\2\u0116")
        buf.write("\u0117\7.\2\2\u01178\3\2\2\2\u0118\u0119\7]\2\2\u0119")
        buf.write(":\3\2\2\2\u011a\u011b\7_\2\2\u011b<\3\2\2\2\u011c\u011d")
        buf.write("\7*\2\2\u011d>\3\2\2\2\u011e\u011f\7+\2\2\u011f@\3\2\2")
        buf.write("\2\u0120\u0121\7}\2\2\u0121B\3\2\2\2\u0122\u0123\7\177")
        buf.write("\2\2\u0123D\3\2\2\2\u0124\u0129\5Y-\2\u0125\u0129\5i\65")
        buf.write("\2\u0126\u0129\5[.\2\u0127\u0129\5k\66\2\u0128\u0124\3")
        buf.write("\2\2\2\u0128\u0125\3\2\2\2\u0128\u0126\3\2\2\2\u0128\u0127")
        buf.write("\3\2\2\2\u0129F\3\2\2\2\u012a\u012d\5g\64\2\u012b\u012d")
        buf.write("\5U+\2\u012c\u012a\3\2\2\2\u012c\u012b\3\2\2\2\u012dH")
        buf.write("\3\2\2\2\u012e\u0131\5m\67\2\u012f\u0131\5]/\2\u0130\u012e")
        buf.write("\3\2\2\2\u0130\u012f\3\2\2\2\u0131J\3\2\2\2\u0132\u0135")
        buf.write("\5O(\2\u0133\u0135\5a\61\2\u0134\u0132\3\2\2\2\u0134\u0133")
        buf.write("\3\2\2\2\u0135L\3\2\2\2\u0136\u013b\5Q)\2\u0137\u013b")
        buf.write("\5S*\2\u0138\u013b\5c\62\2\u0139\u013b\5e\63\2\u013a\u0136")
        buf.write("\3\2\2\2\u013a\u0137\3\2\2\2\u013a\u0138\3\2\2\2\u013a")
        buf.write("\u0139\3\2\2\2\u013bN\3\2\2\2\u013c\u013d\7-\2\2\u013d")
        buf.write("P\3\2\2\2\u013e\u013f\7,\2\2\u013fR\3\2\2\2\u0140\u0141")
        buf.write("\7^\2\2\u0141T\3\2\2\2\u0142\u0143\7#\2\2\u0143\u0144")
        buf.write("\7?\2\2\u0144V\3\2\2\2\u0145\u0146\7?\2\2\u0146X\3\2\2")
        buf.write("\2\u0147\u0148\7>\2\2\u0148Z\3\2\2\2\u0149\u014a\7>\2")
        buf.write("\2\u014a\u014b\7?\2\2\u014b\\\3\2\2\2\u014c\u014d\7~\2")
        buf.write("\2\u014d\u014e\7~\2\2\u014e^\3\2\2\2\u014f\u0150\7#\2")
        buf.write("\2\u0150`\3\2\2\2\u0151\u0152\7/\2\2\u0152b\3\2\2\2\u0153")
        buf.write("\u0154\7\61\2\2\u0154d\3\2\2\2\u0155\u0156\7\'\2\2\u0156")
        buf.write("f\3\2\2\2\u0157\u0158\7?\2\2\u0158\u0159\7?\2\2\u0159")
        buf.write("h\3\2\2\2\u015a\u015b\7@\2\2\u015bj\3\2\2\2\u015c\u015d")
        buf.write("\7@\2\2\u015d\u015e\7?\2\2\u015el\3\2\2\2\u015f\u0160")
        buf.write("\7(\2\2\u0160\u0161\7(\2\2\u0161n\3\2\2\2\u0162\u0163")
        buf.write("\7`\2\2\u0163p\3\2\2\2\u0164\u0165\7<\2\2\u0165\u0166")
        buf.write("\7?\2\2\u0166r\3\2\2\2\u0167\u016b\t\2\2\2\u0168\u016a")
        buf.write("\t\3\2\2\u0169\u0168\3\2\2\2\u016a\u016d\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016ct\3\2\2\2\u016d")
        buf.write("\u016b\3\2\2\2\u016e\u0170\t\4\2\2\u016f\u016e\3\2\2\2")
        buf.write("\u0170\u0171\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172\3")
        buf.write("\2\2\2\u0172v\3\2\2\2\u0173\u0185\5u;\2\u0174\u0186\7")
        buf.write("\60\2\2\u0175\u0176\7\60\2\2\u0176\u0186\5u;\2\u0177\u0179")
        buf.write("\7\60\2\2\u0178\u017a\5u;\2\u0179\u0178\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017d\t\5\2\2")
        buf.write("\u017c\u017e\t\6\2\2\u017d\u017c\3\2\2\2\u017d\u017e\3")
        buf.write("\2\2\2\u017e\u017f\3\2\2\2\u017f\u0186\5u;\2\u0180\u0182")
        buf.write("\t\5\2\2\u0181\u0183\t\6\2\2\u0182\u0181\3\2\2\2\u0182")
        buf.write("\u0183\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0186\5u;\2\u0185")
        buf.write("\u0174\3\2\2\2\u0185\u0175\3\2\2\2\u0185\u0177\3\2\2\2")
        buf.write("\u0185\u0180\3\2\2\2\u0186x\3\2\2\2\u0187\u018b\7$\2\2")
        buf.write("\u0188\u018a\5\177@\2\u0189\u0188\3\2\2\2\u018a\u018d")
        buf.write("\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018c")
        buf.write("\u018e\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u018f\7$\2\2")
        buf.write("\u018fz\3\2\2\2\u0190\u0194\7$\2\2\u0191\u0193\5\177@")
        buf.write("\2\u0192\u0191\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0197\3\2\2\2\u0196")
        buf.write("\u0194\3\2\2\2\u0197\u0198\7\2\2\3\u0198\u01a3\b>\2\2")
        buf.write("\u0199\u019d\7$\2\2\u019a\u019c\5\177@\2\u019b\u019a\3")
        buf.write("\2\2\2\u019c\u019f\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e")
        buf.write("\3\2\2\2\u019e\u01a0\3\2\2\2\u019f\u019d\3\2\2\2\u01a0")
        buf.write("\u01a1\7\f\2\2\u01a1\u01a3\b>\3\2\u01a2\u0190\3\2\2\2")
        buf.write("\u01a2\u0199\3\2\2\2\u01a3|\3\2\2\2\u01a4\u01a8\7$\2\2")
        buf.write("\u01a5\u01a7\5\177@\2\u01a6\u01a5\3\2\2\2\u01a7\u01aa")
        buf.write("\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9")
        buf.write("\u01ab\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u01ac\5\u0083")
        buf.write("B\2\u01ac\u01ad\b?\4\2\u01ad~\3\2\2\2\u01ae\u01b1\n\7")
        buf.write("\2\2\u01af\u01b1\5\u0081A\2\u01b0\u01ae\3\2\2\2\u01b0")
        buf.write("\u01af\3\2\2\2\u01b1\u0080\3\2\2\2\u01b2\u01b3\7^\2\2")
        buf.write("\u01b3\u01b4\t\b\2\2\u01b4\u0082\3\2\2\2\u01b5\u01b6\7")
        buf.write("^\2\2\u01b6\u01b9\n\b\2\2\u01b7\u01b9\7^\2\2\u01b8\u01b5")
        buf.write("\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9\u0084\3\2\2\2\u01ba")
        buf.write("\u01bc\t\t\2\2\u01bb\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2")
        buf.write("\u01bd\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01bf\3")
        buf.write("\2\2\2\u01bf\u01c0\bC\5\2\u01c0\u0086\3\2\2\2\u01c1\u01c2")
        buf.write("\7\61\2\2\u01c2\u01c3\7,\2\2\u01c3\u01c7\3\2\2\2\u01c4")
        buf.write("\u01c6\13\2\2\2\u01c5\u01c4\3\2\2\2\u01c6\u01c9\3\2\2")
        buf.write("\2\u01c7\u01c8\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01ca")
        buf.write("\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca\u01cb\7,\2\2\u01cb")
        buf.write("\u01d4\7\61\2\2\u01cc\u01d0\7%\2\2\u01cd\u01cf\n\n\2\2")
        buf.write("\u01ce\u01cd\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3")
        buf.write("\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d0")
        buf.write("\3\2\2\2\u01d3\u01c1\3\2\2\2\u01d3\u01cc\3\2\2\2\u01d4")
        buf.write("\u01d5\3\2\2\2\u01d5\u01d6\bD\5\2\u01d6\u0088\3\2\2\2")
        buf.write("\u01d7\u01d8\13\2\2\2\u01d8\u01d9\bE\6\2\u01d9\u008a\3")
        buf.write("\2\2\2\32\2\u010e\u0128\u012c\u0130\u0134\u013a\u016b")
        buf.write("\u0171\u0179\u017d\u0182\u0185\u018b\u0194\u019d\u01a2")
        buf.write("\u01a8\u01b0\u01b8\u01bd\u01c7\u01d0\u01d3\7\3>\2\3>\3")
        buf.write("\3?\4\b\2\2\3E\5")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    RETURN = 1
    CONTINUE = 2
    BREAK = 3
    DO = 4
    TO = 5
    DOWNTO = 6
    INTTYPE = 7
    FLOATTYPE = 8
    VOIDTYPE = 9
    BOOLTYPE = 10
    STRINGTYPE = 11
    CLASS = 12
    EXTENDS = 13
    STATIC = 14
    FINAL = 15
    NEW = 16
    THIS = 17
    NIL = 18
    IF = 19
    THEN = 20
    ELSE = 21
    FOR = 22
    BOOLLIT = 23
    SEMI = 24
    COLON = 25
    DOT = 26
    COMMA = 27
    LSB = 28
    RSB = 29
    LB = 30
    RB = 31
    LP = 32
    RP = 33
    COMPAREOP = 34
    EQOP = 35
    LOGICOP = 36
    AMOP = 37
    MDOP = 38
    ADDOP = 39
    MULOP = 40
    DIVOP = 41
    NOTEQOP = 42
    INITOP = 43
    LESSTHANOP = 44
    LESSTHANEQOP = 45
    OROP = 46
    NOTOP = 47
    MINUSOP = 48
    FLOATDIVOP = 49
    MODULUSOP = 50
    EQUALOP = 51
    GREATERTHANOP = 52
    GREATERTHANOPEQ = 53
    ANDOP = 54
    CONCATOP = 55
    ASSIGNOP = 56
    ID = 57
    INTLIT = 58
    FLOATLIT = 59
    STRINGLIT = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62
    WS = 63
    COMMENT = 64
    ERROR_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'continue'", "'break'", "'do'", "'to'", "'downto'", 
            "'int'", "'float'", "'void'", "'boolean'", "'string'", "'class'", 
            "'extends'", "'static'", "'final'", "'new'", "'this'", "'nil'", 
            "'if'", "'then'", "'else'", "'for'", "';'", "':'", "'.'", "','", 
            "'['", "']'", "'('", "')'", "'{'", "'}'", "'+'", "'*'", "'\\'", 
            "'!='", "'='", "'<'", "'<='", "'||'", "'!'", "'-'", "'/'", "'%'", 
            "'=='", "'>'", "'>='", "'&&'", "'^'", "':='" ]

    symbolicNames = [ "<INVALID>",
            "RETURN", "CONTINUE", "BREAK", "DO", "TO", "DOWNTO", "INTTYPE", 
            "FLOATTYPE", "VOIDTYPE", "BOOLTYPE", "STRINGTYPE", "CLASS", 
            "EXTENDS", "STATIC", "FINAL", "NEW", "THIS", "NIL", "IF", "THEN", 
            "ELSE", "FOR", "BOOLLIT", "SEMI", "COLON", "DOT", "COMMA", "LSB", 
            "RSB", "LB", "RB", "LP", "RP", "COMPAREOP", "EQOP", "LOGICOP", 
            "AMOP", "MDOP", "ADDOP", "MULOP", "DIVOP", "NOTEQOP", "INITOP", 
            "LESSTHANOP", "LESSTHANEQOP", "OROP", "NOTOP", "MINUSOP", "FLOATDIVOP", 
            "MODULUSOP", "EQUALOP", "GREATERTHANOP", "GREATERTHANOPEQ", 
            "ANDOP", "CONCATOP", "ASSIGNOP", "ID", "INTLIT", "FLOATLIT", 
            "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS", "COMMENT", 
            "ERROR_CHAR" ]

    ruleNames = [ "RETURN", "CONTINUE", "BREAK", "DO", "TO", "DOWNTO", "INTTYPE", 
                  "FLOATTYPE", "VOIDTYPE", "BOOLTYPE", "STRINGTYPE", "CLASS", 
                  "EXTENDS", "STATIC", "FINAL", "NEW", "THIS", "NIL", "IF", 
                  "THEN", "ELSE", "FOR", "BOOLLIT", "SEMI", "COLON", "DOT", 
                  "COMMA", "LSB", "RSB", "LB", "RB", "LP", "RP", "COMPAREOP", 
                  "EQOP", "LOGICOP", "AMOP", "MDOP", "ADDOP", "MULOP", "DIVOP", 
                  "NOTEQOP", "INITOP", "LESSTHANOP", "LESSTHANEQOP", "OROP", 
                  "NOTOP", "MINUSOP", "FLOATDIVOP", "MODULUSOP", "EQUALOP", 
                  "GREATERTHANOP", "GREATERTHANOPEQ", "ANDOP", "CONCATOP", 
                  "ASSIGNOP", "ID", "INTLIT", "FLOATLIT", "STRINGLIT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", 
                  "WS", "COMMENT", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

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
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[60] = self.UNCLOSE_STRING_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             raise UncloseString(self.text) 
     

        if actionIndex == 1:
              raise UncloseString(self.text[:-1]) 
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             raise IllegalEscape(self.text) 
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise ErrorToken(self.text) 
     


