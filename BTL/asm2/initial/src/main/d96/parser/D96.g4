/*
	PRINCIPLE OF PROGRAMMING LANGUAGES, CSE	HCMUT
	ASSIGNMENT 1
	STUDENT ID: 1910101

 */

grammar D96;

@lexer::header {
from lexererr import *
}

@parser::members {
ZEROLIT_ARR = ['0', '00', '0b0', '0B0', '0x0', '0X0']
}

// @lexer::members {
// def emit(self):
//     tk = self.type
//     result = super().emit()
//     if tk == self.UNCLOSE_STRING:       
//         raise UncloseString(result.text)
//     elif tk == self.ILLEGAL_ESCAPE:
//         raise IllegalEscape(result.text)
//     elif tk == self.ERROR_CHAR:
//         raise ErrorToken(result.text)
//     else:
//         return result;
// }

options {
	language = Python3;
}


program
	: classDecls EOF
	;

classDecls
	: classDecl classDecls 
	| classDecl
	;

classDecl
	: CLASS ID 			LCB memDeclList RCB
	| CLASS ID COLON ID LCB memDeclList RCB
	;

memDeclList
	: memDecl memDeclList |
	;
memDecl
	: attrDecl
	| methodDecl
	; 

attrDecl
	: (VAL | VAR) (attrs | attrsInit) SEMI
	;
attrs
	: memIds COLON typeDecl
	;
memIds
	: memId COMMA memIds
	| memId
	;
attrsInit
	: memId COMMA attrsInit COMMA    expr
	| memId COLON typeDecl 	ASSIGNOP expr
	;

methodDecl
	: memId 		LP paramList RP blockStat
	| CONSTRUCTOR 	LP paramList RP blockStat
	| DESTRUCTOR 	LP 			 RP blockStat
	;
paramList
	: params |
	;
params
	: param SEMI params
	| param
	;
param
	: ids COLON typeDecl
	;

blockStat
	: LCB statList RCB
	;
statList
	: stat statList
	|
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
	: expr7 indexes
	| expr8
	;
indexes
	: LSB expr RSB indexes
	| LSB expr RSB
	;
expr8
	: expr8 DOT ID 
	| expr8 DOT ID LP argList RP	//function call
	| expr9
	;
expr9
	: ID DBCOLON STATIC_ID
	| ID DBCOLON STATIC_ID LP argList RP
	| expr10
	;
expr10
	: NEW ID LP argList RP | operand
	;
operand
	: LP expr RP 
	| ID						// variables (NOT ATTRIBUTES)
	| SELF
	| NULL 		| INTLIT 	| FLOATLIT 
	| BOOLLIT 	| STRINGLIT | arrayLit	//constants
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
	| RETURN SEMI				// chaams hoir
	| RETURN expr SEMI
	| methodCall
	| blockStat
	;

declStat
	: varDecl SEMI
	;
varDecl
	: (VAL | VAR) (variables | varsInit) 
	;
variables
	: ids COLON typeDecl
	;
ids
	: ID COMMA ids
	| ID
	;
varsInit
	: ID COMMA varsInit COMMA expr
	| ID COLON typeDecl ASSIGNOP expr
	;

assignStat				// does a = b = c holds ??????????
	: scalarVar ASSIGNOP expr SEMI
	| indexExpr ASSIGNOP expr SEMI
	;
ifStat
	: IF LP expr RP blockStat elseifList
	;
elseifList
	: ELSEIF LP expr RP blockStat elseifList
	| ELSE blockStat
	|
	;
forStat
	: FOREACH LP scalarVar IN expr DOTDOT expr RP blockStat
	| FOREACH LP scalarVar IN expr DOTDOT expr BY expr RP blockStat
	;
methodCall
	: expr8 DOT ID LP argList RP SEMI
	| ID DBCOLON STATIC_ID LP argList RP SEMI
	;
scalarVar
	: ID
	| expr8 DOT ID
	| ID DBCOLON STATIC_ID
	;
indexExpr
	: expr7 indexes
	;

//
// 		TYPE AND LITERALS
//

typeDecl
	: primitiveType
	| arrayType
	| ID // user-defined class
	;
arrayType
	: ARRAY LSB arrayType 	  COMMA {self.getCurrentToken().text not in self.ZEROLIT_ARR}? INTLIT RSB
	| ARRAY LSB primitiveType COMMA {self.getCurrentToken().text not in self.ZEROLIT_ARR}? INTLIT RSB
	;
primitiveType
	: BOOLTYPE
	| INTTYPE
	| FLOATTYPE
	| STRINGTYPE
	;

arrayLit
	: ARRAY LP exprList RP
	;
exprList
	: exprs |
	;
exprs
	: expr COMMA exprs
	| expr
	;

argList
	: exprs |
	;
memId
	: ID | STATIC_ID
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

DOTDOT:			'..';

SELF:			'Self';
NEW:			'New';
BREAK:			'Break';
CONTINUE:		'Continue';
RETURN:			'Return';
CONSTRUCTOR:	'Constructor';
DESTRUCTOR:		'Destructor';
STRINGTYPE:		'String';
BOOLTYPE:		'Boolean';
INTTYPE:		'Int';
FLOATTYPE:		'Float';

fragment TRUE:	'True';
fragment FALSE:	'False';
ARRAY:			'Array';
NULL:			'Null';

ADDOP: 			'+';
SUBOP: 			'-';
MULOP: 			'*';
DIVOP: 			'/';
MODOP: 			'%';

CONCAT:	 		'+.';
STRCOMP:		'==.';

AND: 			'&&';
OR: 			'||';
NOT: 			'!';
EQ: 			'==';
NE: 			'!=';
LT: 			'<';
LTE: 			'<=';
GT: 			'>';
GTE: 			'>=';


DOT:			'.';
DBCOLON:		'::';

ASSIGNOP: 		'=';


LP: 			'(';
RP: 			')';
LCB: 			'{';
RCB: 			'}';
LSB: 			'[';
RSB: 			']';
COMMA: 			',';
COLON: 			':';
SEMI: 			';';

// KEYWORD
// 	: BREAK | CONTINUE | IF | ELSEIF | ELSE | FOREACH | TRUE | FALSE
// 	| ARRAY | IN | INTTYPE | FLOATTYPE | BOOLTYPE | STRINGTYPE | RETURN
// 	| NULL | CLASS | VAL | VAR | CONSTRUCTOR | DESTRUCTOR | NEW | BY
// 	;

//
//		IDENTIFIERS
//

ID
	: [a-zA-Z_] [a-zA-Z0-9_]*
	;
STATIC_ID
	: '$' [a-zA-Z0-9_]+
	;

// ONLY ALLOW UNDERSCORES '_' BETWEEN DIGITS
fragment UNDR: [_];

fragment OCT
	: [0] [1-7] ([0-7] | UNDR[0-7])*
	;
fragment HEX
	: [0][Xx] [1-9A-F] ([0-9A-F] | UNDR[0-9A-F])* 
	;
fragment BIN
	: [0][Bb] [1] ([01] | UNDR[01])*
	;
fragment DEC
	: [1-9] ([0-9] | UNDR[0-9])* 
	;
INTLIT
	: ( OCT | HEX | BIN | DEC ) {self.text = self.text.replace('_','')}
	| ZEROLIT
	;
fragment ZEROLIT
	: [0]
	| [0][0]
	| [0][Xx][0]
	| [0][Bb][0]
	;

// UNDERSCORE BONANZA AGAIN
fragment INTPART
	: DEC | [0]
	;
fragment DECPART
	: DOT [0-9]*
	;
fragment EXPPART
	: [Ee] [+-]? [0-9]+
	;
FLOATLIT
	: (INTPART? DECPART EXPPART
	| INTPART DECPART? EXPPART
	| INTPART DECPART EXPPART?
	) {self.text = self.text.replace('_','')};

BOOLLIT
	: TRUE | FALSE
	;

STRINGLIT
	: (["] (STR_ESC | STR_CHAR)*? ["]) {self.text = self.text[1:-1]}
	;

//
//		ERROR CATCHING ---------------------------------------- VERY WEIRD
//



ILLEGAL_ESCAPE
	: ["] STR_CHAR*? ESC_ILLEGAL {raise IllegalEscape(self.text[1:])}
	;

UNCLOSE_STRING
	: ["] STR_CHAR*? EOF {raise UncloseString(self.text[1:])}
	| ["] STR_CHAR*? [\b\f\n\r\t\\] {raise UncloseString(self.text[1:-1])}
	;

fragment STR_CHAR
	: ~["\b\f\n\r\t\\] | STR_ESC
	;
fragment ESC_ILLEGAL
	: '\\' ~[bfrnt\\] | '\\'
	;
fragment STR_ESC
	: '\\' [bfrnt\\] | '\'"'
	;

COMMENT: '##' .*? '##' -> skip;			// skip to nearest comment signal

WS: [ \t\r\b\f\n]+ -> skip; 			// skip spaces, tabs, newlines

ERROR_CHAR
	: . {raise ErrorToken(self.text)}
	;