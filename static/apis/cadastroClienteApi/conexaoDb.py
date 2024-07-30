import mysql.connector

def cria_conexao_banco():
    configuracao_db = {
        'host': '127.0.0.1',        
        'user': 'admin',
        'password': 'senhaDb#123',
        'database': 'mydb',
        'raise_on_warnings': True
    }

    conexao = mysql.connector.connect(**configuracao_db)
    return conexao if conexao.is_connected() else False

def verifica_dados_repetidos_cadastro(evt):
    conexao = cria_conexao_banco()

    if (conexao):
        cursor = conexao.cursor()
        cursor.execute(f"SELECT email_jogador FROM mydb.cad_jogadores WHERE email_jogador = '{evt["email"]}'")
        resultado = cursor.fetchall()

        return resultado
    
def cadastra_usuario(evt):
    conexao = cria_conexao_banco()

    if(conexao):
        print()