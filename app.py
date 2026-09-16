from flask import Flask, render_template, request, redirect, url_for
from model.produtos import Produto, ProdutoImagem
from model.usuario import Usuario
from model.comentarios import Comentarios
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
        
       
        usuario_encontrado = Usuario.logar(email, senha)
            
      
        
        if usuario_encontrado:
            return "Login feito com sucesso! Bem-vindo(a)!"
        else:
            return "E-mail ou senha incorretos."
            
    return render_template('login.html')

# rota para cadastrar comentário se o usuário estiver logado
@app.route("/cadastrar_comentario", methods=["POST"])
def cadastrar_comentario():
    
    # verifica se o usuário está no logado
        if not session.get('usuario_id'):
            # pegando os dados do html
                id_produto = request.form.get("id_produto")
                texto = request.form.get("texto")
                id_usuario = session.get("usuario_id")
                Comentario.salvar(id_produto, id_usuario, texto)
                # se não estiver, redirecione para login
                return redirect(url_for('login'))
                
                return redirect(url_for('detalhes_produto', id_produto=id_produto))

# rota para a página produto
@app.route("/produtos/<int:id_produto>")
def detalhes_produtos(id_produto:int):
    produto_encontrado = buscar_por_id(id_produto)
    lista_comentarios = Comentarios.buscar_por_produto(id_produto)
    return render_template("produtos.html", 
    produto = produto_encontrado,
    comentarios = lista_comentarios)

# rota para a página categoria
@app.route("/categorias")
def categorias():
    return render_template("categorias.html")

# rota para a página catálogo
@app.route("/catalogo")
def catalogo():
    produtos = Produto.listar_todos()
    return render_template("catalogo.html", produtos = produtos)

app.run(debug= True)