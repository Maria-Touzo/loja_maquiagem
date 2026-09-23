from database.conexao import conectar

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

    @staticmethod
    def listar_destaque():
        conexao, cursor = conectar()
        cursor.execute("""
        SELECT id_produto, nome_produto, preco, foto_principal
        FROM tb_produtos
        ORDER BY id_produto DESC
        LIMIT 4;
        """)
        resultado = cursor.fetchall()
        cursor.close()
        conexao.close()
        return resultado
