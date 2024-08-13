import boto3
import datetime
from boto3.dynamodb.conditions import Attr

def cria_conexao_banco():
    dynamodb = boto3.resource('dynamodb')

    tabela = dynamodb.Table('cad_jogadores')

    return tabela

def verifica_dados_repetidos_cadastro(evt: dict):
    tabela = cria_conexao_banco()

    resposta = tabela.scan(
    FilterExpression=Attr('nr_cpf').eq({evt['cpf']})
    )

    return resposta['Items']

    
def cadastra_usuario(evt :dict):
    tabela = cria_conexao_banco()

    tabela.put_item(
    Item={
        "cd_jogador": 0,
        "nm_jogador": "12",
        "nm_apelido": "Xavier",
        "dt_nascimento": datetime.datetime(2001, 12, 31),
        "nr_telefone": "31992652507",
        "st_whatapp": "1",
        "nr_camisa": 10,
        "cd_posicao": "2",
        "st_mensal": "1",
        "cpf": "11111111111",
        "senha": "senhaTeste"
        }
    )
