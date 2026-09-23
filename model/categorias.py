from database import conectar

class Categoria:

    @staticmethod
    def listar_todas():
        conexao, cursor = conectar()
        cursor.execute("""
                        SELECT * FROM tb_categorias;
        """)
        resultado = cursor.fetchall()
        conexao.close()
        return resultado

    @staticmethod
    def buscar_por_id(id_categoria):
        conexao, cursor = conectar()
        cursor.execute("""
                        SELECT * FROM tb_categorias WHERE id_categoria=%s;""",[id_categoria])
        resultado = cursor.fetchone()
        conexao.close()
        return resultado
