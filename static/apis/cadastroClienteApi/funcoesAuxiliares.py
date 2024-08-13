import datetime
import json

def formata_retorno_sucesso_corpo(status: int, evt: dict):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
            "Allow-Cross-Origin": '*'
        },
        "corpo": json.dumps(evt)
    }

def formata_retorno_sucesso(status: int, mensagem: str):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
            "Allow-Cross-Origin": '*'
        },
        "mensagem": mensagem
    }

def formata_retorno_erro(status: int, mensagem: str):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json", 
            "Allow-Cross-Origin": '*'
        },
        "mensagem": mensagem
    }

def dictMock():
    simula = {
    "cd_posicao": None,
    "dt_nascimento": datetime.datetime(2001, 12, 31),
    "nm_apelido": "Xavier",
    "nm_jogador": "Rafael Xavier Franco",
    "nr_camisa": 10,
    "nr_cpf": "14140452644",
    "nr_telefone": "31 992652507",
    "senha": 3214122,
    "st_mensal": False,
    "st_whatapp": False
    }
    
    return simula