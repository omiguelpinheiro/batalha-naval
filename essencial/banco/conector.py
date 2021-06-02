from essencial.banco.bd_jogador import cria_tabela_jogador
from essencial.banco.bd_partida import cria_tabela_partida
from essencial.banco.bd_quadrado import cria_tabela_quadrado
from typing import Union
from mysql.connector import connect
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import CursorBase


def conecta_servidor(host: str = "localhost", user: str = "root", password: str = "root", log: bool = False) -> Union[MySQLConnection, int]:
    """Cria uma conexão com o servidor.

    Args:
        host (str, optional): Host do servidor. Default é "localhost".
        user (str, optional): Usuário do servidor. Default é "root".
        password (str, optional): Senha do servidor. Default é "root".
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        Union[MySQLConnection, int]: A conexão com o servidor estabelecida caso tenha
            dado certo ou -1 caso alguma coisa tenha dado errado ao abrir a conexão.

    """
    try:
        conexao = connect(
            host=host, user=user, password=password)
        if log:
            print("Conexão aberta")
        return conexao
    except Exception as e:
        if log:
            print("Conexão não foi aberta", e)
        return -1


def abre_cursor(con: MySQLConnection, log: bool = False) -> Union[CursorBase, int]:
    """Cria o cursor para executar queries sql.

    Args:
        con (MySQLConnection): Uma conexão com um banco de previamente aberta.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        Union[CursorBase, int]: O cursor aberto com buffer ativado caso tenha dado certo ou
            -1 caso alguma coisa tenha dado errado ao abrir o cursor.

    """
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
        return -1


def cria_banco(current_cursor: CursorBase, nome="Modular", log=False) -> int:
    """Cria um banco caso ele não exista.

    Args:
        current_cursor (CursorBase): Um cursor aberto e conectado a um banco de dados.
        nome (str, optional): Nome do banco. Default é "Modular".
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        int: 1 se o banco foi criado.
             0 se o banco não foi criado.

    """
    try:
        query = f"CREATE DATABASE {nome}"
        current_cursor.execute(query)
        if log:
            print("Banco {nome} foi criado")
        return 1
    except Exception as e:
        if log:
            print("Banco não foi criado", e)
        return 0


def usa_banco(current_cursor: CursorBase, nome: str = "Modular", log: bool = False) -> int:
    """Faz o cursor usar o banco.

    Args:
        current_cursor (CursorBase): Um cursor aberto e conectado a um banco de dados.
        nome (str, optional): Nome do banco que o cursor deve usar. Default é "Modular".
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        int: 1 se o cursor estiver agora usando o banco.
             2 se o cursor não conseguiu começar a usar o banco.

    """
    try:
        query = f"USE {nome}"
        current_cursor.execute(query)
        if log:
            print(f"Usando banco {nome}")
        return 1
    except Exception as e:
        if log:
            print("Banco não foi usado", e)
        return 0


def inicializa_banco(conexao: MySQLConnection, log: bool = False) -> CursorBase:
    """Cria banco e tabelas se não existirem ainda.

    Args:
        conexao (MySQLConnection): Uma conexão aberta com o banco de dados.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        CursorBase: O cursor após ter executado as queries.
        
    """
    cursor = abre_cursor(conexao, log)  

    cria_banco(cursor, log=log)
    usa_banco(cursor, log=log)

    cria_tabela_jogador(cursor, log)
    cria_tabela_partida(cursor, log)
    cria_tabela_quadrado(cursor, log)

    return cursor

conexao = conecta_servidor()  # Inicia conexão no import
