# cria tabela quadrado no banco


def cria_tabela_quadrado(current_cursor, log=False):
    try:
        current_cursor.execute("CREATE TABLE Quadrado ( \
            id_dono INT NOT NULL, \
            linha CHAR(1) NOT NULL, \
            coluna CHAR(1) NOT NULL, \
            n_jogada INT NOT NULL, \
            estado CHAR(1) NOT NULL,  \
            id_navio INT NOT NULL, \
            PRIMARY KEY (id_dono, linha, coluna, n_jogada), \
            CONSTRAINT FK_JogadorQuadrado FOREIGN KEY (id_dono) REFERENCES Jogador(id_jogador))")
        if log:
            print("Tabela Quadrado criada")
        return 1
    except Exception as e:
        print("Tabela Quadrado não foi criada", e)
        return 0

# insere valores no banco quadrado


def cria_quadrado_banco(id_dono, linha, coluna, n_jogada, estado, id_navio, current_cursor, log=False):
    try:
        query = f"INSERT INTO Quadrado(id_dono, linha, coluna, n_jogada, estado, id_navio) VALUES ({id_dono}, {linha}, {coluna}, {n_jogada}, '{estado}', {id_navio})"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Quadrado inserido")
        return 1
    except Exception as e:
        raise e
        print("Não inseriu o quadrado", e)
        return 0

# atualiza algum row na tabela quadrado


def atualiza_quadrado(id_dono, linha, coluna, n_jogada, novo_estado, novo_id_navio, current_cursor, log=False):
    try:
        query = f"UPDATE Quadrado SET estado = '{novo_estado}', id_navio = {novo_id_navio} WHERE id_dono = {id_dono} AND linha = {linha} AND coluna = {coluna} AND n_jogada = {n_jogada}"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Quadrado atualizado")
        return 1
    except Exception as e:
        print("Não atualizou o quadrado", e)
        return 0

# remove algum row na tabela quadrado


def deleta_row_quadrado(coluna_condicao, condicao, current_cursor, log=False):
    try:
        query = f"DELETE FROM Quadrado WHERE {coluna_condicao}={condicao}"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Rows em Quadrado removidos")
        return 1
    except Exception as e:
        print("Rows em Quadrado não foram removidos", e)
        return 0

# remove a tabela quadrado do banco


def drop_tabela_quadrado(current_cursor, log=False):
    try:
        query = f"DROP TABLE Quadrado"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Tabela Quadrado removida")
        return 1
    except Exception as e:
        print("Não removeu a Tabela Quadrado", e)
        return 0

def retorna_ultima_jogada(id_jogador_1, id_jogador_2, current_cursor, log=False):
    try:
        query_1 = f"SELECT MAX(n_jogada) FROM Quadrado WHERE id_dono = {id_jogador_1}"
        current_cursor.execute(query_1)
        max_jogador_1 = current_cursor.fetchone()[0]
        query_2 = f"SELECT MAX(n_jogada) FROM Quadrado WHERE id_dono = {id_jogador_2}"
        current_cursor.execute(query_2)
        max_jogador_2 = current_cursor.fetchone()[0]
        ultima_jogada = max(max_jogador_1, max_jogador_2)
        if log:
            print(current_cursor.rowcount, "Ultima jogada obtida")
        return ultima_jogada
    except Exception as e:
        print("Não obteve a ultima jogada", e)
        return -1
