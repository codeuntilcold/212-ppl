/* STUDENT ID : 1915540 */



grammar BKOOL;

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


options{
	language=Python3;
}

program  
    : classdecl+ EOF
    ;

// SYNTAX
classdecl
    : CLASS ID LP memberlist RP 
    | CLASS ID EXTENDS ID LP memberlist RP 
    ;
memberlist
    : member memberlist
    |
    ;
member
    : attribute 
    | method 
    ;

attribute
    : mutableattribute 
    | immutableattribute 
    ;
mutableattribute
    : STATIC typedecl attributes SEMI 
    | typedecl attributes SEMI
    ;
immutableattribute
    : FINAL STATIC typedecl attributes SEMI 
    | STATIC FINAL typedecl attributes SEMI 
    | FINAL typedecl attributes SEMI 
    ;
attributes
    : ID INITOP exp COMMA attributes 
    | ID COMMA attributes 
    | ID INITOP exp 
    | ID
    ;

method
    : STATIC typedecl ID LB paramlist RB blockstatement 
    | typedecl ID LB paramlist RB blockstatement 
    | ID LB paramlist RB blockstatement 
    ;
paramlist
    : params
    |
    ;
params
    : param SEMI params
    | param
    ;  
param
    : typedecl ids
    ;
ids
    : ID COMMA ids 
    | ID
    ;
             
                
typedecl
    : primitype 
    | arraytype 
    | classtype
    ;
primitype
    : INTTYPE | FLOATTYPE | BOOLTYPE | STRINGTYPE | VOIDTYPE 
    ;
arraytype
    : primitype LSB INTLIT RSB 
    | classtype LSB INTLIT RSB
    ;
classtype
    : ID
    ;

exp
    : exp1 COMPAREOP exp1 
    | exp1
    ;
exp1
    : exp2 EQOP exp2 
    | exp2
    ;
exp2
    : exp2 LOGICOP exp3 
    | exp3
    ;
exp3
    : exp3 AMOP exp4 
    | exp4
    ;
exp4
    : exp4 MDOP exp5 
    | exp5
    ;
exp5
    : exp5 CONCATOP exp6 
    | exp6
    ;
exp6
    : NOTOP exp6 
    | exp7
    ;
exp7
    : AMOP exp7 
    | exp8
    ;
exp8
    : exp9 (LSB exp RSB) 
    | exp9
    ;
exp9
    : exp9 DOT ID 
    | exp9 DOT ID LB explist RB 
    | exp10
    ;
exp10
    : NEW ID LB explist RB 
    | operands
    ;
explist
    : exps
    | 
    ;
exps
    : exp COMMA exps
    | exp
    ;
operands
    : ID 
    | THIS 
    | NIL 
    | INTLIT 
    | FLOATLIT 
    | BOOLLIT 
    | STRINGLIT 
    | LB exp RB 
    | arraylit 
    ;

blockstatement
    : LP vardecllist statementlist RP
    ;

vardecllist
    : vardecl SEMI vardecllist 
    | 
    ;
vardecl
    : mutablevar 
    | immutablevar 
    ;
mutablevar
    : typedecl variables
    ;
immutablevar
    :  FINAL typedecl variables 
    ; 
variables
    : ID INITOP exp COMMA variables 
    | ID            COMMA variables 
    | ID INITOP exp 
    | ID
    ; 

statementlist
    : statement statementlist 
    | 
    ;
statement
    : blockstatement 
    | assignstatement 
    | ifstatement 
    | forstatement 
    | breakstatement 
    | continuestatement 
    | returnstatement 
    | methodinvostatement 
    ;


assignstatement
    : localvar ASSIGNOP exp SEMI 
    | THIS DOT ID ASSIGNOP exp SEMI
    | eleofarray ASSIGNOP exp SEMI 
    | mutableattr ASSIGNOP exp SEMI
    ; 
mutableattr
    : exp DOT ID 
    ;
localvar
    : ID
    ;
eleofarray
    : exp LSB exp RSB
    ;

ifstatement
    : IF exp THEN statement 
    | IF exp THEN statement ELSE statement
    ;
forstatement
    : FOR ID ASSIGNOP exp TO exp DO statement 
    | FOR ID ASSIGNOP exp DOWNTO exp DO statement 
    ;
breakstatement
    : BREAK SEMI
    ;
continuestatement
    : CONTINUE SEMI
    ;
returnstatement
    : RETURN exp SEMI
    ;
methodinvostatement
    : exp DOT ID LB explist RB SEMI
    ;

// array literal
arraylit
    : LP arraylitlist RP
    ;
arraylitlist
    : arrayintlit 
    | arrayfloatlit 
    | arraystringlit 
    | arrayboolit
    ; 
arrayintlit
    : INTLIT COMMA arraylitlist 
    | INTLIT
    ;
arrayfloatlit
    : FLOATLIT COMMA arraylitlist 
    | FLOATLIT
    ;
arraystringlit
    : STRINGLIT COMMA arraylitlist 
    | STRINGLIT
    ;
arrayboolit
    : BOOLLIT COMMA arraylitlist 
    | BOOLLIT
    ;


// LEXER TOKEN WORD
RETURN: 'return';
CONTINUE: 'continue';
BREAK: 'break';
DO: 'do';
TO: 'to';
DOWNTO: 'downto';
INTTYPE: 'int';
FLOATTYPE: 'float';
VOIDTYPE: 'void';
BOOLTYPE: 'boolean';
STRINGTYPE: 'string';
CLASS: 'class';
EXTENDS: 'extends';
STATIC: 'static';
FINAL : 'final';
NEW: 'new'; 
THIS: 'this';
NIL: 'nil';
IF: 'if';
THEN: 'then';
ELSE: 'else';
FOR :'for';
BOOLLIT: 'true' | 'false';


SEMI: ';';
COLON: ':';
DOT: '.';
COMMA: ',';
LSB: '[';
RSB: ']';
LB: '(' ;
RB: ')' ;
LP: '{';
RP: '}';


COMPAREOP:(LESSTHANOP | GREATERTHANOP |LESSTHANEQOP | GREATERTHANOPEQ);
EQOP: (EQUALOP | NOTEQOP);
LOGICOP: (ANDOP | OROP);
AMOP: (ADDOP | MINUSOP);
MDOP: (MULOP | DIVOP | FLOATDIVOP | MODULUSOP);

ADDOP: '+';
MULOP: '*';
DIVOP: '\\';
NOTEQOP: '!=';
INITOP: '=';
LESSTHANOP: '<';
LESSTHANEQOP: '<=';
OROP: '||';
NOTOP: '!';
MINUSOP: '-';
FLOATDIVOP: '/';
MODULUSOP: '%';
EQUALOP: '==';
GREATERTHANOP: '>';
GREATERTHANOPEQ: '>=';
ANDOP: '&&';
CONCATOP: '^';
ASSIGNOP: ':=';                                    



ID: [a-zA-Z_] [a-zA-Z0-9_]* ;

INTLIT: [0-9]+;
FLOATLIT: INTLIT ('.' | '.' INTLIT  | '.' INTLIT? ('e'|'E') ('+'|'-')? INTLIT | ('e'|'E') ('+'|'-')? INTLIT ) ;
STRINGLIT: '"' STR_CHAR* '"';

UNCLOSE_STRING
    : '"' STR_CHAR* EOF { raise UncloseString(self.text) }
    | '"' STR_CHAR* '\n' {  raise UncloseString(self.text[:-1]) }
    ;
ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESC_ILLEGAL { raise IllegalEscape(self.text) }
    ;

fragment STR_CHAR:  ~[\n"\\] | ESC_SEQ;
fragment ESC_SEQ: '\\' [bfrnt"\\] ;
fragment ESC_ILLEGAL:'\\' ~[bfrnt"\\] | '\\';


WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines
COMMENT: ('/*' .*? '*/' | '#' ~[\n\r]*) -> skip;

ERROR_CHAR: . { raise ErrorToken(self.text) };
