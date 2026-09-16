from database.conexao import conectar

class Comentarios:
    def __init__(self, id_usuario:int, id_produto:int,texto:str ):
        self.id_usuario = id_usuario
        self.id_produto = id_produto
        self.texto = texto
    
    def cadastrar_comentario(self):
        conexao, cursor = conectar()
        cursor.execute("""
        INSERT INTO tb_comentarios(id_usuario, id_produto, texto)
        VALUES (%s, %s, %s);""",
        [self.id_usuario, self.id_produto, self.texto])
        conexao.commit()
        conexao.close()
        return True

    @staticmethod
    def buscar_por_produto(id_produto:int):
        conexao, cursor = conectar()
        cursor.execute("""
        SELECT 
        tb_comentarios.id_comentario,
        tb_comentarios.texto,
        tb_comentarios.data_comentario,
        tb_usuarios.nome AS nome_usuario
        FROM tb_comentarios
        INNER JOIN tb_usuarios ON tb_comentarios.id_usuario = tb_usuarios.id_usuario
        WHERE tb_comentarios.id_produto = %s;""", [id_produto],)
        resultado = cursor.fetchall()
        conexao.close()
        return resultado
