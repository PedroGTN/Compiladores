from antlr4 import *
from JanderLexer import JanderLexer
import os
current_dir = os.path.dirname(__file__)

class Vocabulary():

    def getTypeName(self, type:int):
        return self.vocab_dict[type]
    
    
    def isToken(self, v):
        return v in self.vocab_dict.values()
    
    
    def get_key(self, val):
   
        for key, value in self.vocab_dict.items():
            if val == value:
                return key
    
        return 1000
    
    def add_key(self, name):
        self.vocab_dict[name] = name

    

    #Abre arquivo de tokens e coloca eles em um dicionário
    def __init__(self, Lexer):
        self.token_file = open(os.path.join(current_dir, Lexer.grammarFileName[:-2] + 'tokens'))
        # self.token_file = open(Lexer.grammarFileName[:-2] + 'tokens')
        self.file_lines = self.token_file.readlines()
        self.vocab_dict = dict()
        for i in range(len(self.file_lines)):
            line = self.file_lines[i].split('\'')

            if len(line) == 1:
                line = line[-1].split('=')
            else:
                line[-1] = line[-1][1:]

            self.vocab_dict[int(line[-1][:-1])] = line[-2]
        pass
