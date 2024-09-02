import sys
from antlr4 import *
from antlr4.error.ErrorListener import ProxyErrorListener
from JanderLexer import JanderLexer
from JanderParser import JanderParser
#Importanto error listener customizado
#para poder ter mensagens de erro customizadas
from JanderErrorListener import * 
#Importanto classe de vocabulary para poder 
#saber o nome de um tipo de token
from Vocabulary import Vocabulary
from VisitorInterp import VisitorInterp

#Arrumando input caso esteja pra Windows e não linux
archive_input = sys.argv[1].replace('\\', '/')
archive_output = sys.argv[2].replace('\\', '/')

# Caso esteja usando linux
# archive_input = sys.argv[1]
# archive_output = sys.argv[2]


#Criando input_string como utf-8 pra não dar problema com acentos
input_string = FileStream(archive_input, 'utf-8')
lexer = JanderLexer(input_string)
stream = CommonTokenStream(lexer)
parser = JanderParser(stream)

vocab = Vocabulary(lexer)
with open(archive_output, 'w') as out:

    #Removendo errorlisteners padrões para que não haja mensagem no console
    #apenas no arquivo de saída para que esteja exatamente como o output esperado
    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    lexer.addErrorListener(ProxyErrorListener([JanderLexerErrorListener(out)]))
    parser.addErrorListener(ProxyErrorListener([JanderParserErrorListener(out)]))

    tree = parser.programa()

    if parser.getNumberOfSyntaxErrors() > 0:
        out.write("syntax errors")
    else:
        vinterp = VisitorInterp(tree, lexer, out)
        vinterp.visitPrograma()

    out.write('Fim da compilacao\n')
    

    Token.type


