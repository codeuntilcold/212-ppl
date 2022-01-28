/*
	PRINCIPLE OF PROGRAMMING LANGUAGES, CSE	HCMUT
	ASSIGNMENT 1
	STUDENT ID: 1910101

 */

grammar D96;

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
    else:
        return result;
}

options {
	language = Python3;
}


// LTT ORDER: program

program
	: classDecl+ EOF
	;

classDecl
	: CLASS ID LCB memDecl* RCB
	| CLASS ID COLON ID LCB memDecl* RCB
	;

memDecl
	: attrDecl
	| methodDecl
	; 

attrDecl
	: (VAL | VAR) (attrList | attrListInit) SEMI
	;

attrList
	: MEM_ID (COMMA MEM_ID)* COLON typeDecl
	;

attrListInit
	: MEM_ID COMMA (attrListInit) COMMA expr
	| MEM_ID COLON typeDecl ASSIGNOP expr
	;

methodDecl
	: MEM_ID LP paramList? RP blockStat
	| CONSTRUCTOR LP paramList? RP blockStat
	| DESTRUCTOR LP RP blockStat
	;

paramList
	: ID COLON typeDecl (SEMI ID COLON typeDecl)*
	;

blockStat
	: LCB stat* RCB
	;

//
// 		EXPRESSION
//

expr
	: expr1 ( CONCAT | STRCOMP ) expr1 | expr1
	;
expr1
	: expr2 ( EQ | NE | GT | LT | GTE | LTE ) expr2 | expr2
	;
expr2
	: expr2 ( AND | OR ) expr3 | expr3
	;
expr3
	: expr3 ( ADDOP | SUBOP ) expr4 | expr4
	;
expr4
	: expr4 ( MULOP | DIVOP | MODOP ) expr5 | expr5
	;
expr5
	: NOT expr5 | expr6
	;
expr6
	: SUBOP expr6 | expr7
	;
expr7
	: expr7 (LSB expr RSB) | expr8					// is this true ?
	;
expr8
	: expr8 INSACC ID (LP argList? RP)?
	| ID STATICACC STATIC_ID (LP argList? RP)?
	| expr9
	;
expr9
	: NEW ID LP argList? RP | operand
	;
operand
	: LP expr RP 
	| ID (LP argList? RP)?							// function call
	| NULL | SELF
	| INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | arrayLit
	// and user-defined objects ?
	// and data from function calls ?
	;

//
//		STATEMENT
//

stat
	: declStat
	| assignStat
	| ifStat
	| forStat
	| BREAK SEMI
	| CONTINUE SEMI
	| RETURN expr? SEMI				// chaams hoir
	| methodCall
	| blockStat
	;

declStat
	: varDecl SEMI
	;
varDecl
	: (VAL | VAR) (varList | varListInit) 
	;
varList
	: ID (COMMA ID)* COLON typeDecl
	;
varListInit
	: ID COMMA varListInit COMMA expr
	| ID COLON typeDecl ASSIGNOP expr
	;

assignStat
	: scalarVar ASSIGNOP expr SEMI
	;
ifStat
	: IF LP expr RP blockStat (ELSEIF blockStat)* (ELSE blockStat)?
	;
forStat
	: FOREACH LP scalarVar IN expr UPTO expr (BY expr)? RP blockStat
	;
methodCall
	: expr8 SEMI
	;
scalarVar
	: expr7			// index expression?
	;









//
// 		TYPE AND LITERALS
//

typeDecl
	: BOOLTYPE
	| INTTYPE
	| FLOATTYPE
	| STRINGTYPE
	| ARRAY LSB typeDecl COMMA INTLIT RSB		// questionable
	// | ID									// user-defined class
	;

arrayLit
	: ARRAY LP (exprList | arrayList) RP
	;

exprList
	: expr (COMMA expr)*
	;

argList
	: exprList
	;

arrayList
	: arrayLit (COMMA arrayLit)*
	;

array_ele
	: MEM_ID LSB expr RSB
	;


//
// 		KEYWORDS
//

CLASS: 			'Class';
VAL: 			'Val';
VAR: 			'Var';
IF:				'If';
ELSE:			'Else';
ELSEIF:			'Elseif';
FOREACH:		'Foreach';
IN:				'In';
BY:				'By';

UPTO:			'..';

SELF:			'Self';
NEW:			'New';
BREAK:			'Break';
CONTINUE:		'Continue';
RETURN:			'Return';
CONSTRUCTOR:	'Constructor';
DESTRUCTOR:		'Destructor';
STRINGTYPE:		'String';
BOOLTYPE:		'Bool';
INTTYPE:		'Int';
FLOATTYPE:		'Float';

TRUE:			'True';
FALSE:			'False';
ARRAY:			'Array';
NULL:			'Null';

ADDOP: 			'+';
SUBOP: 			'-';
MULOP: 			'*';
DIVOP: 			'/';
MODOP: 			'%';

AND: 			'&&';
OR: 			'||';
NOT: 			'!';
EQ: 			'==';
NE: 			'!=';
LT: 			'<';
LTE: 			'<=';
GT: 			'>';
GTE: 			'>=';

CONCAT:	 		'+.';
STRCOMP:		'==.';

INSACC:			'.';
STATICACC:		'::';

ASSIGNOP: 		'=';


LP: '(';

RP: ')';

LCB: '{';

RCB: '}';

LSB: '[';

RSB: ']';

COMMA: ',';

COLON: ':';

SEMI: ';';

KEYWORD
	: BREAK | CONTINUE | IF | ELSEIF | ELSE | FOREACH | TRUE | FALSE
	| ARRAY | IN | INTTYPE | FLOATTYPE | BOOLTYPE | STRINGTYPE | RETURN
	| NULL | CLASS | VAL | VAR | CONSTRUCTOR | DESTRUCTOR | NEW | BY
	;

//
//		IDENTIFIERS
//

MEM_ID	
	: ID | STATIC_ID
	;
ID
	: [a-zA-Z_] [a-zA-Z0-9_]*
	;
STATIC_ID
	: '$' [a-zA-Z0-9_]+
	;

// ONLY ALLOW UNDERSCORES '_' BETWEEN DIGITS

fragment SIGN
	: [+-]?
	;
fragment OCT
	: [0] ([1-7][0-7_]* | [0])
	;
fragment HEX
	: [0][Xx] ([1-9A-F][0-9A-F_]* | [0])
	;
fragment BIN
	: [0][Bb] ([1][01_]* | [0])
	;
fragment DEC
	: [1-9][0-9_]* | [0]
	;
INTLIT
	: SIGN (OCT | HEX | BIN | DEC ) {self.text = self.text.replace('_','')}
	;


// UNDERSCORE BONANZA AGAIN
fragment EXP
	: [Ee] SIGN DEC
	;
FLOATLIT
	: (SIGN DEC)? '.' DEC EXP
	| SIGN DEC ('.' DEC?)? EXP
	| SIGN DEC '.' DEC EXP?
	;

BOOLLIT
	: TRUE | FALSE
	;

STRINGLIT
	: ["] (STR_ESC | .)*? ["]
	;

//
//		ERROR CATCHING ---------------------------------------- VERY WEIRD
//



UNCLOSE_STRING
	: ["] STR_CHAR* EOF {raise UncloseString(self.text[1:])}
	| ["] STR_CHAR* '\n' {raise UncloseString(self.text[1:-1])}
	;
ILLEGAL_ESCAPE
	: '"' STR_CHAR* ESC_ILLEGAL {raise IllegalEscape(self.text[1:-1])}
	;

fragment STR_CHAR
	: ~["\n\\] | STR_ESC
	;
fragment ESC_ILLEGAL
	: '\\' ~[bfrnt'\\] | '\\'
	;
fragment STR_ESC
	: '\\' [bfrnt'\\] | '\'"'
	;

COMMENT: '##' .*? '##' -> skip;			// skip to nearest comment signal

WS: [ \t\r\b\f\n]+ -> skip; 			// skip spaces, tabs, newlines

ERROR_CHAR
	: . {raise ErrorToken(self.text)}
	;