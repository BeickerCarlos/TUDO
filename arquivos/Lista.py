from os import popen, remove


menutexto = """
Lista de Alunos

1- adicionar aluno
2- Listar aluno
3- remover aluno
4- sair
"""
def menu():
    print(menutexto)
Lista_Alunos = []
while(True):
    menu()
    opcao = input("Qual é a opção? ")
    if opcao == "1":
        nome = input("Qual é o nome do aluno para adicionar? ")
        Lista_Alunos.append(nome)
        print(f"o {nome} foi adicionado")
        f = open("lista.txt","a")
        f.write(nome+"\n")
        f.close()
    if opcao == "2":
        for aluno in Lista_Alunos:
            print(Lista_Alunos)
    if opcao == "3":
        nome = input("Informe o aluno a ser removido: ")
        Lista_Alunos.remove(nome)
        print(f"O {nome} foi removido")    
    if opcao == "4":
        break