import json

def formata_retorno_sucesso_corpo(status: int, evt: dict):
    return {
        "statusCode": status,
        "corpo": json.dumps(evt)
    }

def formata_retorno_sucesso(status: int, mensagem: str):
    return {
        "statusCode": status,
        "mensagem": mensagem
    }

def formata_retorno_erro(status: int, mensagem: str):
    return {
        "statusCode": status,
        "mensagem": mensagem
    }