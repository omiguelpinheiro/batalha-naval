from essencial.banco.conector import abre_cursor, conecta_servidor


def cria_tabela_quadrado(con):
    try:
        cursor = abre_cursor(con)
        cursor.execute("CREATE TABLE Quadrado ( \
            id_dono INT NOT NULL, \
            linha CHAR(1) NOT NULL, \
            coluna CHAR(1) NOT NULL, \
            n_jogada INT NOT NULL, \
            estado CHAR(1) NOT NULL,  \
            PRIMARY KEY (id_dono, linha, coluna, n_jogada), \
            CONSTRAINT FK_JogadorQuadrado FOREIGN KEY (id_dono) REFERENCES Jogador(id_jogador) \
            CONSTRAINT FK_JogadorQuadrado FOREIGN KEY (id_dono) REFERENCES Jogador(id_jogador) \
            )")
        con.commit()
        print("Tabela Quadrado criada")
        cursor.close()
        return 1
    except Exception as e:
        print("Tabela Quadrado não foi criada", e)
        return 0


def cria_quadrado_banco(id_dono, linha, coluna, n_jogada, estado, con):
    try:
        cursor = abre_cursor(con)
        query = f"INSERT INTO Quadrado(id_dono, linha, coluna, n_jogada, estado) VALUES ({id_dono}, {linha}, {coluna}, {n_jogada}, {estado})"
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount, "Quadrado inserido")
        cursor.close()
        return 1
    except Exception as e:
        print("Não inseriu o quadrado", e)
        return 0


def atualiza_quadrado(coluna, novo_valor, coluna_condicao, condicao, con):
    try:
        cursor = abre_cursor(con)
        query = f"UPDATE Quadrado SET {coluna}={novo_valor} WHERE {coluna_condicao}={condicao}"
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount, "Quadrado atualizado")
        cursor.close()
        return 1
    except Exception as e:
        print("Não atualizou o quadrado", e)
        return 0


def deleta_partida(coluna_condicao, condicao, con):
    try:
        cursor = abre_cursor(con)
        query = f"DELETE FROM Quadrado WHERE {coluna_condicao}={condicao}"
        cursor.execute(query)
        con.commit()
        print(cursor.rowcount, "Quadrado removido")
        cursor.close()
        return 1
    except Exception as e:
        print("Não removeu o quadrado", e)
        return 0

cria_tabela_quadrado(con)