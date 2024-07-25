import mysql.connector

def cria_conexao_banco():
    configuracao_db = {
        'user': 'admin',
        'password': '1234',
        'host': 'localhost',
        'raise_on_warnings': True
    }

    conexao = mysql.connector.connect(**configuracao_db)
    return conexao if conexao.is_connected() else False

def verifica_dados_repetidos(evt):
    conexao = cria_conexao_banco()

    if conexao():
        cursor = conexao.cursor()
        cursor.execute(f"SELECT email senha FROM mydb.cad_jogadores where cd_jogador = {evt['senha']}")

        resultado = cursor.fetchall()
        print(resultado)


