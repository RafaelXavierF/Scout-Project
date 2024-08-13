from flask import Response
import datetime
import json
import requests

from funcoesAuxiliares import formata_retorno_sucesso, formata_retorno_erro
from conexaoDb import cadastra_usuario ,verifica_dados_repetidos_cadastro

def cadastrar_usuario(evt: dict):
    # corpo = json.dumps(evt)

    retorno = verifica_dados_repetidos_cadastro(evt)

    if( len(retorno) == 0): 
        cadastra_usuario(evt)
        return formata_retorno_sucesso(200, retorno)
    else:
        return formata_retorno_erro(400, 'Um erro interno ocorreu ao finalizar o cadastro.')

def loga_usuario(evt: dict):
    return Response("Id ou senha digitados incorretamente.", status=400)

# Teste mock
simula = {
    "cd_jogador": 1,
    "cd_posicao": None,
    "dt_nascimento": datetime.datetime(2001, 12, 31),
    "nm_apelido": "Xavier",
    "nm_jogador": "Rafael Xavier Franco",
    "nr_camisa": 10,
    "nr_cpf": "14140452648",
    "nr_telefone": "31 992652507",
    "senha": 3214122,
    "st_mensal": False,
    "st_whatapp": False
}

cadastrar_usuario(simula)
