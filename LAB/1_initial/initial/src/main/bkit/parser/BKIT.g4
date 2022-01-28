grammar BKIT;

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

program: 
    // IDENT 
    // IPADDR 
    // FLOAT
    // PASCAL_STRING
    PHPINT
    EOF ;

fragment DIGIT
    : [0-9]
    ;

// PASCAL IDENTIFIER
// IDENT
//     : [a-z][a-z0-9]* 
//     ;

// SIMPLE IP ADDRESS
fragment IPCOM
    : ([1-9][0-9]?[0-9]?|[0]) 
    ;
// IPADDR
//     : IPCOM '.' IPCOM '.' IPCOM '.' IPCOM 
//     ;

// PASCAL FLOAT
// FLOAT
//     : [\-]? DIGIT+ ('.'DIGIT+)? ('e' [\-]? DIGIT+)? 
//     ;

// PASCAL STRING
// PASCAL_STRING
//     :  '\'' ( ~['] | '\'\'' )* '\''
//     ;

// PHP INT
PHPINT
    : 
    ( [0] | [1-9][0-9_]* ) {
        if '_' in self.text:
            self.text = self.text.replace('_','')
    }
    ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;

