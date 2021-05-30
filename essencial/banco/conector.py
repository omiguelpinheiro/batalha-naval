import mysql.connector
from mysql.connector import connect


def conecta_servidor(host="localhost", user="root", password="root"):
    try:
        conexao = mysql.connector.connect(
            host=host, user=user, password=password)
        print("Conexão aberta")
        return conexao
    except Exception as e:
        print("Conexão não foi aberta", e)


def abre_cursor(con):
    try:
        if con is None or not con.is_connected():
            con = conecta_servidor()
        cursor = con.cursor(buffered=True)

        print("Cursor aberto.")
    except Exception as e:
        print("Cursor não foi aberto", e)
    return cursor


def cria_banco(con, nome="Modular"):
    try:
        cursor = abre_cursor(con)
        query = f"CREATE DATABASE {nome}"
        cursor.execute(query)
        con.commit()
        print("Banco {nome} foi criado")
        cursor.close()
        return 1
    except Exception as e:
        print("Banco não foi criado", e)
        return 0


def usa_banco(con, nome="Modular"):
    try:
        cursor = abre_cursor(con)
        query = f"USE {nome}"
        cursor.execute(query)
        con.commit()
        print(f"Usando banco {nome}")
        cursor.close()
        return 1
    except Exception as e:
        print("Banco não foi usado", e)
        return 0


con = conecta_servidor()
cria_banco(con)
usa_banco(con)
