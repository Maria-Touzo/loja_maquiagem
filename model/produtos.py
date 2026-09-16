from database.conexao import conectar

class ProdutoImagem:
    def __init__(self, id_produto: int, url_imagem: str, id_imagem: int = None):
        self.id_imagem = id_imagem
        self.id_produto = id_produto
        self.url_imagem = url_imagem

    def cadastrar(self) -> bool:
        """Insere uma nova imagem vinculada a um produto."""
        conexao, cursor = conectar()
        cursor.execute("""
            INSERT INTO tb_produtos_imagens (id_produto, url_imagem)
            VALUES (%s, %s);
        """, [self.id_produto, self.url_imagem])
        conexao.commit()
        conexao.close()
        return True

    @staticmethod
    def buscar_por_produto(id_produto: int) -> list:
        """Retorna todas as imagens cadastradas para um produto específico."""
        conexao, cursor = conectar()
        cursor.execute("""
            SELECT id_imagem, id_produto, url_imagem 
            FROM tb_produtos_imagens 
            WHERE id_produto = %s;
        """, [id_produto])
        resultado = cursor.fetchall()
        conexao.close()
        return resultado

class Produto:
    def __init__(self, id_produto:int, id_categoria:int, nome_produto:str, descricao:str, preco:float, foto_principal:str):
        self.id_produto = id_produto
        self.id_categoria = id_categoria
        self.nome_produto = nome_produto
        self.descricao = descricao
        self.preco = preco
        self.foto_principal = foto_principal

    @staticmethod
    def listar_todos():
        conexao, cursor = conectar()
        cursor.execute("""
        SELECT * FROM tb_produtos;""")
        resultado = cursor.fetchall()
        conexao.close()
        return resultado

    @staticmethod
    def buscar_por_categorias(id_categoria:int):
        conexao, cursor = conectar()
        cursor.execute("""
        SELECT id_produto, id_categoria, nome_produto, descricao, preco, foto_principal
        FROM tb_produtos
        WHERE id_categoria = %s;""", [id_categoria])
        resultado = cursor.fetchall()
        conexao.close()
        return resultado

    @staticmethod
    def buscar_por_id(id_produto):
        conexao, cursor = conectar()
        cursor.execute("""
        SELECT id_produto, id_categoria, nome_produto, descricao, preco, foto_principal
        FROM tb_produtos
        WHERE id_produto = %s""", [id_produto])
        resultado = cursor.fetchone()
        conexao.close()
        return resultado
