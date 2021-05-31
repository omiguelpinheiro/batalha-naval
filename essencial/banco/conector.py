import mysql.connector
from mysql.connector import connect
from essencial.banco.bd_jogador import cria_tabela_jogador
from essencial.banco.bd_partida import cria_tabela_partida
from essencial.banco.bd_quadrado import cria_tabela_quadrado


def conecta_servidor(host="localhost", user="root", password="root", log=False):
    try:
        conexao = mysql.connector.connect(
            host=host, user=user, password=password)
        if log:
            print("Conexão aberta")
        return conexao
    except Exception as e:
        print("Conexão não foi aberta", e)


def abre_cursor(con, log=False):
    try:
        if con is None or not con.is_connected():
            con = conecta_servidor()
        cursor = con.cursor(buffered=True)
        if log:
            print("Cursor aberto.")
        return cursor
    except Exception as e:
        if log:
            print("Cursor não foi aberto", e)


def cria_banco(current_cursor, nome="Modular", log=False):
    try:
        query = f"CREATE DATABASE {nome}"
        current_cursor.execute(query)
        if log:
            print("Banco {nome} foi criado")
        return 1
    except Exception as e:
        print("Banco não foi criado", e)
        return 0


def usa_banco(current_cursor, nome="Modular", log=False):
    try:
        query = f"USE {nome}"
        current_cursor.execute(query)
        if log:
            print(f"Usando banco {nome}")
        return 1
    except Exception as e:
        print("Banco não foi usado", e)
        return 0

def inicializa_banco(conexao, log=False):
    cursor = abre_cursor(conexao, log)  

    cria_banco(cursor, log=log)
    usa_banco(cursor, log=log)

    cria_tabela_jogador(cursor, log)
    cria_tabela_partida(cursor, log)
    cria_tabela_quadrado(cursor, log)


    return cursor

conexao = conecta_servidor()
