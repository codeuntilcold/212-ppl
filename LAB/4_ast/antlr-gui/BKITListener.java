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
	 * Enter a parse tree produced by {@link BKITParser#cseltype}.
	 * @param ctx the parse tree
	 */
	void enterCseltype(BKITParser.CseltypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#cseltype}.
	 * @param ctx the parse tree
	 */
	void exitCseltype(BKITParser.CseltypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#decl}.
	 * @param ctx the parse tree
	 */
	void enterDecl(BKITParser.DeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#decl}.
	 * @param ctx the parse tree
	 */
	void exitDecl(BKITParser.DeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#decltail}.
	 * @param ctx the parse tree
	 */
	void enterDecltail(BKITParser.DecltailContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#decltail}.
	 * @param ctx the parse tree
	 */
	void exitDecltail(BKITParser.DecltailContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#vardecl}.
	 * @param ctx the parse tree
	 */
	void enterVardecl(BKITParser.VardeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#vardecl}.
	 * @param ctx the parse tree
	 */
	void exitVardecl(BKITParser.VardeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#single_vardecls}.
	 * @param ctx the parse tree
	 */
	void enterSingle_vardecls(BKITParser.Single_vardeclsContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#single_vardecls}.
	 * @param ctx the parse tree
	 */
	void exitSingle_vardecls(BKITParser.Single_vardeclsContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#single_vardecl}.
	 * @param ctx the parse tree
	 */
	void enterSingle_vardecl(BKITParser.Single_vardeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#single_vardecl}.
	 * @param ctx the parse tree
	 */
	void exitSingle_vardecl(BKITParser.Single_vardeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#single_vardecltail}.
	 * @param ctx the parse tree
	 */
	void enterSingle_vardecltail(BKITParser.Single_vardecltailContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#single_vardecltail}.
	 * @param ctx the parse tree
	 */
	void exitSingle_vardecltail(BKITParser.Single_vardecltailContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#constdecl}.
	 * @param ctx the parse tree
	 */
	void enterConstdecl(BKITParser.ConstdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#constdecl}.
	 * @param ctx the parse tree
	 */
	void exitConstdecl(BKITParser.ConstdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#single_constdecl}.
	 * @param ctx the parse tree
	 */
	void enterSingle_constdecl(BKITParser.Single_constdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#single_constdecl}.
	 * @param ctx the parse tree
	 */
	void exitSingle_constdecl(BKITParser.Single_constdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(BKITParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(BKITParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#funcdecl}.
	 * @param ctx the parse tree
	 */
	void enterFuncdecl(BKITParser.FuncdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#funcdecl}.
	 * @param ctx the parse tree
	 */
	void exitFuncdecl(BKITParser.FuncdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link BKITParser#paramlist}.
	 * @param ctx the parse tree
	 */
	void enterParamlist(BKITParser.ParamlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link BKITParser#paramlist}.
	 * @param ctx the parse tree
	 */
	void exitParamlist(BKITParser.ParamlistContext ctx);
}