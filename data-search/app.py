from flask import Flask, render_template
import pymongo

app = Flask(__name__)

url = "mongodb+srv://x:x@cluster0.smtnsyk.mongodb.net/?retryWrites=true&w=majority"

myclient = pymongo.MongoClient(url)
mydb = myclient["meubanco"]
mycol = mydb["Lista-Alunos"]


@app.route("/")
def hello_world():
    dados = mycol.find_one({})
    return render_template("index.html", x = dados)
