from essencial.banco.conector import abre_cursor, con


def cria_tabela_partida(con):
    try:
        cursor = abre_cursor(con)
        cursor.execute("CREATE TABLE Partida ( \
            id_partida INT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
            id_jogador1 INT NOT NULL, \
            id_jogador2 INT NOT NULL, \
            n_ultima_jogada INT NOT NULL, \
            finalizada BOOLEAN NOT NULL, \
            CONSTRAINT FK_Jogador1Partida FOREIGN KEY (id_jogador1) REFERENCES Jogador(id_jogador), \
            CONSTRAINT FK_Jogador2Partida FOREIGN KEY (id_jogador2) REFERENCES Jogador(id_jogador) \
            )")
        con.commit()
        print("Tabela Jogador criada")
        cursor.close()
        return 1
    except Exception as e:
        print("Tabela Jogador não foi criada", e)
        return 0

def cria_partida_banco(id_jogador1, id_jogador2, con):
    try:
        cursor = abre_cursor(con)
        print(id_jogador1, id_jogador2)
        query = f"INSERT INTO Partida(id_jogador1, id_jogador2, n_ultima_jogada, finalizada) VALUES ({id_jogador1}, {id_jogador2}, 0, false)"
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount, "Partida inserida")
        cursor.close()
        return 1
    except Exception as e:
        print("Não inseriu a partida", e)
        return 0

def le_ultimo_id_partida(con):
    try:
        cursor = abre_cursor(con)
        query = "SELECT @@IDENTITY"
        cursor.execute(query)
        con.commit()
        last_id = cursor.fetchone()
        print(cursor.rowcount, "Id partida retornado")
        cursor.close()
        return last_id
    except Exception as e:
        print("Id partida não retornado", e)
        return 0


def atualiza_partida(coluna, novo_valor, coluna_condicao, condicao, con):
    try:
        cursor = abre_cursor(con)
        query = f"UPDATE Partida SET {coluna}={novo_valor} WHERE {coluna_condicao}={condicao}"
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount, "Partida atualizada")
        cursor.close()
        return 1
    except Exception as e:
        print("Não atualizou a partida", e)
        return 0


def deleta_partida(coluna_condicao, condicao, con):
    try:
        cursor = abre_cursor(con)
        query = f"DELETE FROM Partida WHERE {coluna_condicao}={condicao}"
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount, "Partida removida")
        cursor.close()
        return 1
    except Exception as e:
        print("Não removeu a partida", e)
        return 0

cria_tabela_partida(con)
