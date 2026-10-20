from database.conexao import conectar


class Carrinho:
    def __init__(self, id_usuario, id_produto, quantidade=1):
        self.id_usuario = id_usuario
        self.id_produto = id_produto
        self.quantidade = quantidade

    def adicionar_carrinho(self, conexao, cursor):
        # verificando se o produto já está no carrinho
        cursor.execute("""
            SELECT id_carrinho, quantidade 
            FROM tb_carrinho
            WHERE id_usuario = %s AND id_produto = %s
        """, (self.id_usuario, self.id_produto))
        
        item = cursor.fetchone()

        # Se já estiver adicionado no carrinho, ele irá somar as quantidades
        if item:
            cursor.execute("""
                UPDATE tb_carrinho 
                SET quantidade = quantidade + %s 
                WHERE id_usuario = %s AND id_produto = %s
            """, (self.quantidade, self.id_usuario, self.id_produto))
        else:
            # Se não tiver, adiciona
            cursor.execute("""
                INSERT INTO tb_carrinho (id_usuario, id_produto, quantidade)
                VALUES (%s, %s, %s)
            """, (self.id_usuario, self.id_produto, self.quantidade))

        conexao.commit()
        return True

    @staticmethod
    def listar_carrinho(id_usuario):
        conexao, cursor = conectar()
        cursor.execute("""
            SELECT 
                tb_carrinho.id_carrinho,
                tb_carrinho.quantidade,
                tb_produtos.nome_produto,
                tb_produtos.preco,
                tb_produtos.foto_principal
            FROM tb_carrinho 
            INNER JOIN tb_produtos ON tb_carrinho.id_produto = tb_produtos.id_produto
            WHERE tb_carrinho.id_usuario = %s;
        """, [id_usuario])
        
        resultado = cursor.fetchall()
        conexao.close()
        return resultado