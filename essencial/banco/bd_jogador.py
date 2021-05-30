from essencial.banco.conector import abre_cursor, con

# cria a tabela jogador em um banco de dados


def cria_tabela_jogador(con):
    try:
        cursor = abre_cursor(con)
        cursor.execute("CREATE TABLE Jogador ( \
            id_jogador INT AUTO_INCREMENT PRIMARY KEY, \
            nome VARCHAR(30) NOT NULL, \
            tipo_1 INT NOT NULL, \
            tipo_2 INT NOT NULL, \
            tipo_3 INT NOT NULL, \
            tipo_4 INT NOT NULL \
            )")
        con.commit()
        print("Tabela Jogador criada")
        cursor.close()
        return 1
    except Exception as e:
        print("Tabela Jogador não foi criada", e)
        return 0

# insere valores na tabela jogador


def cria_jogador_banco(nome, tipo_1, tipo_2, tipo_3, tipo_4, con):
    try:
        cursor = abre_cursor(con)
        query = f"INSERT INTO Jogador(nome, tipo_1, tipo_2, tipo_3, tipo_4) VALUES ('{nome}', {tipo_1}, {tipo_2}, {tipo_3}, {tipo_4})"
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount, "Jogador inserido")
        cursor.close()
        return 1
    except Exception as e:
        print("Não inseriu o jogador", e)
        return 0

# le o ultimo id jogador inserido


def le_ultimo_id_jogador(con):
    try:
        cursor = abre_cursor(con)
        query = "SELECT @@IDENTITY"
        cursor.execute(query)
        con.commit()
        last_id = cursor.fetchone()
        print(cursor.rowcount, "Id jogador retornado")
        cursor.close()
        return last_id[0]
    except Exception as e:
        print("Id jogador não retornado", e)
        return 0

# atualiza algum row na tabela jogador


def atualiza_jogador(coluna, novo_valor, coluna_condicao, condicao, con):
    try:
        cursor = abre_cursor(con)
        query = f"UPDATE Jogador SET {coluna}={novo_valor} WHERE {coluna_condicao}={condicao}"
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount, "Tabela jogador atualizada")
        cursor.close()
        return 1
    except Exception as e:
        print("Não atualizou a tabela Jogador", e)
        return 0

# deleta algum row na tabela jogador


def deleta_row_jogador(coluna_condicao, condicao, con):
    try:
        cursor = abre_cursor(con)
        query = f"DELETE FROM Jogador WHERE {coluna_condicao}={condicao}"
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount, "Rows em Jogador removidos")
        cursor.close()
        return 1
    except Exception as e:
        print("Rows em Jogador não foram removidos", e)
        return 0

# remove a tabela jogador


def drop_tabela_jogador(con):
    try:
        cursor = abre_cursor(con)
        query = f"DROP TABLE Jogador"
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount, "Tabela Jogador removida")
        cursor.close()
        return 1
    except Exception as e:
        print("Não removeu a Tabela Jogador", e)
        return 0


cria_tabela_jogador(con)  # criar a tabela
