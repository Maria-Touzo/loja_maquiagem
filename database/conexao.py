import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
          host = "localhost",
          port = 3306,
          user = "root",
          password = "root",
          database = "db_loja_maquiagem"
     )

    cursor = conexao.cursor(dictionary=True)
    
    return conexao, cursor