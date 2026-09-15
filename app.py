from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# rota pra abrir a página index
@app.route("/")
def pag_index():
    produtos = recuperar_requisitos()
    destaques = destaque()
    return render_template("index.html", produtos= produtos, destaques = destaques)