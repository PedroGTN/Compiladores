lexer grammar Jander;

PALAVRA_CHAVE : 'algoritmo' | 'declare' | 'fim_algoritmo' | 'leia' | 'escreva'
    ;
SIMBOLO_RESERV : ':'| '(' | ')' | ','
    ;
NUMINT	: ('+'|'-')?('0'..'9')+
	;
NUMREAL	: ('+'|'-')?('0'..'9')+ ('.' ('0'..'9')+)?
	;
IDENT : ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'0'..'9')*
	 ;

TEXT
    :   '"' .*? '"'
    ;

COMENTARIO
    :   '{' .*? '}' -> skip
    ;
WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n' 
        ) -> skip
    ;