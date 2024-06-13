import os
current_dir = os.path.dirname(__file__)
os.chdir(current_dir)

instances_path = "../casos-de-teste/2.casos_teste_t2"
output_path = "saida/"

if not os.path.exists(output_path):
        os.mkdir(output_path)

input_list = os.listdir(instances_path + '/entrada')

for i in input_list:
    #comando para rodar o t2.py, onde ele coloca o path do arquivo de entrada 
    #e o do arquivo de saida
    command1 = 'python3 t2.py ' + instances_path + '/entrada/' + i 
    command1 += ' ' + output_path + i
    
    #comando para rodar o run_teste.py, onde ele coloca o path do  
    #arquivo de saida esperada e o do arquivo de saida gerado pelo t1.py
    command2 = 'python3 run_teste.py ' + instances_path + '/saida/' + i
    command2 += ' ' + output_path + i

#     print('\n' + str(command1))
    os.system(str(command1))
#     print('\n' + str(command2))
    os.system(str(command2))
    #input("\nAperte enter para continuar...")