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

program  : classdecl+  EOF;

// SYNTAX

classdecl: (CLASS ID LP memberlist RP) | (CLASS ID EXTENDS ID LP memberlist RP) ; // ok
memberlist: member memberlist | member | ;                              // ok
member: attribute | method ;                                                      // ok
attribute: mutableattribute | immutableattribute ;                                // ok
mutableattribute: STATIC typedecl attributelist SEMI | typedecl attributelist SEMI;   // ok 
immutableattribute: FINAL STATIC typedecl attributelist SEMI | STATIC FINAL typedecl attributelist SEMI | FINAL typedecl attributelist SEMI ;    // ok
attributelist: ID INITOP exp COMMA attributelist | ID COMMA attributelist | ID INITOP exp | ID;    // ok

method: STATIC typedecl ID LB paramlist RB blockstatement | typedecl ID LB paramlist RB blockstatement | ID LB paramlist RB blockstatement ; // ok
paramlist: param SEMI paramlistrest | param | ;  // ok
paramlistrest: param SEMI paramlistrest | param;  
param: typedecl idlist;                      // ok
idlist: ID COMMA idlist | ID;
             
                
typedecl: primitype | arraytype | classtype;
//typenotvoid: primitypenotvoid | arraytype | classtype;
primitype: INTTYPE | FLOATTYPE | BOOLTYPE | STRINGTYPE | VOIDTYPE ;
//primitypenotvoid: INTTYPE | FLOATTYPE | BOOLTYPE | STRINGTYPE ;
arraytype: arraytypename LSB INTLIT RSB ;
arraytypename: INTTYPE | FLOATTYPE | BOOLTYPE | STRINGTYPE | VOIDTYPE |ID;
classtype: ID;

exp: exp1 COMPAREOP exp1 | exp1;
exp1: exp2 EQOP exp2 | exp2;
exp2: exp2 LOGICOP exp3 | exp3;
exp3: exp3 AMOP exp4 | exp4;
exp4: exp4 MDOP exp5 | exp5;
exp5: exp5 CONCATOP exp6 | exp6;
exp6: NOTOP exp6 | exp7;
exp7: AMOP exp7 | exp8;
exp8: exp9 (LSB exp RSB) | exp9;
exp9: exp9 DOT ID | exp9 DOT ID LB explist RB | exp10;
exp10: NEW ID LB explist RB | operands;

explist: exp COMMA explistrest | exp | ;
explistrest: exp COMMA explistrest | exp;

operands: ID | THIS | NIL | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | LB exp RB | arraylit ;


// blockstatement: LP vardecl statementlist RP;  

// vardecl: var vardecl | var | ;
// var: mutablevar | immutablevar ;                                // ok
// mutablevar: typenotvoid varlist SEMI;   // ok 
// immutablevar: FINAL typenotvoid varlist SEMI  ;    // ok
// varlist: ID INITOP exp COMMA varlist | ID COMMA varlist | ID INITOP exp | ID;    // ok

// statementlist: statement statementlist | statement | ;


blockstatement: LP vardecllist statementlist RP;

vardecllist: vardecl SEMI vardecllist | vardecl SEMI | ;
vardecl: mutablevar | immutablevar ;
mutablevar: typedecl varlist;
immutablevar:  FINAL typedecl varlist ; 
varlist: ID INITOP exp COMMA varlist | ID COMMA varlist | ID INITOP exp | ID; 

statementlist: statement statementlist | statement | ;

statement: blockstatement | assignstatement | ifstatement | forstatement | breakstatement | continuestatement | returnstatement | methodinvostatement ;   // miss method invocation statement




assignstatement: localvar ASSIGNOP exp SEMI 
                | THIS DOT ID ASSIGNOP exp SEMI
                | eleofarray ASSIGNOP exp SEMI 
                | mutableattr  ASSIGNOP exp SEMI
                ; 

mutableattr: exp DOT ID ;
localvar: ID;
eleofarray: exp LSB exp RSB;

ifstatement: IF exp THEN statement | IF exp THEN statement ELSE statement;



forstatement: FOR ID ASSIGNOP exp TO exp DO statement | FOR ID ASSIGNOP exp DOWNTO exp DO statement ;

breakstatement: BREAK SEMI;

continuestatement: CONTINUE SEMI;

returnstatement: RETURN exp SEMI;

methodinvostatement: exp DOT ID LB explist RB SEMI;

// array literal
arraylit: LP arraylitlist RP;
arraylitlist: arrayintlit | arrayfloatlit | arraystringlit | arrayboolit; 
arrayintlit: INTLIT COMMA arraylitlist | INTLIT;
arrayfloatlit: FLOATLIT COMMA arraylitlist | FLOATLIT;
arraystringlit: STRINGLIT COMMA arraylitlist | STRINGLIT;
arrayboolit: BOOLLIT COMMA arraylitlist | BOOLLIT;


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

   //oke  

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
INITOP: '=';                               // not sure
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
ASSIGNOP: ':=';                                    // assign op
// MAIN: 'main';

KEYWORD: BOOLTYPE 
        | BREAK 
        | CLASS 
        | CONTINUE 
        | DO 
        | ELSE 
        | EXTENDS 
        | FLOATTYPE 
        | IF 
        | INTTYPE 
        | NEW 
        | STRINGTYPE 
        | THEN 
        | FOR 
        | RETURN 
        | BOOLLIT 
        | VOIDTYPE
        | NIL
        | THIS
        | FINAL
        | STATIC
        | TO
        | DOWNTO ;



ID: [a-zA-Z_] [a-zA-Z0-9_]* ;

INTLIT: [0-9]+;          // type integer
FLOATLIT: INTLIT ('.' | '.' INTLIT  | '.' INTLIT? ('e'|'E') ('+'|'-')? INTLIT | ('e'|'E') ('+'|'-')? INTLIT ) ;      // type float
                     // type boolean
STRINGLIT: '"' STR_CHAR* '"';                   // seem to be wrong, type string

// ARRAYTYPE: INTTYPE LSB INTSIZE RSB;
//INTSIZE: [1-9][0-9]*;
UNCLOSE_STRING:
	'"' STR_CHAR* EOF {
                raise UncloseString(self.text)
            }
        |
    '"' STR_CHAR* '\n' {
                raise UncloseString(self.text[:-1])
            }
        ;
ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESC_ILLEGAL {
                raise IllegalEscape(self.text)
            };



fragment STR_CHAR:  ~[\n"\\] | ESC_SEQ;
fragment ESC_SEQ: '\\' [bfrnt"\\] ;
fragment ESC_ILLEGAL:'\\' ~[bfrnt"\\] | '\\';


WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines

COMMENT: ('/*' (.)*? '*/' | '#' ~[\n\r]*) -> skip;   // oke




ERROR_CHAR: . {
		raise ErrorToken(self.text)
	};
