lexer grammar Jander;

PALAVRA_CHAVE : 'algoritmo' | 'declare' | 'fim_algoritmo' | 
                'leia' | 'escreva' | 'literal' | 'inteiro' | 
                'real' | 'logico' | 'e' | 'ou' | 'nao' | 
                'se' | 'entao' | 'senao' | 'fim_se' | 'caso' |
                'seja' | 'fim_caso' | 'para' | 'ate' | 'faca' | 
                'fim_para' | 'enquanto' | 'fim_enquanto' |
                'registro' | 'fim_registro' | 'tipo' |
                'procedimento' | 'fim_procedimento' | 'var' |
                'funcao' | 'fim_funcao' | 'retorne' | 'constante'
    ;

SIMBOLO_RESERV : ':'| '(' | ')' | ',' | '..' |
                 '<-' | '^' | '&' | '.' | '[' |
                 ']'
    ;

NUM_INT	: ('0'..'9')+
	;

NUM_REAL	: ('0'..'9')+ ('.' ('0'..'9')+)?
	;

MATH : '+' | '/' | '*' | '%' | '-' | '<' | '>' | '<=' |
         '>=' | '=' | '<>' | 'falso' | 'verdadeiro'
    ;

IDENT : ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*
	 ;


CADEIA
    :   '"' ~('\n'|'\r')*? '"'
    ;

COMENTARIO
    :   '{' ~('\n'|'\r')*? '}' -> skip
    ;

WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n' 
        ) -> skip
    ;

ERROR
    :   ( ('"' ~('"')*? ('\n'|'\r'))  |  ('{' ~('}')*? ('\n'|'\r')) ) {self.notifyListeners(LexerNoViableAltException(self, input, 0, None))}
    ;
