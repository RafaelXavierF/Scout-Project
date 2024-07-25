import mysql.connector

def cria_conexao_banco():
    configuracao_db = {
        'user': 'admin',
        'password': '1234',
        'host': 'localhost',
        'raise_on_warnings': True
    }
    conexao = mysql.connector.connect(**configuracao_db)
    return conexao.is_connected()
