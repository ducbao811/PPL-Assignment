grammar BKIT;

// Student ID: 1852258

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

// PARSER
program: many_declaration EOF;

many_declaration
    : global_var_declaration_part func_declaration_part
    | func_declaration_part
    ;

// Global declaration part
global_var_declaration_part: var_declaration* ;
var_declaration: VAR COLON var_list SEMI;
var_list
    : var var_list_prime
    | var
    ;
var_list_prime
    : CM var var_list_prime
    |
    ;

literal: INTLIT | FLOATLIT | BOOLIT| STRLIT| arrlit ;

arrlit
    : LP literal arrlitprime RP
    | LP RP 
    ;
arrlitprime
    : CM literal arrlitprime
    |
    ;

var
    : variable '=' literal
    | variable
    ;
variable: ID dimensions;
dimensions
    : dimension dimensions
    | 
    ;
dimension: LS INTLIT RS ;

// Function declaration part

func_declaration_part: func_declaration* ;

    
func_declaration
    : FUNC COLON ID parameter body
    | FUNC COLON ID body
    ;
parameter: PARAM COLON parameter_list;
parameter_list
    : variable parameter_list_prime
    | variable
    ;
parameter_list_prime
    : CM variable parameter_list_prime
    |
    ;
body: BODY COLON stmt_list EBODY DOT;
stmt_list: (var_declaration)* (stmt)*;


////////////////////////////////////////////
////// Statement part

stmt
    : assignment_stmt
    | if_stmt
    | for_stmt
    | while_stmt
    | doWhile_stmt
    | break_stmt
    | continue_stmt
    | call_stmt
    | return_stmt
    ;

// Assignment
assignment_stmt: lhs '=' expression SEMI;
lhs
    : ID
    | expression index_operator
    ;

// If
if_stmt: IF expression THEN stmt_list elif_block else_block EIF DOT;
elif_block: (ELSEIF expression THEN stmt_list)* ;
else_block
    : ELSE stmt_list
    |
    ;

// For
for_stmt
    : FOR LB ID '=' expression CM expression CM expression RB DO stmt_list EFOR DOT;

// While
while_stmt: WHILE expression DO stmt_list EWHILE DOT ;

// Do while
doWhile_stmt: DO stmt_list WHILE expression ENDDO DOT ;

// Break
break_stmt: BREAK SEMI ;

// Continue 
continue_stmt: CONTI SEMI ;

// Call
call_stmt: ID LB expression_list RB SEMI ;

// Return
return_stmt
    : RETURN expression SEMI
    | RETURN SEMI
    ;

// Expresion part

expression_list
    : expression expression_list_prime
    | 
    ;
expression_list_prime
    : CM expression expression_list_prime
    |
    ;

RELATIONALOP: EQ | NEQ | LT | GT | LTE | GTE | NEQF | LTF | GTF | GTEF | LTEF ;
LOGICALOP: AND | OR ;
ADDINGOP: ADD | FADD | SUB | FSUB ;
MULTIPLYINGOP: MUL  | FMUL | DIV | FDIV | MOL;
SIGN: SUB | FSUB ;

expression
    : LB expression RB #sub_exp
    | ID LB expression_list RB #function_call
    | expression index_operator #index_expr
    | SIGN expression #sign_exp
    | NOT expression #not_exp
    | expression MULTIPLYINGOP expression #multiplying_exp
    | expression ADDINGOP expression #adding_exp
    | expression LOGICALOP expression #logical_exp
    | expression RELATIONALOP expression #relational_exp
    | literal #atomic
    | ID dimensions #atomic
    ;

index_operator
    : LS expression RS
    | LS expression RS index_operator
    ;

// LEXER

fragment Digit: [0-9] ;
fragment LowerLe: [a-z];
fragment UpperLe: [A-Z];

ID: LowerLe (LowerLe|UpperLe|'_'|Digit)* ;


// literal part

INTLIT:  [1-9]Digit* | '0'( [xX][1-9A-F](Digit|[A-F])* | [oO][1-7][0-7]* )? ;

FLOATLIT: Digit+ ('.' Digit* | ( [eE] (ADD | SUB)? Digit+ ) | '.' Digit* ( [eE] (ADD | SUB)? Digit+ ));

BOOLIT: TRUE | FALSE ;

STRLIT: '"' ('\\' [bfrnt'\\] | '\'' ["] | ~[\b\t\f\r\n\\"] )* '"' {self.text = self.text[1:-1]};



// Comment

COMMENT: '**' .*? '**' -> skip;

// Seperators

SEMI: ';' ;
COLON: ':' ;
LB: '(' ;
RB: ')' ;
LP: '{' ;
RP: '}' ;
LS: '[' ;
RS: ']' ;
DOT: '.' ;
CM: ',' ;




//Keyword
BODY: 'Body' ;
BREAK: 'Break';
CONTI: 'Continue' ;
DO: 'Do' ;
ELSE: 'Else' ;
ELSEIF: 'ElseIf' ;
EBODY: 'EndBody' ;
EIF: 'EndIf' ;
EFOR: 'EndFor' ;
EWHILE: 'EndWhile' ;
FOR: 'For' ;
FUNC: 'Function' ;
IF: 'If' ;
PARAM: 'Parameter' ;
RETURN: 'Return' ;
THEN: 'Then' ;
VAR: 'Var' ;
WHILE: 'While' ;
TRUE: 'True' ;
FALSE: 'False';
ENDDO: 'EndDo' ;



WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


// Operators

MUL : '*';
FMUL: MUL DOT;
DIV: '\\';
FDIV: DIV DOT;
ADD: '+';
FADD: ADD DOT;
SUB: '-';
FSUB: SUB DOT;
MOL: '%';
NOT: '!' ;
AND: '&&' ;
OR: '||' ;
EQ: '==' ;
NEQ: '!=' ;
LT: '<' ;
GT: '>' ;
LTE: '<=' ;
GTE: '>=' ;
NEQF: '=/=' ;
LTF: LT DOT ;
GTF: GT DOT ;
GTEF: GTE DOT ;
LTEF: LTE DOT;

UNCLOSE_STRING: '"' ([\\] [bfrnt'\\] | '\'' ["] | ~[\b\t\f\r\n\\"] )*{self.text = self.text[1:]};
ERROR_CHAR: .;
ILLEGAL_ESCAPE: '"' (~["\\])*([\\] ~[btnfr'\\]){self.text = self.text[1:]};
UNTERMINATED_COMMENT: '**' .*? ('*'~'*')?;