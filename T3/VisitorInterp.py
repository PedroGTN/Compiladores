import sys
from antlr4 import *
from JanderLexer import JanderLexer
from JanderParser import JanderParser
from JanderListener import JanderListener
from Vocabulary import Vocabulary
from antlr4.tree.Tree import TerminalNodeImpl
import re

class VisitorInterp(JanderListener):
    def __init__(self, ctx:JanderParser.ProgramaContext, lexer:JanderLexer):
        self.vocab = Vocabulary(lexer)
        self.ctx = ctx
        self.dict = dict()
        JanderParser.ProgramaContext.start


    # Visitor que captura os numeros das linhas onde cada delaracao ocorre
    def visitPrograma(self):
        for i in range(self.ctx.getChildCount()):
            for j in range(self.ctx.getChild(i).getChildCount()):
                text = self.visitToken(self.ctx.getChild(i).getChild(j))
                print(re.sub('[0-9]', '', text))
                print(re.sub('[^0-9]', '', text))
                line = re.sub('[0-9]', '', text).split()
                line2 = re.sub('[^0-9]', '', text)
                if(line[0] == 'declare'):
                    for k in line[1:-2]:
                        self.dict[k] = line[-1]
                elif(line[1] == '<-'):
                    print("atribuicao")
        print(self.dict)
        return 
    
    # Retorna o nome de cada token visitado
    def getTokenName(self, token):
        if isinstance(token, TerminalNode):
            return (token.symbol.type)
        else:
            return 0

    # Visita cada token e se ele for um terminal volta ao nó pai 
    # para poder consultar a linha, visita recusivamente
    def visitToken(self, token):
        ret = self.getTokenName(token)

        if isinstance(token, TerminalNodeImpl):
            token_mesmo = token.getParent().start
            line = str(token_mesmo.line)
        else:
            line = '-1'
            
        if ret > 0:
            if self.vocab.getTypeName(ret) == 'IDENT':
                text = token.getText() + line + " "
            elif self.vocab.getTypeName(ret) == ',':
                text = ''
            else:
                text = self.vocab.getTypeName(ret) + line + " "
        else:
            text = ''
        if not isinstance(token, TerminalNode):
            for i in range(token.getChildCount()):
                text += self.visitToken(token.getChild(i))

        

        return text



    # def visitToken(self, ctx):
    #     for i in range(ctx.getChildCount()):
    #         text = ''

    #         for j in range(ctx.getChild(i).getChildCount()):
    #             child = ctx.getChild(i).getChild(j)
    #             if isinstance(child, TerminalNode):
    #                 print( self.vocab.getTypeName(child.symbol.type))

    #         for j in range(ctx.getChild(i).getChildCount()):
    #             child = ctx.getChild(i).getChild(j)
    #             for k in range(child.getChildCount()):
    #                 child_c = child.getChild(k)
    #                 if isinstance(child_c, TerminalNode):
    #                     print( self.vocab.getTypeName(child_c.symbol.type))
            
    #         for j in range(ctx.getChild(i).getChildCount()):
    #             child = ctx.getChild(i).getChild(j)
    #             for k in range(child.getChildCount()):
    #                 child_c = child.getChild(k)
    #                 for m in range(child.getChildCount()):
    #                     child_c_c = child_c.getChild(m)
    #                     if isinstance(child_c_c, TerminalNode):
    #                         print( self.vocab.getTypeName(child_c_c.symbol.type))

    #         for j in range(ctx.getChild(i).getChildCount()):
    #             newvar = ctx.getChild(i).getChild(j)
    #             if newvar.getChildCount():
    #                 for k in range(newvar.getChildCount()):
    #                     text += newvar.getChild(k).getText() + ' '
    #             else:    
    #                 text += newvar.getText() + ' '

    #         print(text, '\n')
        
    #     return