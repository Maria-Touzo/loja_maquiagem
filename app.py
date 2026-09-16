from flask import Flask, render_template, request, redirect, url_for

from model.usuario import Usuario
app = Flask(__name__)

# rota pra abrir a página index
@app.route("/")
def pag_index():
    return render_template("index.html")

# rota para a página cadastro
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        
        nome = request.form.get("nome")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        senha = request.form.get("senha")
        endereco = request.form.get("endereco")
        
       
        novo_usuario = Usuario(nome, email, telefone, senha, endereco)
        novo_usuario.cadastrar()
        
        
        return redirect(url_for("login")) 
        
  
    return render_template("cadastro.html")


# rota para a página login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        
        try:
            # Tenta buscar o usuário no banco de dados
            usuario_encontrado = Usuario.logar(email, senha)
            
        except Exception as e:
            
            return "Erro interno no servidor ao tentar logar."
        
        if usuario_encontrado:
            return "Login feito com sucesso! Bem-vindo(a)!"
        else:
            return "E-mail ou senha incorretos."
            
    # Se for GET, mostra a página HTML do login
    return render_template('login.html')
# rota para a página produto
@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

# rota para a página categoria
@app.route("/categorias")
def categorias():
    return render_template("categorias.html")

# rota para a página catálogo
@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html")

app.run(debug= True)