#!/bin/bash

diretorio="../casos-de-teste/1.casos_teste_t1"

lista_arquivos_entrada=("$diretorio/entrada"/*)
lista_arquivos_saida=("$diretorio/saida"/*)

for i in "${lista_arquivos_entrada[@]}"; do 
    echo "$i"
done