from email.errors import InvalidHeaderDefect


while(True):
    nome = input("Digite um nome: ")
    if nome == "*":
        break
    idade = input("Digite a idade: ")
    f = open('lista.txt', "a")
    f.write(f"{nome} : {idade}\n")
    f.close()

#    for line in f:
#        print(line.strip())