from database import conectar

class Comentario():
    def __init__(self, id_comentario, id_produto, id_usuario, texto, data ):
        self.id_comentario = id_comentario
        self.id_produto = id_produto
        self.id_usuario = id_usuario
        self.texto = texto
        self.data = data

    @staticmethod
    def salvar_comentario(id_produto: int, id_usuario: int, texto: str):
        conexao, cursor = conectar()
        cursor.execute("""
                    INSERT INTO tb_comentarios (id_produto, id_usuario, texto)
                    VALUES (%s, %s, %s);""", [id_produto, id_usuario, texto])
        conexao.commit()
        conexao.close()
        return True

    @staticmethod
    def buscar_comentario_por_produto(id_produto: int):
        conexao, cursor = conectar()
        cursor.execute("""
        SELECT tb_comentarios.texto, tb_usuarios.nome 
        FROM tb_comentarios
        INNER JOIN tb_usuarios
            ON tb_comentarios.id_usuario = tb_usuarios.id_usuario
        WHERE tb_comentarios.id_produto = %s;""", [id_produto ])
        resultado =cursor.fetchall()
        conexao.close()
        return resultado