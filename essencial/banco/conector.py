import mysql.connector
from mysql.connector import connect


def conecta_servidor(host="localhost", user="root", password=""):
    try:
        conexao = mysql.connector.connect(
            host=host, user=user, password=password)
        print("Conexão aberta")
    except Exception as e:
        print("Conexão não foi aberta", e)
    return conexao


def abre_cursor(con):
    try:
        if con is None or not con.is_connected():
            con = conecta_servidor()
        cursor = con.cursor(buffered=True)

        print("Cursor aberto.")
    except Exception as e:
        print("Cursor não foi aberto", e)
    return cursor


def cria_banco(nome, con):
    try:
        cursor = abre_cursor(con)
        query = f"CREATE DATABASE {nome}"
        cursor.execute(query)
        con.commit()
        print("Banco {nome} foi criado")
        cursor.execute(f"USE {nome}")
        print(f"Usando banco {nome}")
        cursor.close()
        return 1
    except Exception as e:
        print("Banco não foi criado", e)
        return 0


def usa_banco(nome, con):
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
cria_banco("MODULAR", con)
usa_banco("MODULAR", con)


'''
# CONSULTA DO QUE FIZEMOS NO PRIMEIRO DIA:
try:
    host = "localhost"
    database = "Modular"
    user = "root"
    password = "123"

    connection = mysql.connector.connect(
        host=host, user=user, password=password)

    cursor = connection.cursor()

    if connection.is_connected():
        db_info = connection.get_server_info()
        print(db_info)
        cursor.execute(f"DROP DATABASE {database}")
        cursor.execute(f"CREATE DATABASE {database}")
        cursor.execute("USE Modular")
        cursor.execute("CREATE TABLE Jogador ( \
            id_jogador INT AUTO_INCREMENT PRIMARY KEY, \
            nome VARCHAR(30) NOT NULL, \
            tipo_1 INT NOT NULL, \
            tipo_2 INT NOT NULL, \
            tipo_3 INT NOT NULL, \
            tipo_4 INT NOT NULL \
            )")

        cursor.execute("CREATE TABLE Partida ( \
            id_partida INT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
            id_jogador1 INT NOT NULL, \
            id_jogador2 INT NOT NULL, \
            n_ultima_jogada INT NOT NULL, \
            finalizada BOOLEAN NOT NULL, \
            CONSTRAINT FK_Jogador1Partida FOREIGN KEY (id_jogador1) REFERENCES Jogador(id_jogador), \
            CONSTRAINT FK_Jogador2Partida FOREIGN KEY (id_jogador2) REFERENCES Jogador(id_jogador) \
            )")

        cursor.execute("CREATE TABLE Quadrado ( \
            id_dono INT NOT NULL, \
            linha CHAR(1) NOT NULL, \
            coluna CHAR(1) NOT NULL, \
            n_jogada INT NOT NULL, \
            estado CHAR(1) NOT NULL,  \
            PRIMARY KEY (id_dono, linha, coluna, n_jogada), \
            CONSTRAINT FK_JogadorQuadrado FOREIGN KEY (id_dono) REFERENCES Jogador(id_jogador)")\

        # CRUD
        # Create (isso aqui vai sumir)
        cursor.execute(
            "INSERT INTO Jogador(nome, tipo_0, tipo_1, tipo_2, tipo_3) VALUES ('Miguel', 0, 1, 2, 3)")
        cursor.execute(
            "INSERT INTO Jogador(nome, tipo_0, tipo_1, tipo_2, tipo_3) VALUES ('Leo', 1, 2, 3, 4)")
        cursor.execute(
            "INSERT INTO Jogador(nome, tipo_0, tipo_1, tipo_2, tipo_3) VALUES ('Luiza', 2, 3, 4, 5)")
        cursor.execute(
            "INSERT INTO Jogador(nome, tipo_0, tipo_1, tipo_2, tipo_3) VALUES ('Marina', 3, 4, 5, 6)")
        # Read
        cursor.execute("SELECT * FROM Jogador")

        cursor.execute(
            "INSERT INTO Quadrado(id_dono, linha, coluna, n_jogada, estado) VALUES (1, 'a', '8', 1, 'H')")
        cursor.execute(
            "INSERT INTO Quadrado(id_dono, linha, coluna, n_jogada, estado) VALUES (2, 'f', '3', 2, 'H')")
        cursor.execute(
            "INSERT INTO Quadrado(id_dono, linha, coluna, n_jogada, estado) VALUES (3, 'd', '1', 5, 'w')")
        cursor.execute(
            "INSERT INTO Quadrado(id_dono, linha, coluna, n_jogada, estado) VALUES (3, 'c', '9', 9, 'h')")

        # Update
        cursor.execute("UPDATE Partida SET finalizada=1 WHERE id_partida=2")

        # Delete
        cursor.execute("DELETE FROM Partida WHERE id_partida=1")

        result = cursor.fetchall()
        print(result)

        connection.commit()
except Exception as e:
    print("Erro de conexão", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("Conexão encerrada")
'''
