from database.conexao import conectar

def listar_produtos(id_categoria=None):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
        
    produtos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return produtos