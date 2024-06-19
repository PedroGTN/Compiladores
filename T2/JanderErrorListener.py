from antlr4.error.ErrorListener import ErrorListener

class JanderLexerErrorListener(ErrorListener):
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
    
    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print('Ambiguity')
        
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        print('AttemptingFullContext')

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print('ContextSensitivity')



class JanderParserErrorListener(ErrorListener):
    def __init__(self, output_archive) -> None:
        self.output_archive = output_archive
        super().__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if(offendingSymbol.type == 72):
            self.output_archive.write("Linha " + str(line) + ': ' + msg.split('\'')[1] + ' - simbolo nao identificado\n')
        elif(msg.split()[0] == 'missing'):
            self.output_archive.write("Linha " + str(line) + ': erro sintatico proximo a ' +  msg.split('\'')[-2].replace('<EOF>', 'EOF') + '\n')
        elif(msg.split()[0] == 'extraneous'):
            self.output_archive.write("Linha " + str(line) + ': erro sintatico proximo a ' +  msg.split('\'')[1] + '\n')
        elif(msg.split()[0] == 'mismatched'):
            if(msg.split('\'')[1][0] == '\"' and msg.split('\'')[1][-1] != '\"'):
                self.output_archive.write("Linha " + str(line) + ': cadeia literal nao fechada\n')
            elif(msg.split('\'')[1][0] == '{'):
                self.output_archive.write("Linha " + str(line) + ': comentario nao fechado\n')
            else:
                self.output_archive.write("Linha " + str(line) + ': erro sintatico proximo a ' +  msg.split('\'')[1] + '\n')
        elif(msg.split()[0] == 'no'):
            self.output_archive.write("Linha " + str(line) + ': erro sintatico proximo a ' +  msg.split('\'')[1][-1] + '\n')
        else:
            self.output_archive.write("Linha " + str(line) + ': ' +  msg + '\n')

        self.output_archive.write("Fim da compilacao\n")
        exit()

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print('Ambiguity')
        
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        print('AttemptingFullContext')

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print('ContextSensitivity')