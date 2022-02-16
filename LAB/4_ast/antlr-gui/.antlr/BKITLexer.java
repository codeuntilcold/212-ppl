// Generated from d:\1_University\HK212\prin_prog_lang\LAB\4_ast\antlr-gui\BKIT.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BKITLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LET=1, CONST=2, FUNCTION=3, SEMI=4, COLON=5, COMMA=6, LR=7, RR=8, EQ=9, 
		INT=10, FLOAT=11, BOOLEAN=12, INTLIT=13, FLOATLIT=14, BOOLEANLIT=15, ID=16, 
		WS=17;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"LET", "CONST", "FUNCTION", "SEMI", "COLON", "COMMA", "LR", "RR", "EQ", 
			"INT", "FLOAT", "BOOLEAN", "INTLIT", "FLOATLIT", "BOOLEANLIT", "ID", 
			"WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Let'", "'Constant'", "'Function'", "';'", "':'", "','", "'('", 
			"')'", "'='", "'Int'", "'Float'", "'Boolean'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LET", "CONST", "FUNCTION", "SEMI", "COLON", "COMMA", "LR", "RR", 
			"EQ", "INT", "FLOAT", "BOOLEAN", "INTLIT", "FLOATLIT", "BOOLEANLIT", 
			"ID", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public BKITLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "BKIT.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23\u0080\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3"+
		"\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\3\r\3\16\6\16[\n\16\r\16\16\16\\\3\17\6\17`\n\17\r\17\16\17a\3\17"+
		"\3\17\6\17f\n\17\r\17\16\17g\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\5\20s\n\20\3\21\6\21v\n\21\r\21\16\21w\3\22\6\22{\n\22\r\22\16\22"+
		"|\3\22\3\22\2\2\23\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r"+
		"\31\16\33\17\35\20\37\21!\22#\23\3\2\5\3\2\62;\4\2C\\c|\5\2\13\f\16\17"+
		"\"\"\2\u0085\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2"+
		"\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2"+
		"\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2"+
		"\2\2\2#\3\2\2\2\3%\3\2\2\2\5)\3\2\2\2\7\62\3\2\2\2\t;\3\2\2\2\13=\3\2"+
		"\2\2\r?\3\2\2\2\17A\3\2\2\2\21C\3\2\2\2\23E\3\2\2\2\25G\3\2\2\2\27K\3"+
		"\2\2\2\31Q\3\2\2\2\33Z\3\2\2\2\35_\3\2\2\2\37r\3\2\2\2!u\3\2\2\2#z\3\2"+
		"\2\2%&\7N\2\2&\'\7g\2\2\'(\7v\2\2(\4\3\2\2\2)*\7E\2\2*+\7q\2\2+,\7p\2"+
		"\2,-\7u\2\2-.\7v\2\2./\7c\2\2/\60\7p\2\2\60\61\7v\2\2\61\6\3\2\2\2\62"+
		"\63\7H\2\2\63\64\7w\2\2\64\65\7p\2\2\65\66\7e\2\2\66\67\7v\2\2\678\7k"+
		"\2\289\7q\2\29:\7p\2\2:\b\3\2\2\2;<\7=\2\2<\n\3\2\2\2=>\7<\2\2>\f\3\2"+
		"\2\2?@\7.\2\2@\16\3\2\2\2AB\7*\2\2B\20\3\2\2\2CD\7+\2\2D\22\3\2\2\2EF"+
		"\7?\2\2F\24\3\2\2\2GH\7K\2\2HI\7p\2\2IJ\7v\2\2J\26\3\2\2\2KL\7H\2\2LM"+
		"\7n\2\2MN\7q\2\2NO\7c\2\2OP\7v\2\2P\30\3\2\2\2QR\7D\2\2RS\7q\2\2ST\7q"+
		"\2\2TU\7n\2\2UV\7g\2\2VW\7c\2\2WX\7p\2\2X\32\3\2\2\2Y[\t\2\2\2ZY\3\2\2"+
		"\2[\\\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]\34\3\2\2\2^`\t\2\2\2_^\3\2\2\2`a"+
		"\3\2\2\2a_\3\2\2\2ab\3\2\2\2bc\3\2\2\2ce\7\60\2\2df\t\2\2\2ed\3\2\2\2"+
		"fg\3\2\2\2ge\3\2\2\2gh\3\2\2\2h\36\3\2\2\2ij\7V\2\2jk\7t\2\2kl\7w\2\2"+
		"ls\7g\2\2mn\7H\2\2no\7c\2\2op\7n\2\2pq\7u\2\2qs\7g\2\2ri\3\2\2\2rm\3\2"+
		"\2\2s \3\2\2\2tv\t\3\2\2ut\3\2\2\2vw\3\2\2\2wu\3\2\2\2wx\3\2\2\2x\"\3"+
		"\2\2\2y{\t\4\2\2zy\3\2\2\2{|\3\2\2\2|z\3\2\2\2|}\3\2\2\2}~\3\2\2\2~\177"+
		"\b\22\2\2\177$\3\2\2\2\t\2\\agrw|\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}