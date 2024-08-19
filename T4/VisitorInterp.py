import sys
from antlr4 import *
from JanderLexer import JanderLexer
from JanderParser import JanderParser
from JanderListener import JanderListener
from Vocabulary import Vocabulary
from antlr4.tree.Tree import TerminalNodeImpl
import re
from scope_dict import Scope_Dict

debug = 0

class VisitorInterp(JanderListener):
    def __init__(self, ctx:JanderParser.ProgramaContext, lexer:JanderLexer, out):
        self.vocab = Vocabulary(lexer)
        self.ctx = ctx
        self.regdict = dict()
        self.dict = Scope_Dict()
        self.dict.add("NUM_INT", 'inteiro')
        self.dict.add("NUM_REAL", 'real')
        self.dict.add("CADEIA", 'literal')
        self.dict.add("verdadeiro", 'logico')
        self.dict.add("falso", 'logico')
        self.out = out
        JanderParser.ProgramaContext.start


    # Visitor que captura os numeros das linhas onde cada delaracao ocorre
    def visitPrograma(self):
        for i in range(self.ctx.getChildCount()):
            for j in range(self.ctx.getChild(i).getChildCount()):
                
                text = self.visitToken(self.ctx.getChild(i).getChild(j))
                if debug>1:
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
        i = 0
        while(i < len(line)):
            if line[i] == '^' or line[i] == '&':
                line[i+1] = line[i] + line[i+1]
                line.pop(i)
                line2.pop(i)
            else:
                i+=1

        i = 0
        while(i < len(line)):
            if line[i] == '.':
                line[i-1] = line[i-1] + line[i] + line[i+1]
                line.pop(i)
                line.pop(i)
                line2.pop(i)
                line2.pop(i)
            else:
                i+=1

        line_dict = dict()
        for l in range(len(line)):
            line_dict[line[l]] = line2[l]


        if line[0] == 'tipo':
            if debug>1:
                print("declaracao registro")
                print(line)
            self.vocab.add_key(line[1])
            self.dict.add(line[1], "registro")
            self.regdict[line[1]] = []
            ind = line.index(':')
            reglist = line[ind+2:]
            while ':' in reglist:
                dot = reglist.index(':')
                for l in reglist[:dot]:
                    self.regdict[line[1]].append([l, reglist[dot+1]])
                reglist = reglist[dot+2:]
            
            if debug>1:
                print(self.regdict[line[1]])
        elif line[0] == 'declare':
                # print("declaracao")
            if debug>1:
                print(line[-2])
            #se o penultimo item da linha for um ^ sabemos que é um ponteiro
            # print(line[-1])
            if line[-1] == 'fim_registro':
                ind = line.index(':')
                for k in line[1:ind]:
                    if self.dict.search(k):
                        self.out.write('Linha ' + line_dict[k] + ': identificador ' + k + ' ja declarado anteriormente\n')
                        if debug:
                            print('Linha ' + line_dict[k] + ': identificador ' + k + ' ja declarado anteriormente\n')
                    else:
                        self.dict.add(k, "registro")
                        reglist = line[ind+2:]
                        while ':' in reglist:
                            dot = reglist.index(':')
                            for r in reglist[:dot]:
                                self.dict.add(k + '.' + r, reglist[dot+1])
                            reglist = reglist[dot+2:]
                if debug>1:
                    self.dict.print()

            elif line[-1][0] == '^':
                self.vocab.add_key(line[-1]) #adicionando o tipo ponteiro ao dicionário

                for k in line[1:-2]:
                    if self.dict.search(k):
                        self.out.write('Linha ' + line_dict[k] + ': identificador ' + k + ' ja declarado anteriormente\n')
                        if debug:
                            print('Linha ' + line_dict[k] + ': identificador ' + k + ' ja declarado anteriormente\n')
                    else:
                        self.dict.add(k, line[-1])
                        self.dict.add('^'+k, line[-1][1:])
                
                if debug>0:
                    print("ponteiro")

            elif line[-1] in self.regdict.keys():
                if not self.vocab.isToken(line[-1]):
                        self.out.write('Linha ' + line_dict[line[-1]] + ': tipo ' + line[-1] + ' nao declarado\n')
                        if debug:
                            print('Linha ' + line_dict[line[-1]] + ': tipo ' + line[-1] + ' nao declarado\n')
                for k in line[1:-2]:
                    if self.dict.search(k):
                        self.out.write('Linha ' + line_dict[k] + ': identificador ' + k + ' ja declarado anteriormente\n')
                        if debug:
                            print('Linha ' + line_dict[k] + ': identificador ' + k + ' ja declarado anteriormente\n')
                    else:
                        self.dict.add(k, line[-1])
                        for r in self.regdict[line[-1]]:
                            self.dict.add(k + '.' + r[0], r[1])
                if debug>0:
                    self.dict.print()            
            else:
                if not self.vocab.isToken(line[-1]):
                        self.out.write('Linha ' + line_dict[line[-1]] + ': tipo ' + line[-1] + ' nao declarado\n')
                        if debug:
                            print('Linha ' + line_dict[line[-1]] + ': tipo ' + line[-1] + ' nao declarado\n')
                for k in line[1:-2]:
                    if self.dict.search(k):
                        self.out.write('Linha ' + line_dict[k] + ': identificador ' + k + ' ja declarado anteriormente\n')
                        if debug:
                            print('Linha ' + line_dict[k] + ': identificador ' + k + ' ja declarado anteriormente\n')
                    else:
                        self.dict.add(k, line[-1])
                        self.dict.add('&' + k, '^'+line[-1])
        elif(line[1] == '<-'):
            # print("atribuicao")
            # print(line)
            if self.dict.search_text(line[0]) == 'logico':
                for k in line[1:]:
                    # print(k)
                    if self.dict.search(k):
                        if self.dict[k] == 'literal':
                            self.out.write('Linha ' + line_dict[line[0]] +': atribuicao nao compativel para ' + line[0] + '\n')
                            if debug:
                                print('Linha ' + line_dict[line[0]] +': atribuicao nao compativel para ' + line[0])
            else:
                for k in line[1:]:
                    # print(k)
                    if self.dict.search(k):
                        if self.dict.search_text(k) !=  self.dict.search_text(line[0]) and not (self.dict.search_text(k) == 'inteiro' and self.dict.search_text(line[0]) == 'real'):
                            self.out.write('Linha ' + line_dict[line[0]] +': atribuicao nao compativel para ' + line[0] + '\n')
                            if debug:
                                print('Linha ' + line_dict[line[0]] +': atribuicao nao compativel para ' + line[0])

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
                print(line[lines_list[k]:lines_list[k+1]+1])
                self.analyzeLine(line[lines_list[k]:lines_list[k+1]+1], line2[lines_list[k]:lines_list[k+1]+1])
        else:
            for k in line:
                # print(k, self.vocab.isToken(k), k in self.dict.keys())
                if not self.vocab.isToken(k) and not self.dict.search(k):
                    self.out.write('Linha ' + line_dict[k] + ': identificador ' + k + ' nao declarado\n')
                    if debug:
                        print('Linha ' + line_dict[k] + ': identificador ' + k + ' nao declarado')
            if debug>1:
                print(line)

        



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