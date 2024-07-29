from flask import Response
import datetime
import json

from funcoesAuxiliares import todos_preenchidos, formata_retorno_sucesso, formata_retorno_erro
from conexaoDb import cria_conexao_banco, verifica_dados_repetidos_cadastro

def cadastrar_usuario(evt: dict):
    preenchido = todos_preenchidos(evt)

    if(not preenchido):
        return formata_retorno_erro(400, 'Preencha todos os campos para prosseguir com o cadastro.')
    else:
        retorno_banco = verifica_dados_repetidos_cadastro(evt)
        if( len(retorno_banco) == 0):
            print('Conexão bem sucedida')
        else:
            print('Um erro ocorreu ao se conectar ao banco de dados.')
            return 'Um erro interno ocorreu ao finalizar o cadastro.'

def loga_usuario(evt: dict):
    conn = cria_conexao_banco()

    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT nm_jogador, cd_jogador, senha FROM mydb.cad_jogadores where cd_jogador = 1")

        resultado = cursor.fetchall()

        if(len(resultado) >= 1):
            validado = True if evt["id"] == resultado[0][1] and evt["senha"] == resultado[0][2] else False
            if(validado):
                return json.dumps(resultado[0][1])
        else:
            return Response("Id ou senha digitados incorretamente.", status=400)


# Teste mock
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

cadastrar_usuario(simula)