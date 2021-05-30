from essencial.banco.conector import abre_cursor, con, conecta_servidor

# cria tabela quadrado no banco


def cria_tabela_quadrado(con):
    try:
        cursor = abre_cursor(con)
        cursor.execute("CREATE TABLE Quadrado ( \
            id_dono INT NOT NULL, \
            linha CHAR(1) NOT NULL, \
            coluna CHAR(1) NOT NULL, \
            n_jogada INT NOT NULL, \
            estado CHAR(1) NOT NULL,  \
            id_navio INT NOT NULL, \
            PRIMARY KEY (id_dono, linha, coluna, n_jogada), \
            CONSTRAINT FK_JogadorQuadrado FOREIGN KEY (id_dono) REFERENCES Jogador(id_jogador))")
        con.commit()
        print("Tabela Quadrado criada")
        cursor.close()
        return 1
    except Exception as e:
        print("Tabela Quadrado não foi criada", e)
        return 0

# insere valores no banco quadrado


def cria_quadrado_banco(id_dono, linha, coluna, n_jogada, estado, id_navio, con, log=False):
    try:
        cursor = abre_cursor(con)
        query = f"INSERT INTO Quadrado(id_dono, linha, coluna, n_jogada, estado, id_navio) VALUES ({id_dono}, {linha}, {coluna}, {n_jogada}, '{estado}', {id_navio})"
        cursor.execute(query)
        con.commit()
        if log:
            print(cursor.rowcount, "Quadrado inserido")
        cursor.close()
        return 1
    except Exception as e:
        print("Não inseriu o quadrado", e)
        return 0

# atualiza algum row na tabela quadrado


def atualiza_quadrado(id_dono, linha, coluna, n_jogada, novo_estado, novo_id_navio, con):
    try:
        cursor = abre_cursor(con)
        query = f"UPDATE Quadrado SET estado = '{novo_estado}', id_navio = {novo_id_navio} WHERE id_dono = {id_dono} AND linha = {linha} AND coluna = {coluna} AND n_jogada = {n_jogada}"
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount, "Quadrado atualizado")
        cursor.close()
        return 1
    except Exception as e:
        print("Não atualizou o quadrado", e)
        return 0

# remove algum row na tabela quadrado


def deleta_row_quadrado(coluna_condicao, condicao, con):
    try:
        cursor = abre_cursor(con)
        query = f"DELETE FROM Quadrado WHERE {coluna_condicao}={condicao}"
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount, "Rows em Quadrado removidos")
        cursor.close()
        return 1
    except Exception as e:
        print("Rows em Quadrado não foram removidos", e)
        return 0

# remove a tabela quadrado do banco


def drop_tabela_quadrado(con):
    try:
        cursor = abre_cursor(con)
        query = f"DROP TABLE Quadrado"
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount, "Tabela Quadrado removida")
        cursor.close()
        return 1
    except Exception as e:
        print("Não removeu a Tabela Quadrado", e)
        return 0

def retorna_ultima_jogada(id_jogador_1, id_jogador_2, con):
    try:
        cursor = abre_cursor(con)
        query_1 = f"SELECT MAX(n_jogada) FROM Quadrado WHERE id_dono = {id_jogador_1}"
        cursor.execute(query_1)
        con.commit()
        max_jogador_1 = cursor.fetchone()[0]
        query_2 = f"SELECT MAX(n_jogada) FROM Quadrado WHERE id_dono = {id_jogador_2}"
        cursor.execute(query_2)
        con.commit()
        max_jogador_2 = cursor.fetchone()[0]
        ultima_jogada = max(max_jogador_1, max_jogador_2)
        print(cursor.rowcount, "Ultima jogada obtida")
        cursor.close()
        return ultima_jogada
    except Exception as e:
        print("Não obteve a ultima jogada", e)
        return -1

cria_tabela_quadrado(con)
