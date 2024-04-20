import sys
from antlr4 import *
from Jander import Jander
from Vocabulary import Vocabulary

# PALAVRA_CHAVE=1
# SIMBOLO_RESERV=2
# NUMINT=3
# NUMREAL=4
# IDENT=5
# TEXT=6
# COMENTARIO=7
# WS=8

archive_input = sys.argv[1]
archive_output = sys.argv[2]


input_string = FileStream(archive_input)
lexer = Jander(input_string)
t = lexer.nextToken()
vocab = Vocabulary(lexer)
with open(archive_output, 'w') as out:
    while(t.type != Token.EOF):
        txt = '\'' + t.text + '\'' 
        match (t.type):
            case 6: 
                out.write("<" + txt + "," + vocab.getTypeName(t.type) + ">\n")
            case 5: 
                out.write("<" + txt + "," + vocab.getTypeName(t.type) + ">\n")
            case _:
                out.write("<" + txt + "," + txt + ">\n")
        
        t = lexer.nextToken()

