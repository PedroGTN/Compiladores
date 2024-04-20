import os

instances_path = "../casos-de-teste/1.casos_teste_t1"
output_path = "saida/"

if not os.path.exists(output_path):
        os.mkdir(output_path)

input_list = os.listdir(instances_path + '/entrada')

for file1 in input_list:
    command1 = 'python3 t1.py ' + instances_path + '/entrada/' + file1 
    command1 += ' ' + output_path + file1

    command2 = 'python3 run_teste.py ' + instances_path + '/saida/' + file1
    command2 += ' ' + output_path + file1

    os.system(str(command1))
    os.system(str(command2))

    #input("Press Enter to continue...")