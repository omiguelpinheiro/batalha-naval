from essencial.banco.conector import abre_cursor, con

# cria a tabela partida no banco


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

# insere valores na tabela partida


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

# le o ultimo id de partida inserido na tabela


def le_ultimo_id_partida(con):
    try:
        cursor = abre_cursor(con)
        query = "SELECT @@IDENTITY"
        cursor.execute(query)
        con.commit()
        last_id = cursor.fetchone()
        print(cursor.rowcount, "Id partida retornado")
        cursor.close()
        return last_id[0]
    except Exception as e:
        print("Id partida não retornado", e)
        return 0

# atualiza algum row da tabela partida


def finaliza_partida(id_partida, con):
    try:
        cursor = abre_cursor(con)
        query = f"UPDATE Partida SET finalizada=TRUE WHERE id_partida={id_partida}"
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount, "Partida atualizada")
        cursor.close()
        return 1
    except Exception as e:
        print("Não atualizou a partida", e)
        return 0

# remove algum row da tabela partida


def deleta_row_partida(coluna_condicao, condicao, con):
    try:
        cursor = abre_cursor(con)
        query = f"DELETE FROM Partida WHERE {coluna_condicao}={condicao}"
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount, "Rows em Partida removidos")
        cursor.close()
        return 1
    except Exception as e:
        print("Rows em Partida não foram removidos", e)
        return 0

# remove a tabela partida do banco


def drop_tabela_partida(con):
    try:
        cursor = abre_cursor(con)
        query = f"DROP TABLE Partida"
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount, "Tabela Partida removida")
        cursor.close()
        return 1
    except Exception as e:
        print("Não removeu a Tabela Partida", e)
        return 0


cria_tabela_partida(con)
