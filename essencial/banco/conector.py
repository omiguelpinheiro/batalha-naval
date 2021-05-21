
import mysql.connector
from mysql.connector import connect

cursor = None

try:
    host = "localhost"
    database = "Modular"
    user = "root"
    password = "123"
    
    connection = mysql.connector.connect(host=host, user=user, password=password)
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
            tipo_0 INT NOT NULL, \
            tipo_1 INT NOT NULL, \
            tipo_2 INT NOT NULL, \
            tipo_3 INT NOT NULL \
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
            CONSTRAINT FK_JogadorQuadrado FOREIGN KEY (id_dono) REFERENCES Jogador(id_jogador) \
            )")

        # CRUD
        # Create
        cursor.execute("INSERT INTO Jogador(nome, tipo_0, tipo_1, tipo_2, tipo_3) VALUES ('Miguel', 0, 1, 2, 3)")
        cursor.execute("INSERT INTO Jogador(nome, tipo_0, tipo_1, tipo_2, tipo_3) VALUES ('Leo', 1, 2, 3, 4)")
        cursor.execute("INSERT INTO Jogador(nome, tipo_0, tipo_1, tipo_2, tipo_3) VALUES ('Luiza', 2, 3, 4, 5)")
        cursor.execute("INSERT INTO Jogador(nome, tipo_0, tipo_1, tipo_2, tipo_3) VALUES ('Marina', 3, 4, 5, 6)")

        # Read
        cursor.execute("SELECT * FROM Jogador")

        cursor.execute("INSERT INTO Partida(id_jogador1, id_jogador2, n_ultima_jogada, finalizada) VALUES (1, 2, 0, false)")
        cursor.execute("INSERT INTO Partida(id_jogador1, id_jogador2, n_ultima_jogada, finalizada) VALUES (3, 4, 25, false)")

        cursor.execute("INSERT INTO Quadrado(id_dono, linha, coluna, n_jogada, estado) VALUES (1, 'a', '8', 1, 'H')")
        cursor.execute("INSERT INTO Quadrado(id_dono, linha, coluna, n_jogada, estado) VALUES (2, 'f', '3', 2, 'H')")
        cursor.execute("INSERT INTO Quadrado(id_dono, linha, coluna, n_jogada, estado) VALUES (3, 'd', '1', 5, 'w')")
        cursor.execute("INSERT INTO Quadrado(id_dono, linha, coluna, n_jogada, estado) VALUES (3, 'c', '9', 9, 'h')")

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
