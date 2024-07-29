import mysql.connector
import datetime

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
    else:
        return False
    
def cadastra_usuario(evt):
    conexao = cria_conexao_banco()
    
    print('Teste.')
    
#simula mock 
simula = {
    "cd_jogador": 1,
    "nm_jogador": "12",
    "nm_apelido": "Xavier",
    "dt_nascimento": datetime.datetime(2001, 12, 31),
    "nr_telefone": "31992652507",
    "st_whatapp": "1",
    "nr_camisa": 10,
    "cd_posicao": "2",
    "st_mensal": "1",
    "nr_cpf": "11111111111",
    "senha_cpf": "senhaTeste",
    "email": "teste@gmail.com"
}

verifica_dados_repetidos_cadastro(simula)