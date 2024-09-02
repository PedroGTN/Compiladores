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
        self.funcdict = dict()
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
                
                text, text2 = self.visitToken(self.ctx.getChild(i).getChild(j))
                if debug>1:
                    print(text)
                line_split = []
 
                for k in text.split():
                    line_split.append(k.split('|'))
                line, line2 = map(list, zip(*line_split))
            
                self.analyzeLine(line, line2, text2.split())

        # print(self.dict)
        return 
    

    def arrumarlinhas(self, line, line2, line3):

        if debug>1:
            print("linha1|linha2",len(line), len(line2))
            print(line, '\n', line2)

        if line3:
            i = 0
            while(i < len(line)):
                if '"' in line[i]:
                    if line[i][-1] == '"':
                        break
                    j = i + 1
                    while(j < len(line)):
                        if '"' in line[j]:
                            break
                        j += 1
                    # print("outside", i, j, len(line))
                    for k in range(i, j):
                        # print("inside", i, j, len(line))
                        line[i] = line[i] + ' ' + line[i+1]
                        line.pop(i+1)

                i += 1            


        if debug>1:
            print("linha1|linha2",len(line), len(line2))
            print(line, '\n', line2)


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

        i = 0
        while(i < len(line)):
            if line[i] == '[':
                ind = line[i:].index(']')
                for j in range(i, i+ind+1):
                    line[i-1] += line[j]

                for j in range(i, i+ind+1):
                    line.pop(i)
                    line2.pop(i)
            else:
                i+=1

        return [line, line2]


    def analyzeLine(self, line, line2, line3):
        if len(line) < 2:
            return

        nl1 = self.arrumarlinhas(line, line2.copy(), False)
        nl2 = self.arrumarlinhas(line3, line2, True)


        if debug>1:
            print(line, '\n', line3)

        checkvar = 1
        checkfun = 1
        close_scope = 0

        
        line_dict = dict()
        for l in range(len(line)):
            line_dict[line[l]] = line2[l]

        if line[0] == 'constante':
            ind = line.index(':')
            for i in range(1, ind):
                self.dict.add(line[i], line[ind+1])
                self.dict.add('&' + line[i], '^'+line[ind+1])

        elif line[0] == 'procedimento':
            checkfun = 0
            self.dict.add(line[1], 'void')
            self.dict.change_scope(1)
            close_scope = 1

            if debug>0:
                print("procedimento")
                print(line)
            self.funcdict[line[1]] = []

            abrepar = line.index('(')
            fechapar = line.index(')')

            lineaz = line[abrepar+1 : fechapar].copy()
            flag = 1
            while ':' in lineaz:
                ind = lineaz.index(':')
                if lineaz[ind+1] in self.regdict.keys():
                    self.dict.add(lineaz[ind-1], lineaz[ind+1])
                    for r in self.regdict[lineaz[ind+1]]:
                        self.dict.add(lineaz[ind-1] + '.' + r[0], r[1])
                else:    
                    self.dict.add(lineaz[ind-1], lineaz[ind+1])
                self.funcdict[line[1]].append(lineaz[ind+1])
                lineaz.pop(ind)
            
            # self.funcdict[line[1]].append('void')

            fim_proced = line.index('fim_procedimento')
            last_line = line2[fechapar+1]
            last_ind = fechapar+1
            lines_list = []
            for i in range(fechapar+1, fim_proced):
                if(last_line != line2[i]):
                    lines_list.append([last_ind, i])
                    last_line = line2[i]
                    last_ind = i


            for k in lines_list:
                self.analyzeLine(line[k[0]:k[1]], line2[k[0]:k[1]], line3[k[0]:k[1]])


            if debug > 0:
                print("fdict",self.funcdict)
            
            for k in line:
                if k == 'retorne':
                    self.out.write('Linha ' + line_dict[k] + ': comando retorne nao permitido nesse escopo\n')
                    if debug:
                        print('Linha ' + line_dict[k] + ': comando retorne nao permitido nesse escopo\n')


        elif line[0] == 'funcao':
            checkfun = 0
            ind = line.index(')')
            self.dict.add(line[1], line[ind+2])

            self.dict.change_scope(1)
            close_scope = 1

            if debug:
                print("funcao")
                print(line)
            self.funcdict[line[1]] = []

            abrepar = line.index('(')
            fechapar = line.index(')')

            lineaz = line[abrepar+1 : fechapar].copy()
            flag = 1
            while ':' in lineaz:
                ind = lineaz.index(':')
                if lineaz[ind+1] in self.regdict.keys():
                    self.dict.add(lineaz[ind-1], lineaz[ind+1])
                    for r in self.regdict[lineaz[ind+1]]:
                        self.dict.add(lineaz[ind-1] + '.' + r[0], r[1])
                else:    
                    self.dict.add(lineaz[ind-1], lineaz[ind+1])
                self.funcdict[line[1]].append(lineaz[ind+1])
                lineaz.pop(ind)

            # self.funcdict[line[1]].append(line[fechapar+2])

            if debug > 0:
                print("fdict",self.funcdict)

        elif line[0] == 'tipo':
            checkvar = 0
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
            checkfun = 0
                # print("declaracao")
            if debug>1:
                print(line[-2])
            # print(line[-1])
            if line[-1] == 'fim_registro':
                checkvar = 0
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

            #se o penultimo item da linha for um ^ sabemos que é um ponteiro
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
            if self.dict.search(line[0]):
            # print("atribuicao")
            # print(line)
                if self.dict.search_text(line[0]) == 'logico':
                    for k in line[1:]:
                        # print(k)
                        if self.dict.search(k):
                            if self.dict.search_text(k) == 'literal':
                                self.out.write('Linha ' + line_dict[line[0]] +': atribuicao nao compativel para ' + line3[0] + '\n')
                                if debug:
                                    print('Linha ' + line_dict[line[0]] +': atribuicao nao compativel para ' + line3[0])
                else:
                    for k in line[1:]:
                        # print(k)
                        if self.dict.search(k):
                            if self.dict.search_text(k) !=  self.dict.search_text(line[0]) and not (self.dict.search_text(k) == 'inteiro' and self.dict.search_text(line[0]) == 'real'):
                                self.out.write('Linha ' + line_dict[line[0]] +': atribuicao nao compativel para ' + line3[0] + '\n')
                                if debug:
                                    print('Linha ' + line_dict[line[0]] +': atribuicao nao compativel para ' + line3[0])

        if(line[0] == 'se'):
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
                if debug:
                    print(line[lines_list[k]:lines_list[k+1]+1])
                self.analyzeLine(line[lines_list[k]:lines_list[k+1]+1], line2[lines_list[k]:lines_list[k+1]+1], line3[lines_list[k]:lines_list[k+1]+1])
        else:
            pilhaparam = []
            for i in range(len(line)):
                # print(k, self.vocab.isToken(k), k in self.dict.keys())
                if line[i] in self.funcdict.keys() and checkfun:

                    if len(pilhaparam):

                        if pilhaparam[-1][0] != self.dict.search_text(line[i]):
                            self.out.write('Linha ' + line_dict[line[i]] + ': incompatibilidade de parametros na chamada de ' + pilhaparam[-1][1]+ '\n')
                            if debug>0:
                                print('Linha ' + line_dict[line[i]] + ': wrong type of return of func ' + pilhaparam[-1][1] + '\n', line[i], self.dict.search_text(line[i]), pilhaparam[-1][0])
                        pilhaparam.pop(-1)

                    for k in self.funcdict[line[i]]:
                        pilhaparam.append([k, line[i], line_dict[line[i]]])

                elif len(pilhaparam):

                    if self.dict.search_text(line[i]) != 'NULL':
                        if pilhaparam[-1][0] != self.dict.search_text(line[i]):
                            self.out.write('Linha ' + line_dict[line[i]] + ': incompatibilidade de parametros na chamada de ' + pilhaparam[-1][1] + '\n')
                            if debug>0:
                                print('Linha ' + line_dict[line[i]] + ': wrong type of var ' + pilhaparam[-1][1] + '\n', line[i], self.dict.search_text(line[i]), pilhaparam)
    
                        pilhaparam.pop(-1)
            
                if not self.vocab.isToken(line[i]) and not self.dict.search(line[i]) and checkvar:
                    self.out.write('Linha ' + line_dict[line[i]] + ': identificador ' + line[i] + ' nao declarado\n')
                    if debug:
                        print('Linha ' + line_dict[line[i]] + ': identificador ' + line[i] + ' nao declarado')

                if line[i] == 'retorne' and checkfun:
                    self.out.write('Linha ' + line_dict[line[i]] + ': comando retorne nao permitido nesse escopo\n')
                    if debug:
                        print('Linha ' + line_dict[line[i]] + ': comando retorne nao permitido nesse escopo\n')


            if pilhaparam:
                self.out.write('Linha ' + pilhaparam[-1][2] + ': incompatibilidade de parametros na chamada de ' + pilhaparam[-1][1] + '\n')
                if debug>0:
                    print('Linha ' + pilhaparam[-1][2] + ': too little params ' + pilhaparam[-1][1] + '\n', line[i], self.dict.search_text(line[i]), pilhaparam)

            if close_scope:
                self.dict.change_scope(-1)

            if debug>0:
                print(pilhaparam)
                print("checkfun|checkvar", checkfun, checkvar)
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
                text2 = token.getText() + " "
            elif self.vocab.getTypeName(ret) == ',':
                text = ''
                text2 = ''
            else:
                text = self.vocab.getTypeName(ret) + '|' + line + " "
                text2 = token.getText() + " "
        else:
            text = ''
            text2 = ''
        if not isinstance(token, TerminalNode):
            for i in range(token.getChildCount()):
                text_final = self.visitToken(token.getChild(i))
                text += text_final[0]
                text2 += text_final[1]

        

        return [text,text2]


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