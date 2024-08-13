def formata_retorno_sucesso(status: int, evt: dict):
    {
        "status": status,
        "retorno": evt
    }

def formata_retorno_erro(status: int, mensagem: str):
    {
        "status": status,
        "mensagem": mensagem
    }