from flask import Flask, render_template, request, redirect, url_for, session, flash
from model.produtos import Produto, ProdutoImagem
from model.usuario import Usuario
from model.comentarios import Comentario
from model.categorias import Categoria


app = Flask(__name__)
app.secret_key = 'chave_secreta_loja_maquiagem' 

@app.route("/")
def index():
    destaque = Produto.listar_destaque()
    return render_template("index.html", produtos = destaque)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        senha = request.form.get("senha")
        endereco = request.form.get("endereco")
        
        if sucesso:
            return redirect(url_for("login"))
        else:
            flash("E-mail já cadastrado!")
            
    return render_template("cadastro.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        
        usuario_encontrado = Usuario.logar(email, senha)
        
        if usuario_encontrado:
            session["usuario_id"] = usuario_encontrado["id_usuario"]
            session["usuario_nome"] = usuario_encontrado["nome"]
            return redirect(url_for("index"))
        else:
            flash("E-mail ou senha incorretos.")
            
    return render_template('login.html')


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/catalogo")
def catalogo():
    id_categoria = request.args.get('categoria')
    if id_categoria:
        produtos = Produto.buscar_por_categorias(id_categoria)
    else:
        produtos = Produto.listar_todos()
    return render_template("catalogo.html", produtos=produtos)


@app.route("/produtos/<int:id_produto>")
def detalhes_produtos(id_produto: int):
    
    produto_encontrado = Produto.buscar_por_id(id_produto)
    lista_comentarios = Comentarios.buscar_por_produto(id_produto)
    
    return render_template("produtos.html", produto= produto_encontrado, comentarios=lista_comentarios)

@app.route("/cadastrar_comentario", methods=["POST"])
def cadastrar_comentario():
     if "usuario_id" not in session:
        return redirect(url_for('login'))
        
     id_produto = int(request.form.get("id_produto"))
     texto = request.form.get("texto")
     id_usuario = session.get("usuario_id")
    
     Comentario.salvar_comentario(id_produto, id_usuario, texto)
     return redirect(url_for('detalhes_produtos', id_produto=id_produto))


@app.route("/categorias")
def categorias():
    categorias_listar = Categoria.listar_todas_categorias()
    return render_template("categorias.html", categorias = categorias_listar)

if __name__ == "__main__":
    app.run(debug=True)