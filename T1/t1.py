import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener, ProxyErrorListener
from Jander import Jander
from Vocabulary import Vocabulary
from importlib import reload

#PALAVRA_CHAVE=1
#SIMBOLO_RESERV=2
#NUM_INT=3
#NUM_REAL=4
#MATH=5
#IDENT=6
#CADEIA=7
#COMENTARIO=8
#WS=9


#Linha 5: ~ - simbolo nao identificado

class JanderErrorListener(ErrorListener):
    def __init__(self, output_archive) -> None:
        self.output_archive = output_archive
        super().__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if(msg.split('\'')[1][0] == '\"'):
            self.output_archive.write("Linha " + str(line) + ': cadeia literal nao fechada')
        elif(msg.split('\'')[1][0] == '{'):
            self.output_archive.write("Linha " + str(line) + ': comentario nao fechado')
        else:
            self.output_archive.write("Linha " + str(line) + ': ' + str(msg.strip('\'')[-1]) + ' - simbolo nao identificado\n')
        exit()
    
    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print('Ambiguity')
        
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        print('AttemptingFullContext')

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print('ContextSensitivity')


archive_input = sys.argv[1].replace('\\', '/')
archive_output = sys.argv[2].replace('\\', '/')


input_string = FileStream(archive_input, 'utf-8')
lexer = Jander(input_string)



t = lexer.nextToken()
vocab = Vocabulary(lexer)
with open(archive_output, 'w') as out:
    lexer.removeErrorListeners()
    JanderErro = [JanderErrorListener(out)]
    lexer.addErrorListener(ProxyErrorListener(JanderErro))
    while(t.type != Token.EOF):
        txt = '\'' + t.text + '\'' 
        match (t.type):
            case 3: 
                out.write("<" + txt + "," + vocab.getTypeName(t.type) + ">\n")
            case 4: 
                out.write("<" + txt + "," + vocab.getTypeName(t.type) + ">\n")
            case 6: 
                out.write("<" + txt + "," + vocab.getTypeName(t.type) + ">\n")
            case 7: 
                out.write("<" + txt + "," + vocab.getTypeName(t.type) + ">\n")
            case _:
                out.write("<" + txt + "," + txt + ">\n")
        
        t = lexer.nextToken()
    


