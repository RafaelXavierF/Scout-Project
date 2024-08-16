from funcoesAuxiliares import formata_retorno_sucesso, formata_retorno_erro
from conexaoDb import cadastra_usuario ,verifica_dados_repetidos_cadastro

def cadastrar_usuario(evt: dict, context :dict):
    try:
        retorno = verifica_dados_repetidos_cadastro(evt)
        
        if( len(retorno) == 0):
            cadastra_usuario(evt)

            return (formata_retorno_sucesso(200, 'Cadastro realizado com sucesso.'))
        else:
            return (formata_retorno_erro(400, 'Cpf-já-existente ou mal-formatado.'))
        
    except NameError:
        return formata_retorno_erro(400, NameError)

def loga_usuario(evt: dict, context: dict):
    try:
        retorno = verifica_dados_repetidos_cadastro(evt)

        if(len(retorno) > 1):
            print('')

    except NameError:
        return (formata_retorno_erro(400, 'Usuário-não-comprometido ou .'))

def pega_dados_usuario(evt: dict, context: dict):
    print('')