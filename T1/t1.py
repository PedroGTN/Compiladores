import sys
from antlr4 import *
from Jander import Jander
from Vocabulary import Vocabulary

archive_input = sys.argv[1]


input_string = FileStream(archive_input)
lexer = Jander(input_string)
t = lexer.nextToken()
vocab = Vocabulary(Jander)
while(t.type != Token.EOF):
    print("<" + vocab.getTypeName(t.type) + "," + t.text + ">")
    t = lexer.nextToken()

