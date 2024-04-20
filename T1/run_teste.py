import sys

compare1, compare2 = sys.argv[1:3]

cont = 0

with open(compare1, 'r') as arc1, open(compare2, 'r') as arc2:
    for linha1, linha2 in zip(arc1, arc2):
        cont += 1
        for char1, char2 in zip(linha1, linha2):
            if char1 != char2:
                print("~~~~~~~~~~ERRO~~~~~~~~~~")
                print(compare1.split('/')[-1])
                print(cont)
                print(linha1, "!=", linha2)
                exit()

print("done")