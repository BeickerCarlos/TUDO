from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/form", methods=["POST"])
def hello_world2():
    dados = request.form.get('nome')
    return f"<h1>{dados}</h1>"