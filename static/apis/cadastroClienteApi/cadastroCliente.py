from flask import Response
import datetime
import json
import requests

from funcoesAuxiliares import todos_preenchidos, formata_retorno_sucesso, formata_retorno_erro
from conexaoDb import cadastra_usuario ,verifica_dados_repetidos_cadastro

def cadastrar_usuario(evt: dict):
    preenchido = todos_preenchidos(evt)

    if(not preenchido):
        return formata_retorno_erro(400, 'Preencha todos os campos para prosseguir com o cadastro.')
    else:
        retorno = verifica_dados_repetidos_cadastro(evt)
        if( len(retorno) == 0): 
            formata_retorno_sucesso(200, retorno)
        else:
            return formata_retorno_erro(400, 'Um erro interno ocorreu ao finalizar o cadastro.')

def loga_usuario(evt: dict):
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
