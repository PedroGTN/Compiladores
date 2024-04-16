import sys
from antlr4 import *
from Jander import Jander

archive_input, archive_out = sys.argv[1:]


input_string = FileStream(archive_input)
lexer = Jander(input_string)
t = lexer.nextToken()
while(t.type != Token.EOF):
    print("<", t.type ,",", t.text, ">")
    t = lexer.nextToken()

