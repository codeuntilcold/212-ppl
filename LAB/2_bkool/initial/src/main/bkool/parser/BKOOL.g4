grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

/*
 *	LAB 2
 */

////// BÀI 1

// program: (vardecl | funcdecl)+ EOF;
// or
// program: decls EOF;

// decls: decl decls | decl;

// decl: vardecl | funcdecl;

// vardecl: 'vardecl' ;

// funcdecl: 'funcdecl' ;

// WS: [ \t\r\n] -> skip;

// ERROR_CHAR: . {raise ErrorToken(self.text)};

////// BÀI 2

//// EBNF

// program: (vardecl | funcdecl)+ EOF;

// vardecl: TYPE idlist SEMI;

// funcdecl: TYPE ID paramdecl body;

// paramdecl: '(' paramlist? ')';

// paramlist: TYPE idlist (SEMI TYPE idlist)* ;

// idlist: ID (COMMA ID)*;

// body: 'body';

// TYPE: 'int' | 'float';

// ID: [a-zA-Z]+;

// COMMA: ',';

// SEMI: ';';

// WS: [ \t\r\n] -> skip;

// ERROR_CHAR: . {raise ErrorToken(self.text)};

//// BNF

// program: decls EOF;

// decls: decl decls | decl ;

// decl: vardecl | funcdecl;

// vardecl: TYPE idlist SEMI;

// funcdecl: TYPE ID paramdecl body;

// paramdecl: '(' (paramlist | ) ')';

// paramlist: param SEMI paramlist
// 	| param ;

// param: TYPE idlist ;

// idlist: ID COMMA idlist
// 	| ID;

// body: 'body';

// TYPE: 'int' | 'float';

// ID: [a-zA-Z]+;

// COMMA: ',';

// SEMI: ';';

// WS: [ \t\r\n] -> skip;

// ERROR_CHAR: . {raise ErrorToken(self.text)};

////// BÀI 3

// program : (vardecl | funcdecl)+ EOF;

// body: '{' (vardecl | stat)* '}';

// vardecl: TYPE idlist SEMI;

// funcdecl: TYPE ID paramdecl body;

// paramdecl: '(' paramlist? ')';

// paramlist: TYPE idlist (SEMI TYPE idlist)* ;

// stat: ID '=' expr SEMI
// 	| ID ('(' exprlist ')')? SEMI
// 	| 'return' expr SEMI;

// idlist: ID (COMMA ID)*;

// exprlist: expr (COMMA expr)*;

// expr: 'expr';

// TYPE: 'int' | 'float' ;

// ID: [a-zA-Z]+;

// COMMA: ',';

// SEMI: ';';

// WS: [ \t\r\n] -> skip;

// ERROR_CHAR: . {raise ErrorToken(self.text)};

////// BÀI 4

// program : (vardecl | funcdecl)+ EOF;

// body: '{' (vardecl | stat)* '}';



// vardecl: TYPE idlist SEMI;

// funcdecl: TYPE ID paramdecl body;

// paramdecl: '(' paramlist? ')';



// paramlist: TYPE idlist (SEMI TYPE idlist)* ;

// idlist: ID (COMMA ID)*;

// exprlist: expr (COMMA expr)*;



// stat: ID '=' expr SEMI
// 	| ID ('(' exprlist ')')? SEMI
// 	| 'return' expr SEMI;

// expr: '(' expr ')'
// 	| expr ('*' | '/') term		// left
// 	| term ('+') expr			// right
// 	| expr ('-') expr
// 	| term
// 	;

// term: INTLIT
// 	| FLOATLIT
// 	| ID ('(' exprlist ')')?
// 	;




// TYPE: 'int' | 'float' ;

// INTLIT: [0-9]+;

// fragment INTPART: [0-9]+;
// fragment FRACPART: [0-9]+;
// FLOATLIT: INTPART '.' FRACPART;

// ID: [a-zA-Z]+;

// COMMA: ',';

// SEMI: ';';

// WS: [ \t\r\n] -> skip;

// ERROR_CHAR: . {raise ErrorToken(self.text)};


