// Generated from c:/Users/YO/Documents/Python Projects/compiler/patito.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link patitoParser}.
 */
public interface patitoListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link patitoParser#startRule}.
	 * @param ctx the parse tree
	 */
	void enterStartRule(patitoParser.StartRuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link patitoParser#startRule}.
	 * @param ctx the parse tree
	 */
	void exitStartRule(patitoParser.StartRuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link patitoParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(patitoParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link patitoParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(patitoParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link patitoParser#vars}.
	 * @param ctx the parse tree
	 */
	void enterVars(patitoParser.VarsContext ctx);
	/**
	 * Exit a parse tree produced by {@link patitoParser#vars}.
	 * @param ctx the parse tree
	 */
	void exitVars(patitoParser.VarsContext ctx);
	/**
	 * Enter a parse tree produced by {@link patitoParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(patitoParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link patitoParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(patitoParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link patitoParser#funcs}.
	 * @param ctx the parse tree
	 */
	void enterFuncs(patitoParser.FuncsContext ctx);
	/**
	 * Exit a parse tree produced by {@link patitoParser#funcs}.
	 * @param ctx the parse tree
	 */
	void exitFuncs(patitoParser.FuncsContext ctx);
	/**
	 * Enter a parse tree produced by {@link patitoParser#body}.
	 * @param ctx the parse tree
	 */
	void enterBody(patitoParser.BodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link patitoParser#body}.
	 * @param ctx the parse tree
	 */
	void exitBody(patitoParser.BodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link patitoParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(patitoParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link patitoParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(patitoParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link patitoParser#assign}.
	 * @param ctx the parse tree
	 */
	void enterAssign(patitoParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link patitoParser#assign}.
	 * @param ctx the parse tree
	 */
	void exitAssign(patitoParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link patitoParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(patitoParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link patitoParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(patitoParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link patitoParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(patitoParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link patitoParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(patitoParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link patitoParser#termino}.
	 * @param ctx the parse tree
	 */
	void enterTermino(patitoParser.TerminoContext ctx);
	/**
	 * Exit a parse tree produced by {@link patitoParser#termino}.
	 * @param ctx the parse tree
	 */
	void exitTermino(patitoParser.TerminoContext ctx);
	/**
	 * Enter a parse tree produced by {@link patitoParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(patitoParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link patitoParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(patitoParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link patitoParser#cte}.
	 * @param ctx the parse tree
	 */
	void enterCte(patitoParser.CteContext ctx);
	/**
	 * Exit a parse tree produced by {@link patitoParser#cte}.
	 * @param ctx the parse tree
	 */
	void exitCte(patitoParser.CteContext ctx);
	/**
	 * Enter a parse tree produced by {@link patitoParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(patitoParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link patitoParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(patitoParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link patitoParser#cycle}.
	 * @param ctx the parse tree
	 */
	void enterCycle(patitoParser.CycleContext ctx);
	/**
	 * Exit a parse tree produced by {@link patitoParser#cycle}.
	 * @param ctx the parse tree
	 */
	void exitCycle(patitoParser.CycleContext ctx);
	/**
	 * Enter a parse tree produced by {@link patitoParser#f_call}.
	 * @param ctx the parse tree
	 */
	void enterF_call(patitoParser.F_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link patitoParser#f_call}.
	 * @param ctx the parse tree
	 */
	void exitF_call(patitoParser.F_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link patitoParser#print}.
	 * @param ctx the parse tree
	 */
	void enterPrint(patitoParser.PrintContext ctx);
	/**
	 * Exit a parse tree produced by {@link patitoParser#print}.
	 * @param ctx the parse tree
	 */
	void exitPrint(patitoParser.PrintContext ctx);
}