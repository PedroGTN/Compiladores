import sys
from antlr4 import *
from antlr4.error.ErrorListener import ProxyErrorListener
from Jander import Jander 
#Importanto error listener customizado
#para poder ter mensagens de erro customizadas
from JanderErrorListener import JanderErrorListener 
#Importanto classe de vocabulary para poder 
#saber o nome de um tipo de token
from Vocabulary import Vocabulary

#Arrumando input caso esteja pra Windows e não linux
archive_input = sys.argv[1].replace('\\', '/')
archive_output = sys.argv[2].replace('\\', '/')

#Criando input_string como utf-8 pra não dar problema com acentos
input_string = FileStream(archive_input, 'utf-8')
lexer = Jander(input_string)


t = lexer.nextToken()
vocab = Vocabulary(lexer)
with open(archive_output, 'w') as out:

    #Removendo errorlisteners padrões para que não haja mensagem no console
    #apenas no arquivo de saída para que esteja exatamente como o output esperado
    lexer.removeErrorListeners()
    JanderErro = [JanderErrorListener(out)]
    lexer.addErrorListener(ProxyErrorListener(JanderErro))

    while(t.type != Token.EOF):
        txt = '\'' + t.text + '\'' 
        match (t.type):
            case 3: 
                out.write("<" + txt + "," + vocab.getTypeName(t.type) + ">\n")
            case 4: 
                out.write("<" + txt + "," + vocab.getTypeName(t.type) + ">\n")
            case 6: 
                out.write("<" + txt + "," + vocab.getTypeName(t.type) + ">\n")
            case 7: 
                out.write("<" + txt + "," + vocab.getTypeName(t.type) + ">\n")
            case _:
                out.write("<" + txt + "," + txt + ">\n")
        
        t = lexer.nextToken()
    


