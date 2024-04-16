from antlr4 import *
from Jander import Jander

class Vocabulary():

    def getTypeName(self, type:int):
        return self.vocab_dict[type]

    def __init__(self, Lexer):
        self.token_file = open(Lexer.grammarFileName[:-2] + 'tokens')
        self.file_lines = self.token_file.readlines()
        self.vocab_dict = dict()
        for i in range(len(self.file_lines)):
            line = self.file_lines[i].split('=')
            self.vocab_dict[int(line[1][:-1])] = line[0]
        pass
