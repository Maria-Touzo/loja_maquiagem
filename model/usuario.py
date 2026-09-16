from database.conexao import conectar

class Usuario:
    def __init__(self, nome:str, email:str, telefone:str, senha:str, endereco:str):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.endereco = endereco

    def cadastrar(self):
        conexao, cursor = conectar()
        cursor.execute("""
                        INSERT INTO tb_usuarios (nome, email, telefone, senha, endereco)
                       VALUES (%s, %s, %s, %s, %s);
                       """, [self.nome,self.email, self.telefone, self.senha, self.endereco])
        conexao.commit()
        conexao.close()
        return True

    @staticmethod
    def logar(usuario:str, senha:str) ->dict:
        conexao, cursor = conectar()
        cursor.execute("""
                        SELECT * FROM usuarios WHERE usuario = %s AND senha  %s;
                       """, 
                       [usuario, senha ])
        resultado = cursor.fetchone
        conexao.close()
        return resultado
