from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return Program(ctx.many_declaration().accept(self))
    
    def visitMany_declaration(self,ctx:BKITParser.Many_declarationContext):
        if ctx.global_var_declaration_part():
            return ctx.global_var_declaration_part().accept(self) + ctx.func_declaration_part().accept(self)
        else:
            return ctx.func_declaration_part().accept(self)
    
    def visitGlobal_var_declaration_part(self,ctx:BKITParser.Global_var_declaration_partContext):
        if ctx.var_declaration():
            varDecNum = len(ctx.var_declaration())
            varDecList = []
            for i in range (varDecNum):
                varDecList.append(ctx.var_declaration(i).accept(self))
            varDecList = [item for sublist in varDecList for item in sublist]
            return varDecList
        return []
    
    def visitVar_declaration(self,ctx:BKITParser.Var_declarationContext):
        return ctx.var_list().accept(self)
    
    def visitVar_list(self,ctx:BKITParser.Var_listContext):
        if ctx.getChildCount() == 1:
            return ctx.var().accept(self)
        return [ctx.var().accept(self)] + ctx.var_list_prime().accept(self)
    
    def visitVar_list_prime(self,ctx:BKITParser.Var_list_primeContext):
        if ctx.getChildCount() != 0:
            return [ctx.var().accept(self)] + ctx.var_list_prime().accept(self)
        return []
        
    def visitVar(self,ctx:BKITParser.VarContext):
        if ctx.getChildCount() == 1:
            return VarDecl(*ctx.variable().accept(self), None)
        return VarDecl(*ctx.variable().accept(self),ctx.literal().accept(self))
    
    def visitVariable(self,ctx:BKITParser.VariableContext):
        return (Id(ctx.ID().getText()), ctx.dimensions().accept(self) )
    
    def visitDimensions(self,ctx:BKITParser.DimensionsContext):
        if ctx.getChildCount() == 2:
            return [ctx.dimension().accept(self)] + ctx.dimensions().accept(self)
        return []
    
    def visitDimension(self, ctx:BKITParser.DimensionContext):
        return IntLiteral(int(ctx.INTLIT().getText()))
    
    def visitLiteral(self,ctx:BKITParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText(),0))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText(),))
        elif ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText())
        elif ctx.arrlit():
            return ArrayLiteral(ctx.arrlit().accept(self))
        else:
            return StringLiteral(ctx.STRLIT().getText())
    
    def visitArrlit(self, ctx:BKITParser.ArrlitContext):
        if ctx.getChildCount() != 0:
            return [ctx.literal().accept(self)] + ctx.arrlitprime().accept(self)
    
    def visitArrlitprime(self, ctx:BKITParser.ArrlitprimeContext):
        if ctx.getChildCount() != 0:
            return [ctx.literal().accept(self)] + ctx.arrlitprime().accept(self)
        return []
    
    def visitFunc_declaration_part(self,ctx:BKITParser.Func_declaration_partContext):
        if ctx.func_declaration():
            size = len(ctx.func_declaration())
            res = []
            for i in range (size):
                res.append(ctx.func_declaration(i).accept(self))
            return res
        return []
    
    def visitFunc_declaration(self,ctx:BKITParser.Func_declarationContext):
        if ctx.parameter():
            return FuncDecl(Id(ctx.ID().getText()),ctx.parameter().accept(self),ctx.body().accept(self))
        return FuncDecl(Id(ctx.ID().getText()),[],ctx.body().accept(self))
    
    def visitParameter(self, ctx:BKITParser.ParameterContext):
        return ctx.parameter_list().accept(self)
    
    def visitParameter_list(self, ctx:BKITParser.Parameter_listContext):
        if ctx.parameter_list_prime():
            return [VarDecl(*ctx.variable().accept(self), None)] + ctx.parameter_list_prime().accept(self)
        return [VarDecl(*ctx.variable().accept(self), None)]
    
    def visitParameter_list_prime(self, ctx:BKITParser.Parameter_list_primeContext):
        if ctx.getChildCount() == 0:
            return []
        return [VarDecl(*ctx.variable().accept(self), None)] + ctx.parameter_list_prime().accept(self)
    
    def visitBody(self,ctx:BKITParser.BodyContext):
        return ctx.stmt_list().accept(self)
    
    def visitStmt_list(self, ctx:BKITParser.Stmt_listContext):
        varDecList = []
        stmtList = []
        if ctx.getChildCount() == 0:
            return ([],[])
        if ctx.var_declaration():
            varDecNum = len(ctx.var_declaration())
            for i in range (varDecNum):
                varDecList.append(ctx.var_declaration(i).accept(self))
            varDecList = [item for sublist in varDecList for item in sublist]
        if ctx.stmt():
            stmtListNum = len(ctx.stmt())
            for i in range (stmtListNum):
                stmtList.append(ctx.stmt(i).accept(self))
        return (varDecList,stmtList)

    def visitStmt(self, ctx:BKITParser.StmtContext):
        if ctx.assignment_stmt():
            return ctx.assignment_stmt().accept(self)
        if ctx.if_stmt():
            return ctx.if_stmt().accept(self)
        if ctx.for_stmt():
            return ctx.for_stmt().accept(self)
        if ctx.while_stmt():
            return ctx.while_stmt().accept(self)
        if ctx.doWhile_stmt():
            return ctx.doWhile_stmt().accept(self)
        if ctx.break_stmt():
            return ctx.break_stmt().accept(self)
        if ctx.continue_stmt():
            return ctx.continue_stmt().accept(self)
        if ctx.call_stmt():
            return ctx.call_stmt().accept(self)
        if ctx.return_stmt():
            return ctx.return_stmt().accept(self)
    
    def visitAssignment_stmt(self, ctx:BKITParser.Assignment_stmtContext):
        return Assign(ctx.lhs().accept(self),ctx.expression().accept(self))
    
    def visitLhs(self, ctx:BKITParser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return ArrayCell(ctx.expression().accept(self), ctx.index_operator().accept(self))
    
    def visitIf_stmt(self, ctx: BKITParser.If_stmtContext):
        return If( [(ctx.expression().accept(self),*ctx.stmt_list().accept(self))] + ctx.elif_block().accept(self), ctx.else_block().accept(self) )
    
    def visitElif_block(self, ctx: BKITParser.Elif_blockContext):
        if ctx.getChildCount() == 0:
            return []
        res = []
        size = len(ctx.ELSEIF())
        for i in range (size):
            res.append((ctx.expression(i).accept(self), *ctx.stmt_list(i).accept(self)))
        return res
    
    
    def visitElse_block(self, ctx: BKITParser.Else_blockContext):
        if ctx.getChildCount() == 0:
            return ([],[])
        return ctx.stmt_list().accept(self)
     
    def visitFor_stmt(self, ctx: BKITParser.For_stmtContext):
        return For(Id(ctx.ID().getText()), ctx.expression(0).accept(self), ctx.expression(1).accept(self), ctx.expression(2).accept(self), ctx.stmt_list().accept(self))
    
    def visitWhile_stmt(self, ctx: BKITParser.While_stmtContext):
        return While(ctx.expression().accept(self),ctx.stmt_list().accept(self))
    
    def visitDoWhile_stmt(self, ctx: BKITParser.DoWhile_stmtContext):
        return Dowhile(ctx.stmt_list().accept(self), ctx.expression().accept(self))
    
    def visitBreak_stmt(self, ctx: BKITParser.Break_stmtContext):
        return Break()
    
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return Continue()
    
    def visitCall_stmt(self, ctx: BKITParser.Call_stmtContext):
        return CallStmt(Id(ctx.ID().getText()),ctx.expression_list().accept(self))
    
    def visitReturn_stmt(self, ctx: BKITParser.Return_stmtContext):
        if ctx.expression():
            return Return(ctx.expression().accept(self))
        return Return(None)
    
    def visitExpression_list(self, ctx:BKITParser.Expression_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [ctx.expression().accept(self)] + ctx.expression_list_prime().accept(self)
    
    def visitExpression_list_prime(self, ctx:BKITParser.Expression_list_primeContext):
        if ctx.getChildCount() == 0:
            return []
        return [ctx.expression().accept(self)] + ctx.expression_list_prime().accept(self)
    
    def visitLogical_exp(self, ctx:BKITParser.Logical_expContext):
        return BinaryOp(ctx.LOGICALOP().getText(),ctx.expression(0).accept(self),ctx.expression(1).accept(self))

    def visitSub_exp(self, ctx:BKITParser.Sub_expContext):
        return ctx.expression().accept(self)
    
    def visitFunction_call(self, ctx:BKITParser.Function_callContext):
        return CallExpr(Id(ctx.ID().getText()),ctx.expression_list().accept(self))
    
    def visitSign_exp(self, ctx:BKITParser.Sign_expContext):
        return UnaryOp(ctx.SIGN().getText(), ctx.expression().accept(self))
    
    def visitNot_exp(self, ctx:BKITParser.Not_expContext):
        return UnaryOp(ctx.NOT().getText(), ctx.expression().accept(self))
    
    def visitMultiplying_exp(self, ctx:BKITParser.Multiplying_expContext):
        return BinaryOp(ctx.MULTIPLYINGOP().getText(), ctx.expression(0).accept(self),ctx.expression(1).accept(self))
    
    def visitAdding_exp(self, ctx:BKITParser.Adding_expContext):
        return BinaryOp(ctx.ADDINGOP().getText(), ctx.expression(0).accept(self),ctx.expression(1).accept(self))
    
    def visitRelational_exp(self, ctx:BKITParser.Relational_expContext):
        return BinaryOp(ctx.RELATIONALOP().getText(), ctx.expression(0).accept(self),ctx.expression(1).accept(self))
    
    def visitAtomic(self, ctx:BKITParser.AtomicContext):
        if ctx.ID():
            if len(ctx.dimensions().accept(self)) == 0:
                return Id(ctx.ID().getText())
            else:
                return ArrayCell(Id(ctx.ID().getText()),ctx.dimensions().accept(self))
        return ctx.literal().accept(self)
    
    def visitIndex_expr(self, ctx:BKITParser.Index_exprContext):
        return ArrayCell(ctx.expression().accept(self), ctx.index_operator().accept(self))
    
    def visitIndex_operator(self, ctx:BKITParser.Index_operatorContext):
        if ctx.index_operator():
            return [ctx.expression().accept(self)] + ctx.index_operator().accept(self)
        else:
            return [ctx.expression().accept(self)]