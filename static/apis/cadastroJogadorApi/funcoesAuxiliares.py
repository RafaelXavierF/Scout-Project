import json

def formata_retorno_sucesso_corpo(status: int, evt: dict):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Methods": 'POST',
            "Access-Control-Allow-Origin": '*'
        },
        "corpo": json.dumps(evt)
    }

def formata_retorno_sucesso(status: int, mensagem: str):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Methods": 'POST',
            "Access-Control-Allow-Origin": '*'
        },
        "mensagem": mensagem
    }

def formata_retorno_erro(status: int, mensagem: str):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Methods": 'POST',
            "Access-Control-Allow-Origin": '*'
        },
        "mensagem": mensagem
    }