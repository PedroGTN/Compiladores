from antlr4 import *
from JanderLexer import JanderLexer
import os
current_dir = os.path.dirname(__file__)

class Vocabulary():

    def getTypeName(self, type:int):
        return self.vocab_dict[type]

    #Abre arquivo de tokens e coloca eles em um dicionário
    def __init__(self, Lexer):
        self.token_file = open(os.path.join(current_dir, Lexer.grammarFileName[:-2] + 'tokens'))
        # self.token_file = open(Lexer.grammarFileName[:-2] + 'tokens')
        self.file_lines = self.token_file.readlines()
        self.vocab_dict = dict()
        for i in range(len(self.file_lines)):
            if(self.file_lines[i][0] == '\''):
                break
            line = self.file_lines[i].split('=')
            self.vocab_dict[int(line[1][:-1])] = line[0]
        pass
