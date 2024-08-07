import sys
from antlr4 import *
from JanderLexer import JanderLexer
from JanderParser import JanderParser
from JanderListener import JanderListener
from Vocabulary import Vocabulary
from antlr4.tree.Tree import TerminalNodeImpl
import re

debug = 1


class VisitorInterp(JanderListener):
    def __init__(self, ctx:JanderParser.ProgramaContext, lexer:JanderLexer, out):
        self.vocab = Vocabulary(lexer)
        self.ctx = ctx
        self.dict = dict()
        self.dict["NUM_INT"] = {'type':'inteiro'}
        self.dict["NUM_REAL"] = {'type':'real'}
        self.dict["CADEIA"] = {'type':'literal'}
        self.dict['verdadeiro'] = {'type':'logico'}
        self.dict['falso'] = {'type':'logico'}


        # self.tipagem = {}
        # self.tipagem["NUM_INT"] = 'inteiro'
        # self.tipagem["NUM_REAL"] = 'real'
        # self.tipagem["CADEIA"] = 'literal'
        # self.tipagem['verdadeiro'] = 'logico'
        # self.tipagem['falso'] = 'logico'
        # self.tipagem['REGISTRO'] = 'registro'

        # self.scopo = dict()
        # self.scopo['global'] = {}

        self.out = out
        JanderParser.ProgramaContext.start


    # Visitor que captura os numeros das linhas onde cada delaracao ocorre
    def visitPrograma(self):
        for i in range(self.ctx.getChildCount()):
            for j in range(self.ctx.getChild(i).getChildCount()):
                
                text = self.visitToken(self.ctx.getChild(i).getChild(j))
                if debug:
                    print("AAAAAAAAAA\n")
                    print(text)
                line_split = []
                for k in text.split():
                    line_split.append(k.split('|'))
                line, line2 = map(list, zip(*line_split))
                # print(line)
                # print(line2)
                # print(re.sub('[0-9]', '', text))
                # print(re.sub('[^0-9]', '', text))
                # line = re.sub('[0-9]', '', text).split()
                # line2 = re.sub('[^0-9]', '', text)
            
                self.analyzeLine(line, line2)

        # print(self.dict)
        return 
    

    def analyzeLine(self, line, line2):
        print("dict comeco", self.dict)

        line_dict = dict()
        for l in range(len(line)):
            line_dict[line[l]] = line2[l]

        # print('linha', line_dict)

        if(line[0] == 'declare'):
                # print("declaracao")
            if not self.vocab.isToken(line[-1]):
                    self.out.write('Linha ' + line_dict[line[-1]] + ': tipo ' + line[-1] + ' nao declarado\n')
                    if debug:
                        print('Linha ' + line_dict[line[-1]] + ': tipo ' + line[-1] + ' nao declarado\n')
            for k in line[1:-2]:
                if k == ':':
                    continue
                if k in self.dict.keys():
                    self.out.write('Linha ' + line_dict[k] + ': identificador ' + k + ' ja declarado anteriormente\n')
                    if debug:
                        print('Linha ' + line_dict[k] + ': identificador ' + k + ' ja declarado anteriormente\n')
                else:
                    print("linha inteira", line)
                    if line[-2] == '^':
                        ponteiro = line[-2] + line[-1]
                        print("entrou ponteiro", ponteiro)
                        self.dict[k] = {"type":ponteiro}
                    else:
                        print('entrou variavel', line[-1])
                        self.dict[k] = {'type':line[-1]}
        else:
            for k in line:
                # print(k, self.vocab.isToken(k), k in self.dict.keys())
                if not self.vocab.isToken(k) and not k in self.dict.keys():
                    self.out.write('Linha ' + line_dict[k] + ': identificador ' + k + ' nao declarado\n')
                    if debug:
                        print('Linha ' + line_dict[k] + ': identificador ' + k + ' nao declarado')

        if(line[1] == '<-'):
            # print("atribuicao")
            print("linha inteira", line)
            # print(self.dict)
            print(self.dict[line[0]], line[0])
            print(line_dict)
            if self.dict[line[0]] == 'logico':
                for k in line[1:]:
                    # print(k)
                    if k in self.dict.keys():
                        print("aa")
                        if self.dict[k] == 'literal':
                            self.out.write('Linha ' + line_dict[line[0]] +': atribuicao nao compativel para ' + line[0] + '\n')
                            if debug:
                                print('Linha ' + line_dict[line[0]] +': atribuicao nao compativel para ' + line[0])

            # elif self.dict[line[0]][0] == '^':
            #     pass
            else:
                for k in line[1:]:
                    # print(k)
                    if k in self.dict.keys():
                        print('b', k)
                        print("bb", self.dict[k])
                        print("bbb", self.dict[line[0]])
                        print('bbbb', line[0])

                        if self.dict[k]['type'] !=  self.dict[line[0]]['type'] and not (self.dict[k]['type'] == 'inteiro' and self.dict[line[0]]['type'] == 'real'):
                            print('b', k)
                            print("bb", self.dict[k])
                            print("bbb", self.dict[line[0]])
                            print('bbbb', line[0])

                            self.out.write('Linha ' + line_dict[line[0]] +': atribuicao nao compativel para ' + line[0] + '\n')
                            if debug:
                                print('Linha ' + line_dict[line[0]] +': atribuicao nao compativel para ' + line[0])
                        # elif self.dict[k]['type'] == 
                        else:
                            self.dict[line[0]]['content'] = self.dict[k]['content']

        elif(line[0] == 'se'):
            lines_list = []
            for k in range(len(line)):
                if line[k] == 'senao' or line[k] == 'entao':    
                    lines_list.append(k-1)
                    lines_list.append(k+1)
                elif  line[k] == 'se':
                    lines_list.append(k+1)
                elif  line[k] == 'fim_se':
                    lines_list.append(k-1)
            for k in range(len(lines_list)-1):
                self.analyzeLine(line[lines_list[k]:lines_list[k+1]+1], line2[lines_list[k]:lines_list[k+1]+1])

        print('\n\n')



    # Retorna o nome de cada token visitado
    def getTokenName(self, token):
        if isinstance(token, TerminalNode):
            return (token.symbol.type)
        else:
            return 0

    # Visita cada token e se ele for um terminal volta ao nó pai 
    # para poder consultar a linha, visita recursivamente
    def visitToken(self, token):
        ret = self.getTokenName(token)

        if isinstance(token, TerminalNodeImpl):
            token_mesmo = token.getParent().start
            line = str(token_mesmo.line)
        else:
            line = '-1'
            
        if ret > 0:
            if self.vocab.getTypeName(ret) == 'IDENT':
                text = token.getText() + '|' + line + " "
            elif self.vocab.getTypeName(ret) == ',':
                text = ''
            else:
                text = self.vocab.getTypeName(ret) + '|' + line + " "
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