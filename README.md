T1:
O antlr para Python está sendo usado, mas peço que não tente rodar de novo no T1 pois o lexer que ele gera possui um bug e por algum motivo é preciso importar uma função de error handling manualmente. 
O T1 está dentro na pasta T1, no arquivo "t1.py". Para rodar o programa, dê git clone neste repositório dentro do WSL, abra a pasta T1, e execute:

```bash
python3 t1.py <arquivo de entrada> <arquivo de saida>
```

Na pasta do T1 há também o programa "all_tests.py", que roda todos os arquivos de entrada do T1 no programa, e coloca o output do programa na pasta chamada saida, este programa também roda um outro programa que compara a saída gerada com as saídas esperadas que estão na pasta de casos de teste, para rodar o "all_tests.py" basta executar:

```bash
python3 all_tests.py
```

Tanto o "all_tests.py" quanto o "run_teste.py", que faz a comparação da saída com a saída esperada, estão comentados também, caso queira verificar que não estamos apenas copiando as saídas dos casos de teste
