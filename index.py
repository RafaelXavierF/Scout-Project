from flask import Flask
import mysql.connector

app = Flask('_name_')

# Configurações de conexão
config = {
  'user': 'admin',
  'password': '180188',
  'host': '192.168.1.2',
  'database': 'mydb',
  'raise_on_warnings': True
}

try:
    # Conecta ao banco de dados
    conn = mysql.connector.connect(**config)

    if conn.is_connected():
        print('Conexão bem-sucedida!')

        # Executa uma consulta
        cursor = conn.cursor()
        cursor.execute("SELECT nm_jogador FROM mydb.cad_jogadores where cd_jogador = 1")

        # Obtém os resultados
        for row in cursor.fetchall():
            print(row)

except mysql.connector.Error as err:
    print("Erro de conexão:", err)

finally:
    # Fecha a conexão
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print('Conexão encerrada.')
        