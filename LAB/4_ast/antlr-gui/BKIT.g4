grammar BKIT;

program: decl+ EOF;

cseltype: INT | FLOAT | BOOLEAN;

decl: vardecl decltail | constdecl decltail | funcdecl decltail;

decltail: vardecl decltail | constdecl decltail | funcdecl decltail | ; 

vardecl: LET single_vardecls SEMI;

single_vardecls: single_vardecl single_vardecltail;

single_vardecl: ID COLON cseltype;

single_vardecltail: COMMA single_vardecl single_vardecltail | ;

constdecl: CONST single_constdecl SEMI;

single_constdecl: ID COLON cseltype EQ expr;

expr: INTLIT | FLOATLIT | BOOLEANLIT;

funcdecl: FUNCTION ID LR paramlist RR SEMI;

paramlist: single_vardecls | ;

LET: 'Let';

CONST: 'Constant';

FUNCTION: 'Function';

SEMI: ';';

COLON: ':';

COMMA: ',';

LR: '(';

RR: ')';

EQ: '=';

INT: 'Int';

FLOAT: 'Float';

BOOLEAN: 'Boolean';

INTLIT: [0-9]+;

FLOATLIT: [0-9]+ '.' [0-9]+;

BOOLEANLIT: 'True' | 'False';

ID: [a-zA-Z]+;

WS: [ \t\r\n\f]+ -> skip;