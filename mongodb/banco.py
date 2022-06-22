import pymongo

url = "mongodb+srv://x:eduardo12344@cluster0.smtnsyk.mongodb.net/?retryWrites=true&w=majority"
myclient = pymongo.MongoClient(url)
mydb = myclient["meubanco"]
mycol = mydb["Lista-Alunos"]
nome = input("Digite um nome: ")
dados = {"nome":f"{nome}"}
x = mycol.insert_one(dados)
print("Os dados foram inseridos com id:", x.inserted_id)