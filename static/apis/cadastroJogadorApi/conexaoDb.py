import boto3
from boto3.dynamodb.conditions import Attr

def cria_conexao_banco():
    dynamodb = boto3.resource('dynamodb')

    tabela = dynamodb.Table('cad_jogadores')

    return tabela

def verifica_dados_repetidos_cadastro(evt: dict):
    tabela = cria_conexao_banco()

    resposta = tabela.scan(
    FilterExpression=Attr('nr_cpf').eq(evt['nr_cpf'])
    )

    return resposta['Items']

def cadastra_usuario(evt :dict):
    tabela = cria_conexao_banco()
    
    tabela.put_item(
    Item={
        "cd_jogador": evt['cd_jogador'],
        "cd_posicao": evt['cd_posicao'],
        "dt_nascimento": int(evt['dt_nascimento'].timestamp()),
        "nm_apelido": evt['nm_apelido'],
        "nm_jogador": evt['nm_jogador'],
        "nr_camisa": evt['nr_camisa'],
        "nr_cpf": evt['nr_cpf'],
        "nr_telefone": evt['nr_telefone'],
        "senha": evt['senha'],
        "st_mensal": evt['st_mensal'],
        "st_whatsapp": evt['st_whatapp']
        }
    )