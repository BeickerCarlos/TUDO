f = open('lista.txt')

for line in f:
    dados = line.strip()
    resultado = dados.split(":")
    #nome = resultado[0]
    #idade = resultado[1]
    nome, idade = resultado
    print(f"nome: {nome}\nidade: {idade}")

f.close()