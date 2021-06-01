# cria a tabela partida no banco


def cria_tabela_partida(current_cursor, log=False):
    try:
        current_cursor.execute("CREATE TABLE Partida ( \
            id_partida INT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
            id_jogador1 INT NOT NULL, \
            id_jogador2 INT NOT NULL, \
            n_ultima_jogada INT NOT NULL, \
            finalizada BOOLEAN NOT NULL, \
            vencedor INT NOT NULL, \
            CONSTRAINT FK_Jogador1Partida FOREIGN KEY (id_jogador1) REFERENCES Jogador(id_jogador), \
            CONSTRAINT FK_Jogador2Partida FOREIGN KEY (id_jogador2) REFERENCES Jogador(id_jogador) \
            )")
        if log:
            print("Tabela partida criada")
        return 1
    except Exception as e:
        print("Tabela Partida não foi criada", e)
        return 0

# insere valores na tabela partida


def cria_partida_banco(id_jogador1, id_jogador2, current_cursor, log=False):
    try:
        query = f"INSERT INTO Partida(id_jogador1, id_jogador2, n_ultima_jogada, finalizada, vencedor) VALUES ({id_jogador1}, {id_jogador2}, 0, false, -1)"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Partida inserida")
        return 1
    except Exception as e:
        raise e
        print("Não inseriu a partida", e)
        return 0

# le o ultimo id de partida inserido na tabela


def le_ultimo_id_partida(current_cursor, log=False):
    try:
        query =  "SELECT @@IDENTITY"
        current_cursor.execute(query)
        last_id = current_cursor.fetchone()
        if log:
            print(current_cursor.rowcount, "Id partida retornado")
        return last_id[0]
    except Exception as e:
        print("Id partida não retornado", e)
        return 0

# atualiza algum row da tabela partida


def finaliza_partida(id_partida, id_vencedor, current_cursor, log=False):
    try:
        query = f"UPDATE Partida SET finalizada=TRUE, vencedor={id_vencedor} WHERE id_partida={id_partida}"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Partida atualizada")
        return 1
    except Exception as e:
        print("Não atualizou a partida", e)
        return 0

def atualiza_ultima_rodada(id_partida, ultima_rodada, current_cursor, log=False):
    try:
        query = f"UPDATE Partida SET n_ultima_jogada={ultima_rodada} WHERE id_partida={id_partida}"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Última rodada da partida atualizada")
        return 1
    except Exception as e:
        raise e
        print("Não atualizou a última rodada da partida", e)
        return 0

def deleta_row_partida(coluna_condicao, condicao, current_cursor, log=False):
    try:
        query = f"DELETE FROM Partida WHERE {coluna_condicao}={condicao}"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Rows em Partida removidos")
        return 1
    except Exception as e:
        print("Rows em Partida não foram removidos", e)
        return 0

# remove a tabela partida do banco


def drop_tabela_partida(current_cursor, log=False):
    try:
        query = f"DROP TABLE Partida"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Tabela Partida removida")
        return 1
    except Exception as e:
        print("Não removeu a Tabela Partida", e)
        return 0
