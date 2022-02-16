// Generated from d:\1_University\HK212\prin_prog_lang\LAB\4_ast\antlr-gui\BKIT.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BKITParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LET=1, CONST=2, FUNCTION=3, SEMI=4, COLON=5, COMMA=6, LR=7, RR=8, EQ=9, 
		INT=10, FLOAT=11, BOOLEAN=12, INTLIT=13, FLOATLIT=14, BOOLEANLIT=15, ID=16, 
		WS=17;
	public static final int
		RULE_program = 0, RULE_cseltype = 1, RULE_decl = 2, RULE_decltail = 3, 
		RULE_vardecl = 4, RULE_single_vardecls = 5, RULE_single_vardecl = 6, RULE_single_vardecltail = 7, 
		RULE_constdecl = 8, RULE_single_constdecl = 9, RULE_expr = 10, RULE_funcdecl = 11, 
		RULE_paramlist = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "cseltype", "decl", "decltail", "vardecl", "single_vardecls", 
			"single_vardecl", "single_vardecltail", "constdecl", "single_constdecl", 
			"expr", "funcdecl", "paramlist"
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

	@Override
	public String getGrammarFileName() { return "BKIT.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BKITParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(BKITParser.EOF, 0); }
		public List<DeclContext> decl() {
			return getRuleContexts(DeclContext.class);
		}
		public DeclContext decl(int i) {
			return getRuleContext(DeclContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(26);
				decl();
				}
				}
				setState(29); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LET) | (1L << CONST) | (1L << FUNCTION))) != 0) );
			setState(31);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CseltypeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(BKITParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(BKITParser.FLOAT, 0); }
		public TerminalNode BOOLEAN() { return getToken(BKITParser.BOOLEAN, 0); }
		public CseltypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cseltype; }
	}

	public final CseltypeContext cseltype() throws RecognitionException {
		CseltypeContext _localctx = new CseltypeContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_cseltype);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << FLOAT) | (1L << BOOLEAN))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclContext extends ParserRuleContext {
		public VardeclContext vardecl() {
			return getRuleContext(VardeclContext.class,0);
		}
		public DecltailContext decltail() {
			return getRuleContext(DecltailContext.class,0);
		}
		public ConstdeclContext constdecl() {
			return getRuleContext(ConstdeclContext.class,0);
		}
		public FuncdeclContext funcdecl() {
			return getRuleContext(FuncdeclContext.class,0);
		}
		public DeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decl; }
	}

	public final DeclContext decl() throws RecognitionException {
		DeclContext _localctx = new DeclContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_decl);
		try {
			setState(44);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LET:
				enterOuterAlt(_localctx, 1);
				{
				setState(35);
				vardecl();
				setState(36);
				decltail();
				}
				break;
			case CONST:
				enterOuterAlt(_localctx, 2);
				{
				setState(38);
				constdecl();
				setState(39);
				decltail();
				}
				break;
			case FUNCTION:
				enterOuterAlt(_localctx, 3);
				{
				setState(41);
				funcdecl();
				setState(42);
				decltail();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DecltailContext extends ParserRuleContext {
		public VardeclContext vardecl() {
			return getRuleContext(VardeclContext.class,0);
		}
		public DecltailContext decltail() {
			return getRuleContext(DecltailContext.class,0);
		}
		public ConstdeclContext constdecl() {
			return getRuleContext(ConstdeclContext.class,0);
		}
		public FuncdeclContext funcdecl() {
			return getRuleContext(FuncdeclContext.class,0);
		}
		public DecltailContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decltail; }
	}

	public final DecltailContext decltail() throws RecognitionException {
		DecltailContext _localctx = new DecltailContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_decltail);
		try {
			setState(56);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(46);
				vardecl();
				setState(47);
				decltail();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(49);
				constdecl();
				setState(50);
				decltail();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(52);
				funcdecl();
				setState(53);
				decltail();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VardeclContext extends ParserRuleContext {
		public TerminalNode LET() { return getToken(BKITParser.LET, 0); }
		public Single_vardeclsContext single_vardecls() {
			return getRuleContext(Single_vardeclsContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public VardeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardecl; }
	}

	public final VardeclContext vardecl() throws RecognitionException {
		VardeclContext _localctx = new VardeclContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_vardecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			match(LET);
			setState(59);
			single_vardecls();
			setState(60);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Single_vardeclsContext extends ParserRuleContext {
		public Single_vardeclContext single_vardecl() {
			return getRuleContext(Single_vardeclContext.class,0);
		}
		public Single_vardecltailContext single_vardecltail() {
			return getRuleContext(Single_vardecltailContext.class,0);
		}
		public Single_vardeclsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_single_vardecls; }
	}

	public final Single_vardeclsContext single_vardecls() throws RecognitionException {
		Single_vardeclsContext _localctx = new Single_vardeclsContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_single_vardecls);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			single_vardecl();
			setState(63);
			single_vardecltail();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Single_vardeclContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode COLON() { return getToken(BKITParser.COLON, 0); }
		public CseltypeContext cseltype() {
			return getRuleContext(CseltypeContext.class,0);
		}
		public Single_vardeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_single_vardecl; }
	}

	public final Single_vardeclContext single_vardecl() throws RecognitionException {
		Single_vardeclContext _localctx = new Single_vardeclContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_single_vardecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(65);
			match(ID);
			setState(66);
			match(COLON);
			setState(67);
			cseltype();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Single_vardecltailContext extends ParserRuleContext {
		public TerminalNode COMMA() { return getToken(BKITParser.COMMA, 0); }
		public Single_vardeclContext single_vardecl() {
			return getRuleContext(Single_vardeclContext.class,0);
		}
		public Single_vardecltailContext single_vardecltail() {
			return getRuleContext(Single_vardecltailContext.class,0);
		}
		public Single_vardecltailContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_single_vardecltail; }
	}

	public final Single_vardecltailContext single_vardecltail() throws RecognitionException {
		Single_vardecltailContext _localctx = new Single_vardecltailContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_single_vardecltail);
		try {
			setState(74);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(69);
				match(COMMA);
				setState(70);
				single_vardecl();
				setState(71);
				single_vardecltail();
				}
				break;
			case SEMI:
			case RR:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConstdeclContext extends ParserRuleContext {
		public TerminalNode CONST() { return getToken(BKITParser.CONST, 0); }
		public Single_constdeclContext single_constdecl() {
			return getRuleContext(Single_constdeclContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public ConstdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constdecl; }
	}

	public final ConstdeclContext constdecl() throws RecognitionException {
		ConstdeclContext _localctx = new ConstdeclContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_constdecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			match(CONST);
			setState(77);
			single_constdecl();
			setState(78);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Single_constdeclContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode COLON() { return getToken(BKITParser.COLON, 0); }
		public CseltypeContext cseltype() {
			return getRuleContext(CseltypeContext.class,0);
		}
		public TerminalNode EQ() { return getToken(BKITParser.EQ, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Single_constdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_single_constdecl; }
	}

	public final Single_constdeclContext single_constdecl() throws RecognitionException {
		Single_constdeclContext _localctx = new Single_constdeclContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_single_constdecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			match(ID);
			setState(81);
			match(COLON);
			setState(82);
			cseltype();
			setState(83);
			match(EQ);
			setState(84);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public TerminalNode INTLIT() { return getToken(BKITParser.INTLIT, 0); }
		public TerminalNode FLOATLIT() { return getToken(BKITParser.FLOATLIT, 0); }
		public TerminalNode BOOLEANLIT() { return getToken(BKITParser.BOOLEANLIT, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTLIT) | (1L << FLOATLIT) | (1L << BOOLEANLIT))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncdeclContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(BKITParser.FUNCTION, 0); }
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode LR() { return getToken(BKITParser.LR, 0); }
		public ParamlistContext paramlist() {
			return getRuleContext(ParamlistContext.class,0);
		}
		public TerminalNode RR() { return getToken(BKITParser.RR, 0); }
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public FuncdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcdecl; }
	}

	public final FuncdeclContext funcdecl() throws RecognitionException {
		FuncdeclContext _localctx = new FuncdeclContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_funcdecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			match(FUNCTION);
			setState(89);
			match(ID);
			setState(90);
			match(LR);
			setState(91);
			paramlist();
			setState(92);
			match(RR);
			setState(93);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamlistContext extends ParserRuleContext {
		public Single_vardeclsContext single_vardecls() {
			return getRuleContext(Single_vardeclsContext.class,0);
		}
		public ParamlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramlist; }
	}

	public final ParamlistContext paramlist() throws RecognitionException {
		ParamlistContext _localctx = new ParamlistContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_paramlist);
		try {
			setState(97);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(95);
				single_vardecls();
				}
				break;
			case RR:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23f\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\4\r\t\r\4\16\t\16\3\2\6\2\36\n\2\r\2\16\2\37\3\2\3\2\3\3\3\3\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4/\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\5\5;\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3"+
		"\t\3\t\3\t\3\t\3\t\5\tM\n\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3"+
		"\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\5\16d\n\16\3\16\2\2"+
		"\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2\4\3\2\f\16\3\2\17\21\2`\2\35\3"+
		"\2\2\2\4#\3\2\2\2\6.\3\2\2\2\b:\3\2\2\2\n<\3\2\2\2\f@\3\2\2\2\16C\3\2"+
		"\2\2\20L\3\2\2\2\22N\3\2\2\2\24R\3\2\2\2\26X\3\2\2\2\30Z\3\2\2\2\32c\3"+
		"\2\2\2\34\36\5\6\4\2\35\34\3\2\2\2\36\37\3\2\2\2\37\35\3\2\2\2\37 \3\2"+
		"\2\2 !\3\2\2\2!\"\7\2\2\3\"\3\3\2\2\2#$\t\2\2\2$\5\3\2\2\2%&\5\n\6\2&"+
		"\'\5\b\5\2\'/\3\2\2\2()\5\22\n\2)*\5\b\5\2*/\3\2\2\2+,\5\30\r\2,-\5\b"+
		"\5\2-/\3\2\2\2.%\3\2\2\2.(\3\2\2\2.+\3\2\2\2/\7\3\2\2\2\60\61\5\n\6\2"+
		"\61\62\5\b\5\2\62;\3\2\2\2\63\64\5\22\n\2\64\65\5\b\5\2\65;\3\2\2\2\66"+
		"\67\5\30\r\2\678\5\b\5\28;\3\2\2\29;\3\2\2\2:\60\3\2\2\2:\63\3\2\2\2:"+
		"\66\3\2\2\2:9\3\2\2\2;\t\3\2\2\2<=\7\3\2\2=>\5\f\7\2>?\7\6\2\2?\13\3\2"+
		"\2\2@A\5\16\b\2AB\5\20\t\2B\r\3\2\2\2CD\7\22\2\2DE\7\7\2\2EF\5\4\3\2F"+
		"\17\3\2\2\2GH\7\b\2\2HI\5\16\b\2IJ\5\20\t\2JM\3\2\2\2KM\3\2\2\2LG\3\2"+
		"\2\2LK\3\2\2\2M\21\3\2\2\2NO\7\4\2\2OP\5\24\13\2PQ\7\6\2\2Q\23\3\2\2\2"+
		"RS\7\22\2\2ST\7\7\2\2TU\5\4\3\2UV\7\13\2\2VW\5\26\f\2W\25\3\2\2\2XY\t"+
		"\3\2\2Y\27\3\2\2\2Z[\7\5\2\2[\\\7\22\2\2\\]\7\t\2\2]^\5\32\16\2^_\7\n"+
		"\2\2_`\7\6\2\2`\31\3\2\2\2ad\5\f\7\2bd\3\2\2\2ca\3\2\2\2cb\3\2\2\2d\33"+
		"\3\2\2\2\7\37.:Lc";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}