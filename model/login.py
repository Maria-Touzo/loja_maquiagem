from database.conexao import conectar

def autenticar_usuario(email, senha):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM tb_usuarios WHERE email = %s AND senha = %s", 
        (email, senha)
    )
    usuario = cursor.fetchone()
    cursor.close()
    conexao.close()
    return usuario