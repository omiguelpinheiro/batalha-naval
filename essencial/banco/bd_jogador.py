# cria a tabela jogador em um banco de dados


def cria_tabela_jogador(current_cursor, log=False):
    try:
        current_cursor.execute("CREATE TABLE Jogador ( \
            id_jogador INT AUTO_INCREMENT PRIMARY KEY, \
            nome VARCHAR(30) NOT NULL, \
            tipo_1 INT NOT NULL, \
            tipo_2 INT NOT NULL, \
            tipo_3 INT NOT NULL, \
            tipo_4 INT NOT NULL \
            )")
        print("Tabela Jogador criada")
        return 1
    except Exception as e:
        print("Tabela Jogador não foi criada", e)
        return 0

# insere valores na tabela jogador


def cria_jogador_banco(nome, tipo_1, tipo_2, tipo_3, tipo_4, current_cursor):
    try:
        query = f"INSERT INTO Jogador(nome, tipo_1, tipo_2, tipo_3, tipo_4) VALUES ('{nome}', {tipo_1}, {tipo_2}, {tipo_3}, {tipo_4})"
        current_cursor.execute(query)
        print(current_cursor.rowcount, "Jogador inserido")
        return 1
    except Exception as e:
        print("Não inseriu o jogador", e)
        raise e
        return 0

# le o ultimo id jogador inserido


def le_ultimo_id_jogador(current_cursor):
    try:
        query = "SELECT @@IDENTITY"
        current_cursor.execute(query)
        last_id = current_cursor.fetchone()
        print(current_cursor.rowcount, "Id jogador retornado")
        return last_id[0]
    except Exception as e:
        print("Id jogador não retornado", e)
        return 0

# atualiza algum row na tabela jogador


def atualiza_jogador(coluna, novo_valor, coluna_condicao, condicao, current_cursor):
    try:
        query = f"UPDATE Jogador SET {coluna}={novo_valor} WHERE {coluna_condicao}={condicao}"
        current_cursor.execute(query)
        print(current_cursor.rowcount, "Tabela jogador atualizada")
        return 1
    except Exception as e:
        print("Não atualizou a tabela Jogador", e)
        return 0

# deleta algum row na tabela jogador


def deleta_row_jogador(coluna_condicao, condicao, current_cursor):
    try:
        query = f"DELETE FROM Jogador WHERE {coluna_condicao}={condicao}"
        current_cursor.execute(query)
        print(current_cursor.rowcount, "Rows em Jogador removidos")
        return 1
    except Exception as e:
        print("Rows em Jogador não foram removidos", e)
        return 0

# remove a tabela jogador


def drop_tabela_jogador(current_cursor):
    try:
        query = f"DROP TABLE Jogador"
        current_cursor.execute(query)
        print(current_cursor.rowcount, "Tabela Jogador removida")
        return 1
    except Exception as e:
        print("Não removeu a Tabela Jogador", e)
        return 0
