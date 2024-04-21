from antlr4.error.ErrorListener import ErrorListener

class JanderErrorListener(ErrorListener):
    def __init__(self, output_archive) -> None:
        self.output_archive = output_archive
        super().__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        #Vendo se é colchete ou aspas duplas o primeiro caractere do token 
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