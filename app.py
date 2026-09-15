from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# rota pra abrir a página index
@app.route("/")
def pag_index():
    return render_template("index.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    return render_template("cadastro.html")

@app.route("/login",  methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

@app.route("/categorias")
def categorias():
    return render_template("categorias.html")

@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html")

app.run(debug= True)