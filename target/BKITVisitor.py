# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#many_declaration.
    def visitMany_declaration(self, ctx:BKITParser.Many_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#global_var_declaration_part.
    def visitGlobal_var_declaration_part(self, ctx:BKITParser.Global_var_declaration_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_declaration.
    def visitVar_declaration(self, ctx:BKITParser.Var_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_list.
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_list_prime.
    def visitVar_list_prime(self, ctx:BKITParser.Var_list_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arrlit.
    def visitArrlit(self, ctx:BKITParser.ArrlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arrlitprime.
    def visitArrlitprime(self, ctx:BKITParser.ArrlitprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var.
    def visitVar(self, ctx:BKITParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable.
    def visitVariable(self, ctx:BKITParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dimensions.
    def visitDimensions(self, ctx:BKITParser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dimension.
    def visitDimension(self, ctx:BKITParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_declaration_part.
    def visitFunc_declaration_part(self, ctx:BKITParser.Func_declaration_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_declaration.
    def visitFunc_declaration(self, ctx:BKITParser.Func_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter.
    def visitParameter(self, ctx:BKITParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter_list.
    def visitParameter_list(self, ctx:BKITParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter_list_prime.
    def visitParameter_list_prime(self, ctx:BKITParser.Parameter_list_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body.
    def visitBody(self, ctx:BKITParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt_list.
    def visitStmt_list(self, ctx:BKITParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt.
    def visitStmt(self, ctx:BKITParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:BKITParser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#lhs.
    def visitLhs(self, ctx:BKITParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#elif_block.
    def visitElif_block(self, ctx:BKITParser.Elif_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#else_block.
    def visitElse_block(self, ctx:BKITParser.Else_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stmt.
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#doWhile_stmt.
    def visitDoWhile_stmt(self, ctx:BKITParser.DoWhile_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stmt.
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression_list.
    def visitExpression_list(self, ctx:BKITParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression_list_prime.
    def visitExpression_list_prime(self, ctx:BKITParser.Expression_list_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logical_exp.
    def visitLogical_exp(self, ctx:BKITParser.Logical_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_expr.
    def visitIndex_expr(self, ctx:BKITParser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_call.
    def visitFunction_call(self, ctx:BKITParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#not_exp.
    def visitNot_exp(self, ctx:BKITParser.Not_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#atomic.
    def visitAtomic(self, ctx:BKITParser.AtomicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#sign_exp.
    def visitSign_exp(self, ctx:BKITParser.Sign_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#relational_exp.
    def visitRelational_exp(self, ctx:BKITParser.Relational_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#multiplying_exp.
    def visitMultiplying_exp(self, ctx:BKITParser.Multiplying_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#sub_exp.
    def visitSub_exp(self, ctx:BKITParser.Sub_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#adding_exp.
    def visitAdding_exp(self, ctx:BKITParser.Adding_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_operator.
    def visitIndex_operator(self, ctx:BKITParser.Index_operatorContext):
        return self.visitChildren(ctx)



del BKITParser