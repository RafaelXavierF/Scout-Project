from flask import Response
import datetime
import json
import requests

from funcoesAuxiliares import todos_preenchidos
from conexaoDb import cria_conexao_banco, verifica_dados_repetidos

def cadastrarUsuario(evt):
    preenchido = todos_preenchidos(evt)
    conexao = cria_conexao_banco()

    if(not preenchido):
        return 'Preencha todos os campos para finalizar o cadastro.'
    else:
        if(conexao):
            verifica_dados_repetidos(evt)
        else:
            return 'Um erro interno ocorreu ao finalizar o cadastro'


def verificaLogin(evt):
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
            
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()

     

# Teste mock
simula = {
    "cd_jogador": 1,
    'nm_jogador':'12', 
    "nm_apelido": '',
    "dt_nascimento": datetime.datetime(2001, 12, 31),
    "nr_telefone": '31992652507',
    "st_whatapp": '1',
    "nr_camisa": 10,
    "cd_posicao": '2',
    "st_mensal": '1',
    "nr_cpf": '11111111111',
    "senha_cpf":  'senhaTeste'
}

cadastrarUsuario(simula)
