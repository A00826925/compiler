// Generated from c:/Users/YO/Documents/Python Projects/compiler/patito.g4 by ANTLR 4.13.1


from varfunctable import *
global funclist, quads
funclist = FuncTable()
quads = Cuadruplos()

global current_content, current_func, current_scope, current_type, current_var, various_vars, temporal_operator

current_var = ''
current_func = ''
current_type = ''
current_scope = 0
current_content = ''
various_vars = []
temporal_operator = ''


import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class patitoParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, Id=30, Cte_int=31, Cte_float=32, 
		Cte_string=33, WS=34;
	public static final int
		RULE_startRule = 0, RULE_programa = 1, RULE_vars = 2, RULE_type = 3, RULE_funcs = 4, 
		RULE_body = 5, RULE_statement = 6, RULE_assign = 7, RULE_expression = 8, 
		RULE_exp = 9, RULE_termino = 10, RULE_factor = 11, RULE_cte = 12, RULE_condition = 13, 
		RULE_cycle = 14, RULE_f_call = 15, RULE_print = 16;
	private static String[] makeRuleNames() {
		return new String[] {
			"startRule", "programa", "vars", "type", "funcs", "body", "statement", 
			"assign", "expression", "exp", "termino", "factor", "cte", "condition", 
			"cycle", "f_call", "print"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "';'", "'main'", "'end'", "'var'", "','", "':'", "'int'", 
			"'float'", "'void'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'='", 
			"'>'", "'<'", "'!='", "'+'", "'-'", "'*'", "'/'", "'if'", "'else'", "'while'", 
			"'do'", "'print'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, "Id", "Cte_int", "Cte_float", "Cte_string", 
			"WS"
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
	public String getGrammarFileName() { return "patito.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public patitoParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StartRuleContext extends ParserRuleContext {
		public ProgramaContext programa() {
			return getRuleContext(ProgramaContext.class,0);
		}
		public TerminalNode EOF() { return getToken(patitoParser.EOF, 0); }
		public StartRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_startRule; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).enterStartRule(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).exitStartRule(this);
		}
	}

	public final StartRuleContext startRule() throws RecognitionException {
		StartRuleContext _localctx = new StartRuleContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_startRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			programa();
			setState(35);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public Token Id;
		public TerminalNode Id() { return getToken(patitoParser.Id, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public VarsContext vars() {
			return getRuleContext(VarsContext.class,0);
		}
		public List<FuncsContext> funcs() {
			return getRuleContexts(FuncsContext.class);
		}
		public FuncsContext funcs(int i) {
			return getRuleContext(FuncsContext.class,i);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).enterPrograma(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).exitPrograma(this);
		}
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_programa);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(37);
			match(T__0);
			quads.quad_main_init()
			setState(39);
			((ProgramaContext)_localctx).Id = match(Id);
			global current_func, current_scope; current_func = (((ProgramaContext)_localctx).Id!=null?((ProgramaContext)_localctx).Id.getText():null); funclist; funclist.add_function((((ProgramaContext)_localctx).Id!=null?((ProgramaContext)_localctx).Id.getText():null))
			setState(41);
			match(T__1);
			{
			setState(43);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(42);
				vars();
				}
			}

			setState(48);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__9) {
				{
				{
				setState(45);
				funcs();
				}
				}
				setState(50);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(51);
			match(T__2);
			quads.quad_main_set()
			current_scope+=1; 
			current_func = "main";
			funclist.add_function(current_func)
			setState(54);
			body();
			current_scope-=1
			setState(56);
			match(T__3);
			funclist.print_all_functions(); quads.printQuads()
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

	@SuppressWarnings("CheckReturnValue")
	public static class VarsContext extends ParserRuleContext {
		public Token Id;
		public TypeContext type;
		public List<TerminalNode> Id() { return getTokens(patitoParser.Id); }
		public TerminalNode Id(int i) {
			return getToken(patitoParser.Id, i);
		}
		public List<TypeContext> type() {
			return getRuleContexts(TypeContext.class);
		}
		public TypeContext type(int i) {
			return getRuleContext(TypeContext.class,i);
		}
		public VarsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).enterVars(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).exitVars(this);
		}
	}

	public final VarsContext vars() throws RecognitionException {
		VarsContext _localctx = new VarsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_vars);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			global current_content, current_func, current_scope, current_type, current_var, various_vars
			setState(60);
			match(T__4);
			setState(77); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(61);
				((VarsContext)_localctx).Id = match(Id);
				various_vars.append((((VarsContext)_localctx).Id!=null?((VarsContext)_localctx).Id.getText():null))
				setState(68);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__5) {
					{
					{
					setState(63);
					match(T__5);
					setState(64);
					((VarsContext)_localctx).Id = match(Id);
					various_vars.append((((VarsContext)_localctx).Id!=null?((VarsContext)_localctx).Id.getText():null))
					}
					}
					setState(70);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(71);
				match(T__6);
				setState(72);
				((VarsContext)_localctx).type = type();
				current_type = (((VarsContext)_localctx).type!=null?_input.getText(((VarsContext)_localctx).type.start,((VarsContext)_localctx).type.stop):null)
				setState(74);
				match(T__1);

				for myvar in various_vars: funclist.add_variable_to_function(current_func, myvar, current_type, current_scope, current_content);
				various_vars = [];

				}
				}
				setState(79); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==Id );
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

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).enterType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).exitType(this);
		}
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			_la = _input.LA(1);
			if ( !(_la==T__7 || _la==T__8) ) {
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

	@SuppressWarnings("CheckReturnValue")
	public static class FuncsContext extends ParserRuleContext {
		public Token Id;
		public TypeContext type;
		public List<TerminalNode> Id() { return getTokens(patitoParser.Id); }
		public TerminalNode Id(int i) {
			return getToken(patitoParser.Id, i);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public List<TypeContext> type() {
			return getRuleContexts(TypeContext.class);
		}
		public TypeContext type(int i) {
			return getRuleContext(TypeContext.class,i);
		}
		public VarsContext vars() {
			return getRuleContext(VarsContext.class,0);
		}
		public FuncsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcs; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).enterFuncs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).exitFuncs(this);
		}
	}

	public final FuncsContext funcs() throws RecognitionException {
		FuncsContext _localctx = new FuncsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_funcs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			global current_content, current_func, current_scope, current_type, current_var
			setState(84);
			match(T__9);
			current_scope+=1
			setState(86);
			((FuncsContext)_localctx).Id = match(Id);
			current_func = (((FuncsContext)_localctx).Id!=null?((FuncsContext)_localctx).Id.getText():null); funclist.add_function(current_func)
			setState(88);
			match(T__10);
			setState(106);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==Id) {
				{
				{
				setState(89);
				((FuncsContext)_localctx).Id = match(Id);
				setState(90);
				match(T__6);
				setState(91);
				((FuncsContext)_localctx).type = type();
				current_var = (((FuncsContext)_localctx).Id!=null?((FuncsContext)_localctx).Id.getText():null); 
				current_type = (((FuncsContext)_localctx).type!=null?_input.getText(((FuncsContext)_localctx).type.start,((FuncsContext)_localctx).type.stop):null); 
				funclist.add_variable_to_function(current_func, current_var, current_type, current_scope, current_content)
				setState(101);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__5) {
					{
					{
					setState(93);
					match(T__5);
					setState(94);
					((FuncsContext)_localctx).Id = match(Id);
					setState(95);
					match(T__6);
					setState(96);
					((FuncsContext)_localctx).type = type();
					current_var = (((FuncsContext)_localctx).Id!=null?((FuncsContext)_localctx).Id.getText():null); current_type = (((FuncsContext)_localctx).type!=null?_input.getText(((FuncsContext)_localctx).type.start,((FuncsContext)_localctx).type.stop):null); 
					funclist.add_variable_to_function(current_func, current_var, current_type, current_scope, current_content)
					}
					}
					setState(103);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				}
				setState(108);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(109);
			match(T__11);
			setState(110);
			match(T__12);
			setState(112);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(111);
				vars();
				}
			}

			setState(114);
			body();
			setState(115);
			match(T__13);
			setState(116);
			match(T__1);
			current_scope-=1;
			funclist.delete_all_variables(current_func)
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

	@SuppressWarnings("CheckReturnValue")
	public static class BodyContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).enterBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).exitBody(this);
		}
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			match(T__14);
			setState(124);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1778384896L) != 0)) {
				{
				{
				setState(121);
				statement();
				}
				}
				setState(126);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(127);
			match(T__15);
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

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public CycleContext cycle() {
			return getRuleContext(CycleContext.class,0);
		}
		public F_callContext f_call() {
			return getRuleContext(F_callContext.class,0);
		}
		public PrintContext print() {
			return getRuleContext(PrintContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_statement);
		try {
			setState(134);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(129);
				assign();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(130);
				condition();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(131);
				cycle();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(132);
				f_call();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(133);
				print();
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

	@SuppressWarnings("CheckReturnValue")
	public static class AssignContext extends ParserRuleContext {
		public Token Id;
		public TerminalNode Id() { return getToken(patitoParser.Id, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).enterAssign(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).exitAssign(this);
		}
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(136);
			((AssignContext)_localctx).Id = match(Id);

			quads.push_operate(funclist.get_variable_memory((((AssignContext)_localctx).Id!=null?((AssignContext)_localctx).Id.getText():null), current_scope), funclist.get_variable_type((((AssignContext)_localctx).Id!=null?((AssignContext)_localctx).Id.getText():null), current_scope), False, False, 0, '')

			setState(138);
			match(T__16);

			quads.push_operator('=')

			setState(140);
			expression();

			quads.quads_Assign()

			setState(142);
			match(T__1);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).exitExpression(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			exp();

			quads.quads_Compare()

			setState(159);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1835008L) != 0)) {
				{
				{
				setState(152);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__17:
					{
					setState(146);
					match(T__17);

					quads.push_operator('>')

					}
					break;
				case T__18:
					{
					setState(148);
					match(T__18);

					quads.push_operator('<')

					}
					break;
				case T__19:
					{
					setState(150);
					match(T__19);

					quads.push_operator('!=')

					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(154);
				exp();

				quads.quads_Compare()

				}
				}
				setState(161);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ExpContext extends ParserRuleContext {
		public List<TerminoContext> termino() {
			return getRuleContexts(TerminoContext.class);
		}
		public TerminoContext termino(int i) {
			return getRuleContext(TerminoContext.class,i);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).enterExp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).exitExp(this);
		}
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			termino();

			quads.quads_PlusMin()

			setState(175);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__20 || _la==T__21) {
				{
				{
				setState(168);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__20:
					{
					setState(164);
					match(T__20);

					quads.push_operator('+')

					}
					break;
				case T__21:
					{
					setState(166);
					match(T__21);

					quads.push_operator('-')

					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(170);
				termino();

				quads.quads_PlusMin()

				}
				}
				setState(177);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	@SuppressWarnings("CheckReturnValue")
	public static class TerminoContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public TerminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termino; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).enterTermino(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).exitTermino(this);
		}
	}

	public final TerminoContext termino() throws RecognitionException {
		TerminoContext _localctx = new TerminoContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_termino);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(178);
			factor();

			quads.quads_MultDiv()

			setState(191);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__22 || _la==T__23) {
				{
				{
				setState(184);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__22:
					{
					setState(180);
					match(T__22);

					quads.push_operator('*')

					}
					break;
				case T__23:
					{
					setState(182);
					match(T__23);

					quads.push_operator('/')

					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(186);
				factor();

				quads.quads_MultDiv()

				}
				}
				setState(193);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public Token Id;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode Id() { return getToken(patitoParser.Id, 0); }
		public CteContext cte() {
			return getRuleContext(CteContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).enterFactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).exitFactor(this);
		}
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_factor);
		try {
			setState(217);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(194);
				match(T__10);

				quads.push_FF()

				setState(196);
				expression();
				setState(197);
				match(T__11);

				quads.pop_FF()

				}
				}
				break;
			case T__20:
			case T__21:
				enterOuterAlt(_localctx, 2);
				{
				{
				global temporal_operator
				setState(205);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__20:
					{
					setState(201);
					match(T__20);
					temporal_operator = '+'
					}
					break;
				case T__21:
					{
					setState(203);
					match(T__21);
					temporal_operator = '-'
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(210);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case Id:
					{
					setState(207);
					((FactorContext)_localctx).Id = match(Id);

					quads.push_operate(funclist.get_variable_memory((((FactorContext)_localctx).Id!=null?((FactorContext)_localctx).Id.getText():null), current_scope), funclist.get_variable_type((((FactorContext)_localctx).Id!=null?((FactorContext)_localctx).Id.getText():null), current_scope), False, False, (((FactorContext)_localctx).Id!=null?((FactorContext)_localctx).Id.getText():null), temporal_operator); temporal_operator = ''

					}
					break;
				case Cte_int:
				case Cte_float:
				case Cte_string:
					{
					setState(209);
					cte();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				}
				break;
			case Id:
			case Cte_int:
			case Cte_float:
			case Cte_string:
				enterOuterAlt(_localctx, 3);
				{
				setState(215);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case Id:
					{
					setState(212);
					((FactorContext)_localctx).Id = match(Id);

					quads.push_operate(funclist.get_variable_memory((((FactorContext)_localctx).Id!=null?((FactorContext)_localctx).Id.getText():null), current_scope), funclist.get_variable_type((((FactorContext)_localctx).Id!=null?((FactorContext)_localctx).Id.getText():null), current_scope), False, False, (((FactorContext)_localctx).Id!=null?((FactorContext)_localctx).Id.getText():null), '')

					}
					break;
				case Cte_int:
				case Cte_float:
				case Cte_string:
					{
					setState(214);
					cte();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
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

	@SuppressWarnings("CheckReturnValue")
	public static class CteContext extends ParserRuleContext {
		public Token Cte_int;
		public Token Cte_float;
		public Token Cte_string;
		public TerminalNode Cte_int() { return getToken(patitoParser.Cte_int, 0); }
		public TerminalNode Cte_float() { return getToken(patitoParser.Cte_float, 0); }
		public TerminalNode Cte_string() { return getToken(patitoParser.Cte_string, 0); }
		public CteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cte; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).enterCte(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).exitCte(this);
		}
	}

	public final CteContext cte() throws RecognitionException {
		CteContext _localctx = new CteContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_cte);
		try {
			setState(226);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Cte_int:
				enterOuterAlt(_localctx, 1);
				{
				setState(219);
				((CteContext)_localctx).Cte_int = match(Cte_int);
				global temporal_operator

				quads.push_operate((((CteContext)_localctx).Cte_int!=null?((CteContext)_localctx).Cte_int.getText():null), "int", True, False, 0, temporal_operator); temporal_operator = ''

				}
				break;
			case Cte_float:
				enterOuterAlt(_localctx, 2);
				{
				setState(222);
				((CteContext)_localctx).Cte_float = match(Cte_float);

				quads.push_operate((((CteContext)_localctx).Cte_float!=null?((CteContext)_localctx).Cte_float.getText():null), "float", True, False, 0, temporal_operator); temporal_operator = ''

				}
				break;
			case Cte_string:
				enterOuterAlt(_localctx, 3);
				{
				setState(224);
				((CteContext)_localctx).Cte_string = match(Cte_string);

				quads.push_operate((((CteContext)_localctx).Cte_string!=null?((CteContext)_localctx).Cte_string.getText():null), "string", True, False, 0, temporal_operator); temporal_operator = ''

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

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<BodyContext> body() {
			return getRuleContexts(BodyContext.class);
		}
		public BodyContext body(int i) {
			return getRuleContext(BodyContext.class,i);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).enterCondition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).exitCondition(this);
		}
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(228);
			match(T__24);
			setState(229);
			match(T__10);
			setState(230);
			expression();
			setState(231);
			match(T__11);

			quads.quad_if_1()

			setState(233);
			body();
			setState(237);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__25) {
				{
				setState(234);
				match(T__25);

				quads.quad_if_3()

				setState(236);
				body();
				}
			}

			setState(239);
			match(T__1);

			quads.quad_if_2()

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

	@SuppressWarnings("CheckReturnValue")
	public static class CycleContext extends ParserRuleContext {
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public CycleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cycle; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).enterCycle(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).exitCycle(this);
		}
	}

	public final CycleContext cycle() throws RecognitionException {
		CycleContext _localctx = new CycleContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_cycle);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(242);
			match(T__26);

			quads.quad_while_1()

			setState(244);
			body();
			setState(245);
			match(T__27);
			setState(246);
			match(T__10);
			setState(247);
			expression();
			setState(248);
			match(T__11);

			quads.quad_while_return()

			setState(250);
			match(T__1);



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

	@SuppressWarnings("CheckReturnValue")
	public static class F_callContext extends ParserRuleContext {
		public TerminalNode Id() { return getToken(patitoParser.Id, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public F_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_f_call; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).enterF_call(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).exitF_call(this);
		}
	}

	public final F_callContext f_call() throws RecognitionException {
		F_callContext _localctx = new F_callContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_f_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(253);
			match(Id);
			setState(254);
			match(T__10);
			setState(263);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 16112420864L) != 0)) {
				{
				setState(255);
				expression();
				setState(260);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__5) {
					{
					{
					setState(256);
					match(T__5);
					setState(257);
					expression();
					}
					}
					setState(262);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(265);
			match(T__11);
			setState(266);
			match(T__1);
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

	@SuppressWarnings("CheckReturnValue")
	public static class PrintContext extends ParserRuleContext {
		public Token Cte_string;
		public List<TerminalNode> Cte_string() { return getTokens(patitoParser.Cte_string); }
		public TerminalNode Cte_string(int i) {
			return getToken(patitoParser.Cte_string, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public PrintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).enterPrint(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof patitoListener ) ((patitoListener)listener).exitPrint(this);
		}
	}

	public final PrintContext print() throws RecognitionException {
		PrintContext _localctx = new PrintContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_print);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(268);
			match(T__28);

			quads.push_operator('print')

			setState(270);
			match(T__10);
			setState(274);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				{
				setState(271);
				((PrintContext)_localctx).Cte_string = match(Cte_string);

				quads.push_operate((((PrintContext)_localctx).Cte_string!=null?((PrintContext)_localctx).Cte_string.getText():null), "string", True, False, 0, '')

				}
				break;
			case 2:
				{
				setState(273);
				expression();
				}
				break;
			}
			setState(284);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(276);
				match(T__5);
				setState(280);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
				case 1:
					{
					setState(277);
					((PrintContext)_localctx).Cte_string = match(Cte_string);

					quads.push_operate((((PrintContext)_localctx).Cte_string!=null?((PrintContext)_localctx).Cte_string.getText():null), "string", True, False, 0, '')

					}
					break;
				case 2:
					{
					setState(279);
					expression();
					}
					break;
				}
				}
				}
				setState(286);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(287);
			match(T__11);

			quads.quads_Print()

			setState(289);
			match(T__1);
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
		"\u0004\u0001\"\u0124\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		",\b\u0001\u0001\u0001\u0005\u0001/\b\u0001\n\u0001\f\u00012\t\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0005\u0002C\b\u0002\n\u0002\f\u0002F\t"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0004\u0002N\b\u0002\u000b\u0002\f\u0002O\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004d\b\u0004"+
		"\n\u0004\f\u0004g\t\u0004\u0005\u0004i\b\u0004\n\u0004\f\u0004l\t\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004q\b\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0005\u0005{\b\u0005\n\u0005\f\u0005~\t\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0003\u0006\u0087\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u0099\b\b\u0001\b\u0001"+
		"\b\u0001\b\u0005\b\u009e\b\b\n\b\f\b\u00a1\t\b\u0001\t\u0001\t\u0001\t"+
		"\u0001\t\u0001\t\u0001\t\u0003\t\u00a9\b\t\u0001\t\u0001\t\u0001\t\u0005"+
		"\t\u00ae\b\t\n\t\f\t\u00b1\t\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n"+
		"\u0001\n\u0003\n\u00b9\b\n\u0001\n\u0001\n\u0001\n\u0005\n\u00be\b\n\n"+
		"\n\f\n\u00c1\t\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0003\u000b\u00ce\b\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003"+
		"\u000b\u00d3\b\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u00d8"+
		"\b\u000b\u0003\u000b\u00da\b\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0003\f\u00e3\b\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u00ee\b\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u0103\b\u000f"+
		"\n\u000f\f\u000f\u0106\t\u000f\u0003\u000f\u0108\b\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0003\u0010\u0113\b\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0003\u0010\u0119\b\u0010\u0005\u0010\u011b\b\u0010"+
		"\n\u0010\f\u0010\u011e\t\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0000\u0000\u0011\u0000\u0002\u0004\u0006\b\n\f\u000e"+
		"\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \u0000\u0001\u0001\u0000"+
		"\b\t\u0132\u0000\"\u0001\u0000\u0000\u0000\u0002%\u0001\u0000\u0000\u0000"+
		"\u0004;\u0001\u0000\u0000\u0000\u0006Q\u0001\u0000\u0000\u0000\bS\u0001"+
		"\u0000\u0000\u0000\nx\u0001\u0000\u0000\u0000\f\u0086\u0001\u0000\u0000"+
		"\u0000\u000e\u0088\u0001\u0000\u0000\u0000\u0010\u0090\u0001\u0000\u0000"+
		"\u0000\u0012\u00a2\u0001\u0000\u0000\u0000\u0014\u00b2\u0001\u0000\u0000"+
		"\u0000\u0016\u00d9\u0001\u0000\u0000\u0000\u0018\u00e2\u0001\u0000\u0000"+
		"\u0000\u001a\u00e4\u0001\u0000\u0000\u0000\u001c\u00f2\u0001\u0000\u0000"+
		"\u0000\u001e\u00fd\u0001\u0000\u0000\u0000 \u010c\u0001\u0000\u0000\u0000"+
		"\"#\u0003\u0002\u0001\u0000#$\u0005\u0000\u0000\u0001$\u0001\u0001\u0000"+
		"\u0000\u0000%&\u0005\u0001\u0000\u0000&\'\u0006\u0001\uffff\uffff\u0000"+
		"\'(\u0005\u001e\u0000\u0000()\u0006\u0001\uffff\uffff\u0000)+\u0005\u0002"+
		"\u0000\u0000*,\u0003\u0004\u0002\u0000+*\u0001\u0000\u0000\u0000+,\u0001"+
		"\u0000\u0000\u0000,0\u0001\u0000\u0000\u0000-/\u0003\b\u0004\u0000.-\u0001"+
		"\u0000\u0000\u0000/2\u0001\u0000\u0000\u00000.\u0001\u0000\u0000\u0000"+
		"01\u0001\u0000\u0000\u000013\u0001\u0000\u0000\u000020\u0001\u0000\u0000"+
		"\u000034\u0005\u0003\u0000\u000045\u0006\u0001\uffff\uffff\u000056\u0006"+
		"\u0001\uffff\uffff\u000067\u0003\n\u0005\u000078\u0006\u0001\uffff\uffff"+
		"\u000089\u0005\u0004\u0000\u00009:\u0006\u0001\uffff\uffff\u0000:\u0003"+
		"\u0001\u0000\u0000\u0000;<\u0006\u0002\uffff\uffff\u0000<M\u0005\u0005"+
		"\u0000\u0000=>\u0005\u001e\u0000\u0000>D\u0006\u0002\uffff\uffff\u0000"+
		"?@\u0005\u0006\u0000\u0000@A\u0005\u001e\u0000\u0000AC\u0006\u0002\uffff"+
		"\uffff\u0000B?\u0001\u0000\u0000\u0000CF\u0001\u0000\u0000\u0000DB\u0001"+
		"\u0000\u0000\u0000DE\u0001\u0000\u0000\u0000EG\u0001\u0000\u0000\u0000"+
		"FD\u0001\u0000\u0000\u0000GH\u0005\u0007\u0000\u0000HI\u0003\u0006\u0003"+
		"\u0000IJ\u0006\u0002\uffff\uffff\u0000JK\u0005\u0002\u0000\u0000KL\u0006"+
		"\u0002\uffff\uffff\u0000LN\u0001\u0000\u0000\u0000M=\u0001\u0000\u0000"+
		"\u0000NO\u0001\u0000\u0000\u0000OM\u0001\u0000\u0000\u0000OP\u0001\u0000"+
		"\u0000\u0000P\u0005\u0001\u0000\u0000\u0000QR\u0007\u0000\u0000\u0000"+
		"R\u0007\u0001\u0000\u0000\u0000ST\u0006\u0004\uffff\uffff\u0000TU\u0005"+
		"\n\u0000\u0000UV\u0006\u0004\uffff\uffff\u0000VW\u0005\u001e\u0000\u0000"+
		"WX\u0006\u0004\uffff\uffff\u0000Xj\u0005\u000b\u0000\u0000YZ\u0005\u001e"+
		"\u0000\u0000Z[\u0005\u0007\u0000\u0000[\\\u0003\u0006\u0003\u0000\\e\u0006"+
		"\u0004\uffff\uffff\u0000]^\u0005\u0006\u0000\u0000^_\u0005\u001e\u0000"+
		"\u0000_`\u0005\u0007\u0000\u0000`a\u0003\u0006\u0003\u0000ab\u0006\u0004"+
		"\uffff\uffff\u0000bd\u0001\u0000\u0000\u0000c]\u0001\u0000\u0000\u0000"+
		"dg\u0001\u0000\u0000\u0000ec\u0001\u0000\u0000\u0000ef\u0001\u0000\u0000"+
		"\u0000fi\u0001\u0000\u0000\u0000ge\u0001\u0000\u0000\u0000hY\u0001\u0000"+
		"\u0000\u0000il\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000\u0000jk\u0001"+
		"\u0000\u0000\u0000km\u0001\u0000\u0000\u0000lj\u0001\u0000\u0000\u0000"+
		"mn\u0005\f\u0000\u0000np\u0005\r\u0000\u0000oq\u0003\u0004\u0002\u0000"+
		"po\u0001\u0000\u0000\u0000pq\u0001\u0000\u0000\u0000qr\u0001\u0000\u0000"+
		"\u0000rs\u0003\n\u0005\u0000st\u0005\u000e\u0000\u0000tu\u0005\u0002\u0000"+
		"\u0000uv\u0006\u0004\uffff\uffff\u0000vw\u0006\u0004\uffff\uffff\u0000"+
		"w\t\u0001\u0000\u0000\u0000x|\u0005\u000f\u0000\u0000y{\u0003\f\u0006"+
		"\u0000zy\u0001\u0000\u0000\u0000{~\u0001\u0000\u0000\u0000|z\u0001\u0000"+
		"\u0000\u0000|}\u0001\u0000\u0000\u0000}\u007f\u0001\u0000\u0000\u0000"+
		"~|\u0001\u0000\u0000\u0000\u007f\u0080\u0005\u0010\u0000\u0000\u0080\u000b"+
		"\u0001\u0000\u0000\u0000\u0081\u0087\u0003\u000e\u0007\u0000\u0082\u0087"+
		"\u0003\u001a\r\u0000\u0083\u0087\u0003\u001c\u000e\u0000\u0084\u0087\u0003"+
		"\u001e\u000f\u0000\u0085\u0087\u0003 \u0010\u0000\u0086\u0081\u0001\u0000"+
		"\u0000\u0000\u0086\u0082\u0001\u0000\u0000\u0000\u0086\u0083\u0001\u0000"+
		"\u0000\u0000\u0086\u0084\u0001\u0000\u0000\u0000\u0086\u0085\u0001\u0000"+
		"\u0000\u0000\u0087\r\u0001\u0000\u0000\u0000\u0088\u0089\u0005\u001e\u0000"+
		"\u0000\u0089\u008a\u0006\u0007\uffff\uffff\u0000\u008a\u008b\u0005\u0011"+
		"\u0000\u0000\u008b\u008c\u0006\u0007\uffff\uffff\u0000\u008c\u008d\u0003"+
		"\u0010\b\u0000\u008d\u008e\u0006\u0007\uffff\uffff\u0000\u008e\u008f\u0005"+
		"\u0002\u0000\u0000\u008f\u000f\u0001\u0000\u0000\u0000\u0090\u0091\u0003"+
		"\u0012\t\u0000\u0091\u009f\u0006\b\uffff\uffff\u0000\u0092\u0093\u0005"+
		"\u0012\u0000\u0000\u0093\u0099\u0006\b\uffff\uffff\u0000\u0094\u0095\u0005"+
		"\u0013\u0000\u0000\u0095\u0099\u0006\b\uffff\uffff\u0000\u0096\u0097\u0005"+
		"\u0014\u0000\u0000\u0097\u0099\u0006\b\uffff\uffff\u0000\u0098\u0092\u0001"+
		"\u0000\u0000\u0000\u0098\u0094\u0001\u0000\u0000\u0000\u0098\u0096\u0001"+
		"\u0000\u0000\u0000\u0099\u009a\u0001\u0000\u0000\u0000\u009a\u009b\u0003"+
		"\u0012\t\u0000\u009b\u009c\u0006\b\uffff\uffff\u0000\u009c\u009e\u0001"+
		"\u0000\u0000\u0000\u009d\u0098\u0001\u0000\u0000\u0000\u009e\u00a1\u0001"+
		"\u0000\u0000\u0000\u009f\u009d\u0001\u0000\u0000\u0000\u009f\u00a0\u0001"+
		"\u0000\u0000\u0000\u00a0\u0011\u0001\u0000\u0000\u0000\u00a1\u009f\u0001"+
		"\u0000\u0000\u0000\u00a2\u00a3\u0003\u0014\n\u0000\u00a3\u00af\u0006\t"+
		"\uffff\uffff\u0000\u00a4\u00a5\u0005\u0015\u0000\u0000\u00a5\u00a9\u0006"+
		"\t\uffff\uffff\u0000\u00a6\u00a7\u0005\u0016\u0000\u0000\u00a7\u00a9\u0006"+
		"\t\uffff\uffff\u0000\u00a8\u00a4\u0001\u0000\u0000\u0000\u00a8\u00a6\u0001"+
		"\u0000\u0000\u0000\u00a9\u00aa\u0001\u0000\u0000\u0000\u00aa\u00ab\u0003"+
		"\u0014\n\u0000\u00ab\u00ac\u0006\t\uffff\uffff\u0000\u00ac\u00ae\u0001"+
		"\u0000\u0000\u0000\u00ad\u00a8\u0001\u0000\u0000\u0000\u00ae\u00b1\u0001"+
		"\u0000\u0000\u0000\u00af\u00ad\u0001\u0000\u0000\u0000\u00af\u00b0\u0001"+
		"\u0000\u0000\u0000\u00b0\u0013\u0001\u0000\u0000\u0000\u00b1\u00af\u0001"+
		"\u0000\u0000\u0000\u00b2\u00b3\u0003\u0016\u000b\u0000\u00b3\u00bf\u0006"+
		"\n\uffff\uffff\u0000\u00b4\u00b5\u0005\u0017\u0000\u0000\u00b5\u00b9\u0006"+
		"\n\uffff\uffff\u0000\u00b6\u00b7\u0005\u0018\u0000\u0000\u00b7\u00b9\u0006"+
		"\n\uffff\uffff\u0000\u00b8\u00b4\u0001\u0000\u0000\u0000\u00b8\u00b6\u0001"+
		"\u0000\u0000\u0000\u00b9\u00ba\u0001\u0000\u0000\u0000\u00ba\u00bb\u0003"+
		"\u0016\u000b\u0000\u00bb\u00bc\u0006\n\uffff\uffff\u0000\u00bc\u00be\u0001"+
		"\u0000\u0000\u0000\u00bd\u00b8\u0001\u0000\u0000\u0000\u00be\u00c1\u0001"+
		"\u0000\u0000\u0000\u00bf\u00bd\u0001\u0000\u0000\u0000\u00bf\u00c0\u0001"+
		"\u0000\u0000\u0000\u00c0\u0015\u0001\u0000\u0000\u0000\u00c1\u00bf\u0001"+
		"\u0000\u0000\u0000\u00c2\u00c3\u0005\u000b\u0000\u0000\u00c3\u00c4\u0006"+
		"\u000b\uffff\uffff\u0000\u00c4\u00c5\u0003\u0010\b\u0000\u00c5\u00c6\u0005"+
		"\f\u0000\u0000\u00c6\u00c7\u0006\u000b\uffff\uffff\u0000\u00c7\u00da\u0001"+
		"\u0000\u0000\u0000\u00c8\u00cd\u0006\u000b\uffff\uffff\u0000\u00c9\u00ca"+
		"\u0005\u0015\u0000\u0000\u00ca\u00ce\u0006\u000b\uffff\uffff\u0000\u00cb"+
		"\u00cc\u0005\u0016\u0000\u0000\u00cc\u00ce\u0006\u000b\uffff\uffff\u0000"+
		"\u00cd\u00c9\u0001\u0000\u0000\u0000\u00cd\u00cb\u0001\u0000\u0000\u0000"+
		"\u00ce\u00d2\u0001\u0000\u0000\u0000\u00cf\u00d0\u0005\u001e\u0000\u0000"+
		"\u00d0\u00d3\u0006\u000b\uffff\uffff\u0000\u00d1\u00d3\u0003\u0018\f\u0000"+
		"\u00d2\u00cf\u0001\u0000\u0000\u0000\u00d2\u00d1\u0001\u0000\u0000\u0000"+
		"\u00d3\u00da\u0001\u0000\u0000\u0000\u00d4\u00d5\u0005\u001e\u0000\u0000"+
		"\u00d5\u00d8\u0006\u000b\uffff\uffff\u0000\u00d6\u00d8\u0003\u0018\f\u0000"+
		"\u00d7\u00d4\u0001\u0000\u0000\u0000\u00d7\u00d6\u0001\u0000\u0000\u0000"+
		"\u00d8\u00da\u0001\u0000\u0000\u0000\u00d9\u00c2\u0001\u0000\u0000\u0000"+
		"\u00d9\u00c8\u0001\u0000\u0000\u0000\u00d9\u00d7\u0001\u0000\u0000\u0000"+
		"\u00da\u0017\u0001\u0000\u0000\u0000\u00db\u00dc\u0005\u001f\u0000\u0000"+
		"\u00dc\u00dd\u0006\f\uffff\uffff\u0000\u00dd\u00e3\u0006\f\uffff\uffff"+
		"\u0000\u00de\u00df\u0005 \u0000\u0000\u00df\u00e3\u0006\f\uffff\uffff"+
		"\u0000\u00e0\u00e1\u0005!\u0000\u0000\u00e1\u00e3\u0006\f\uffff\uffff"+
		"\u0000\u00e2\u00db\u0001\u0000\u0000\u0000\u00e2\u00de\u0001\u0000\u0000"+
		"\u0000\u00e2\u00e0\u0001\u0000\u0000\u0000\u00e3\u0019\u0001\u0000\u0000"+
		"\u0000\u00e4\u00e5\u0005\u0019\u0000\u0000\u00e5\u00e6\u0005\u000b\u0000"+
		"\u0000\u00e6\u00e7\u0003\u0010\b\u0000\u00e7\u00e8\u0005\f\u0000\u0000"+
		"\u00e8\u00e9\u0006\r\uffff\uffff\u0000\u00e9\u00ed\u0003\n\u0005\u0000"+
		"\u00ea\u00eb\u0005\u001a\u0000\u0000\u00eb\u00ec\u0006\r\uffff\uffff\u0000"+
		"\u00ec\u00ee\u0003\n\u0005\u0000\u00ed\u00ea\u0001\u0000\u0000\u0000\u00ed"+
		"\u00ee\u0001\u0000\u0000\u0000\u00ee\u00ef\u0001\u0000\u0000\u0000\u00ef"+
		"\u00f0\u0005\u0002\u0000\u0000\u00f0\u00f1\u0006\r\uffff\uffff\u0000\u00f1"+
		"\u001b\u0001\u0000\u0000\u0000\u00f2\u00f3\u0005\u001b\u0000\u0000\u00f3"+
		"\u00f4\u0006\u000e\uffff\uffff\u0000\u00f4\u00f5\u0003\n\u0005\u0000\u00f5"+
		"\u00f6\u0005\u001c\u0000\u0000\u00f6\u00f7\u0005\u000b\u0000\u0000\u00f7"+
		"\u00f8\u0003\u0010\b\u0000\u00f8\u00f9\u0005\f\u0000\u0000\u00f9\u00fa"+
		"\u0006\u000e\uffff\uffff\u0000\u00fa\u00fb\u0005\u0002\u0000\u0000\u00fb"+
		"\u00fc\u0006\u000e\uffff\uffff\u0000\u00fc\u001d\u0001\u0000\u0000\u0000"+
		"\u00fd\u00fe\u0005\u001e\u0000\u0000\u00fe\u0107\u0005\u000b\u0000\u0000"+
		"\u00ff\u0104\u0003\u0010\b\u0000\u0100\u0101\u0005\u0006\u0000\u0000\u0101"+
		"\u0103\u0003\u0010\b\u0000\u0102\u0100\u0001\u0000\u0000\u0000\u0103\u0106"+
		"\u0001\u0000\u0000\u0000\u0104\u0102\u0001\u0000\u0000\u0000\u0104\u0105"+
		"\u0001\u0000\u0000\u0000\u0105\u0108\u0001\u0000\u0000\u0000\u0106\u0104"+
		"\u0001\u0000\u0000\u0000\u0107\u00ff\u0001\u0000\u0000\u0000\u0107\u0108"+
		"\u0001\u0000\u0000\u0000\u0108\u0109\u0001\u0000\u0000\u0000\u0109\u010a"+
		"\u0005\f\u0000\u0000\u010a\u010b\u0005\u0002\u0000\u0000\u010b\u001f\u0001"+
		"\u0000\u0000\u0000\u010c\u010d\u0005\u001d\u0000\u0000\u010d\u010e\u0006"+
		"\u0010\uffff\uffff\u0000\u010e\u0112\u0005\u000b\u0000\u0000\u010f\u0110"+
		"\u0005!\u0000\u0000\u0110\u0113\u0006\u0010\uffff\uffff\u0000\u0111\u0113"+
		"\u0003\u0010\b\u0000\u0112\u010f\u0001\u0000\u0000\u0000\u0112\u0111\u0001"+
		"\u0000\u0000\u0000\u0113\u011c\u0001\u0000\u0000\u0000\u0114\u0118\u0005"+
		"\u0006\u0000\u0000\u0115\u0116\u0005!\u0000\u0000\u0116\u0119\u0006\u0010"+
		"\uffff\uffff\u0000\u0117\u0119\u0003\u0010\b\u0000\u0118\u0115\u0001\u0000"+
		"\u0000\u0000\u0118\u0117\u0001\u0000\u0000\u0000\u0119\u011b\u0001\u0000"+
		"\u0000\u0000\u011a\u0114\u0001\u0000\u0000\u0000\u011b\u011e\u0001\u0000"+
		"\u0000\u0000\u011c\u011a\u0001\u0000\u0000\u0000\u011c\u011d\u0001\u0000"+
		"\u0000\u0000\u011d\u011f\u0001\u0000\u0000\u0000\u011e\u011c\u0001\u0000"+
		"\u0000\u0000\u011f\u0120\u0005\f\u0000\u0000\u0120\u0121\u0006\u0010\uffff"+
		"\uffff\u0000\u0121\u0122\u0005\u0002\u0000\u0000\u0122!\u0001\u0000\u0000"+
		"\u0000\u001a+0DOejp|\u0086\u0098\u009f\u00a8\u00af\u00b8\u00bf\u00cd\u00d2"+
		"\u00d7\u00d9\u00e2\u00ed\u0104\u0107\u0112\u0118\u011c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}