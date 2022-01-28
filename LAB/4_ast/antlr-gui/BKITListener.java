// Generated from BKIT.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link BKITParser}.
 */
public interface BKITListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link BKITParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(BKITParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(BKITParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(BKITParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(BKITParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(BKITParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(BKITParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(BKITParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(BKITParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#operand}.
	 * @param ctx the parse tree
	 */
	void enterOperand(BKITParser.OperandContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#operand}.
	 * @param ctx the parse tree
	 */
	void exitOperand(BKITParser.OperandContext ctx);
}