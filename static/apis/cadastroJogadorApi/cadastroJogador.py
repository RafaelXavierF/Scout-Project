from funcoesAuxiliares import formata_retorno_sucesso, formata_retorno_sucesso_corpo, formata_retorno_erro
from conexaoDb import cadastra_usuario ,obtem_dados_usuario

def cadastrar_usuario(evt :dict, context :dict):
    try:
        dados_usuario = obtem_dados_usuario(evt)
        
        if( len(dados_usuario) == 0):
            cadastra_usuario(evt)

            return (formata_retorno_sucesso(200, 'Cadastro realizado com sucesso.'))
        else:
            return (formata_retorno_erro(400, 'Cpf, email já existente ou mal-formatados.'))
        
    except NameError:
        return formata_retorno_erro(400, NameError)

def loga_usuario(evt: dict, context: dict):
    try:
        dados_usuario = obtem_dados_usuario(evt)
        
        autorizado = True if dados_usuario.get('senha') == evt['senha'] and dados_usuario.get('email') == evt['email'] else False

        if(autorizado):
            return (formata_retorno_sucesso(200, 'Usúario autorizado.'))
        else:
            return (formata_retorno_erro(400, 'Email ou senha digitados incorretamente.'))
        
    except NameError:
        return formata_retorno_erro(400, NameError)

def pega_dados_jogador(evt, context):
    try:
        parametros = evt['PathParameters']

        dados_usuario = obtem_dados_usuario(evt)

        if(dados_usuario):
            return formata_retorno_sucesso_corpo(200, dados_usuario)
        else:
            return (formata_retorno_erro(200, 'Jogador não encontrado ou Cpf mal formatado.'))
        
    except NameError:
        return formata_retorno_erro(400, NameError)
    