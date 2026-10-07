from database.conexao import conectar

class carrinho(id_usuario, id_produto, quantidade=1):
   def adicionar_carrinho():
    conexao, cursor = conectar()
    cursor.execute("""
                        INSERT INTO tb_carrinho (id_usuario, id_produto, quantidade)
                        VALUES (%s, %s, %s )
    """, (id_usuario, id_produto, quantidade))
    conexao.commit()
    conexao.close()
    return True

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
        INNER JOIN tb_produtos  ON tb_carrinho.id_produto = tb_produtos.id_produto
        WHERE tb_carrinho.id_usuario = %s;
        """, [id_usuario])
        resultado = cursor.fetchall()
        conexao.close()
        return resultado