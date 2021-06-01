from essencial.banco.bd_partida import le_ultimo_id_partida

# cria a tabela jogador em um banco de dados


def cria_tabela_jogador(current_cursor, log=False):
    try:
        current_cursor.execute("CREATE TABLE Jogador ( \
            id_jogador INT AUTO_INCREMENT PRIMARY KEY, \
            nome VARCHAR(30) NOT NULL, \
            navios_tipo_1 INT NOT NULL, \
            navios_tipo_2 INT NOT NULL, \
            navios_tipo_3 INT NOT NULL, \
            navios_tipo_4 INT NOT NULL, \
            tamanho_tipo_1 INT NOT NULL, \
            tamanho_tipo_2 INT NOT NULL, \
            tamanho_tipo_3 INT NOT NULL, \
            tamanho_tipo_4 INT NOT NULL, \
            placar INT NOT NULL, \
            maximo_pontos INT NOT NULL \
            )")
        if log:
            print("Tabela Jogador criada")
        return 1
    except Exception as e:
        print("Tabela Jogador não foi criada", e)
        return 0

# insere valores na tabela jogador


def cria_jogador_banco(nome, navios_tipo_1, navios_tipo_2, navios_tipo_3, navios_tipo_4,
                             tamanho_tipo_1, tamanho_tipo_2, tamanho_tipo_3, tamanho_tipo_4,
                             placar, maximo_pontos, cursor, log=False):
    try:
        query = f"INSERT INTO Jogador(nome, navios_tipo_1, navios_tipo_2, navios_tipo_3, navios_tipo_4, \
                                            tamanho_tipo_1, tamanho_tipo_2, tamanho_tipo_3, tamanho_tipo_4, \
                                            placar, maximo_pontos) VALUES ('{nome}', {navios_tipo_1}, {navios_tipo_2}, {navios_tipo_3}, {navios_tipo_4}, \
                                            {tamanho_tipo_1}, {tamanho_tipo_2}, {tamanho_tipo_3}, {tamanho_tipo_4}, {placar}, {maximo_pontos})"
        cursor.execute(query)
        if log:
            print(cursor.rowcount, "Jogador inserido")
        return 1
    except Exception as e:
        raise e
        print("Não inseriu o jogador", e)
        return 0

# le o ultimo id jogador inserido


def le_ultimo_id_jogador(current_cursor, log=False):
    try:
        query = "SELECT @@IDENTITY"
        current_cursor.execute(query)
        last_id = current_cursor.fetchone()
        if log:
            print(current_cursor.rowcount, "Id jogador retornado")
        return last_id[0]
    except Exception as e:
        print("Id jogador não retornado", e)
        return 0

# atualiza algum row na tabela jogador


def atualiza_placar_jogador(id_jogador, placar, current_cursor, log=False):
    try:
        query = f"UPDATE Jogador SET placar={placar} WHERE id_jogador={id_jogador}"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, f"Placar do jogador {id_jogador} atualizado")
        return 1
    except Exception as e:
        print("Placar do jogador não foi atualizado", e)
        return 0

def atualiza_quantidade_navios_jogador(id_jogador, id_navio, quantidade, current_cursor, log=False):
    try:
        query = f"UPDATE Jogador SET navios_tipo_{id_navio + 1} = {quantidade} WHERE id_jogador={id_jogador}"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, f"Navios do jogador {id_jogador} atualizado")
        return 1
    except Exception as e:
        raise e
        print("Navios do jogador não foi atualizado", e)
        return 0

# deleta algum row na tabela jogador


def deleta_row_jogador(coluna_condicao, condicao, current_cursor, log=False):
    try:
        query = f"DELETE FROM Jogador WHERE {coluna_condicao}={condicao}"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Rows em Jogador removidos")
        return 1
    except Exception as e:
        print("Rows em Jogador não foram removidos", e)
        return 0

# remove a tabela jogador


def drop_tabela_jogador(current_cursor, log=False):
    try:
        query = f"DROP TABLE Jogador"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Tabela Jogador removida")
        return 1
    except Exception as e:
        print("Não removeu a Tabela Jogador", e)
        return 0
