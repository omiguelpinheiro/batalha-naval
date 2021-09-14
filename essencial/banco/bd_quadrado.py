from typing import Tuple, Union
from mysql.connector.cursor import CursorBase


def cria_tabela_quadrado(current_cursor: CursorBase, log: bool = False) -> int:
    """Cria a tabela Quadrado no banco de dados.

    Args:
        current_cursor (CursorBase): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        int: 1 se a tabela foi criada com sucesso.
             2 se a tabela não foi criada.
             
    """
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
        if log:
            print("Tabela Quadrado não foi criada", e)
        return 0


def cria_quadrado_banco(id_dono: int, linha: int, coluna: int, n_jogada: int, estado: str, id_navio: int, current_cursor: CursorBase, log: bool = False) -> int:
    """Cria um quadrado no banco de dados.

    Args:
        id_dono (int): Id do dono do quadrado.
        linha (int): Linha em que o quadrado está no tabuleiro.
        coluna (int): Coluna em que o quadrado está no tabuleiro.
        n_jogada (int): Jogada em que ele foi criado. 0 se antes do primeiro ataque feito.
        estado (str): O estado do navio no tabuleiro.
        id_navio (int): Id do navio a qual aquele quadrado pertence.
        current_cursor (CursorBase): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        int: 1 se o quadrado foi criado com sucesso.
             0 se o quadrado não foi criado.

    """
    try:
        query = f"INSERT INTO Quadrado(id_dono, linha, coluna, n_jogada, estado, id_navio) VALUES ({id_dono}, {linha}, {coluna}, {n_jogada}, '{estado}', {id_navio})"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Quadrado inserido")
        return 1
    except Exception as e:
        if log:
            print("Não inseriu o quadrado", e)
        return 0


def atualiza_quadrado(id_dono: int, linha: int, coluna: int, n_jogada: int, novo_estado: str, novo_id_navio: int, current_cursor: int, log: bool = False) -> int:
    """Atualiza um quadrado do banco de dados.

    Args:
        id_dono (int): Id do dono do quadrado.
        linha (int): Linha em que o quadrado está no tabuleiro.
        coluna (int): Coluna em que o quadrado está no tabuleiro.
        n_jogada (int): Jogada em que ele foi criado. 0 se antes do primeiro ataque feito.
        novo_estado (str): Novo estado que o navio assumirá.
        novo_id_navio (int): Novo id do navio ao qual aquele quadrado pertence.
        current_cursor (int): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        int: 1 se o quadrado foi atualizado com sucesso.
             0 se o quadrado não foi atualizado.

    """
    try:
        query = f"UPDATE Quadrado SET estado = '{novo_estado}', id_navio = {novo_id_navio} WHERE id_dono = {id_dono} AND linha = {linha} AND coluna = {coluna} AND n_jogada = {n_jogada}"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Quadrado atualizado")
        return 1
    except Exception as e:
        if log:
            print("Não atualizou o quadrado", e)
        return 0


def retorna_quadrados(current_cursor: CursorBase, log: bool = False) -> Union[Tuple, int]:
    """Retorna todos os quadrados que estão no banco de dados.

    Args:
        current_cursor (int): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        Union[List[Tuple], int]: Todos os quadrados que estão no banco ou 0 caso
            alguma coisa tenha dado errado.

    """
    try:
        query = 'SELECT * FROM Quadrado'
        current_cursor.execute(query)
        columns = [column[0] for column in current_cursor.description]
        rows = [dict(zip(columns, row)) for row in current_cursor.fetchall()]
        if log:
            print(current_cursor.rowcount, "Quadrados retornados")
        return rows
    except Exception as e:
        if log:
            print("Não retornou os quadrados", e)
        return 0


def dropa_tabela_quadrado(current_cursor: CursorBase, log: bool = False) -> int:
    """Deleta a tabela Quadrado do banco de dados.

    Args:
        current_cursor (int): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        int: 1 se a tabela foi removida com sucesso.
             0 se a tabela não foi removida.

    """
    try:
        query = 'DROP TABLE Quadrado'
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Tabela Quadrado removida")
        return 1
    except Exception as e:
        if log:
            print("Não removeu a Tabela Quadrado", e)
        return 0


def retorna_ultima_jogada(id_jogador_1: int, id_jogador_2: int, current_cursor: CursorBase, log: bool = False) -> int:
    """Retorna o número da última jogada feita na partida.

    Args:
        id_jogador_1 (int): Id do primeiro jogador da partida.
        id_jogador_2 (int): Id do segundo jogador da partida.
        current_cursor (int): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        int: O número da última jogada feita na partida ou -1 caso alguma coisa
            tenha dado errado.

    """
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
        if log:
            print("Não obteve a ultima jogada", e)
        return -1
