from mysql.connector.cursor import CursorBase
from typing import Tuple, Union


def cria_tabela_partida(current_cursor: CursorBase, log: bool = False) -> int:
    """Cria tabela Partida onde os dados da partida ficarão.

    Args:
        current_cursor (CursorBase): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        int: 1 se a tabela for criada com sucesso.
             0 se a tabela não for criada.
             
    """
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
        if log:
            print("Tabela Partida não foi criada", e)
        return 0


def cria_partida_banco(id_jogador1: int, id_jogador2: int, current_cursor: CursorBase, log: bool = False) -> int:
    """[summary]

    Args:
        id_jogador1 (int): Id do jogador 1 no banco.
        id_jogador2 (int): Id do jogador 2 no banco.
        current_cursor (CursorBase): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        int: 1 se a partida for criada com sucesso.
             0 se a partida não for criada.

    """
    try:
        query = f"INSERT INTO Partida(id_jogador1, id_jogador2, n_ultima_jogada, finalizada, vencedor) VALUES ({id_jogador1}, {id_jogador2}, 0, false, -1)"
        current_cursor.execute(query)
        if log:
            print("Partida inserida")
        return 1
    except Exception as e:
        if log:
            print("Não inseriu a partida", e)
        return 0


def le_ultimo_id_partida(current_cursor: CursorBase, log: bool = False) -> int:
    """Retorna o último id da tabela Partida do banco.

    Args:
        current_cursor (CursorBase): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        int: O id da última partida inserida no banco ou -1 caso alguma coisa
            tenha dado errado.

    """
    try:
        query =  "SELECT id_partida FROM Partida ORDER BY id_partida DESC LIMIT 1"
        current_cursor.execute(query)
        last_id = current_cursor.fetchone()
        if log:
            print(current_cursor.rowcount, "Id partida retornado")
        return last_id[0]
    except Exception as e:
        if log:
            print("Id partida não retornado", e)
        return -1


def finaliza_partida(id_partida: int, id_vencedor: int, current_cursor: int, log: bool = False) -> int:
    """Atribui um vencedor à coluna vencedor a uma linha de Jogador.

    Args:
        id_partida (int): Id da partida que estamos atualizando.
        id_vencedor (int): Id do jogador vencedor.
        current_cursor (CursorBase): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        int: 1 se a partida foi atualizada com sucesso.
             0 se a partida não foi atualizada.

    """
    try:
        query = f"UPDATE Partida SET finalizada=TRUE, vencedor={id_vencedor} WHERE id_partida={id_partida}"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Partida atualizada")
        return 1
    except Exception as e:
        if log:
            print("Não atualizou a partida", e)
        return 0


def atualiza_ultima_rodada(id_partida: int, ultima_rodada: int, current_cursor: CursorBase, log: bool = False) -> int:
    """Atualizad uma partida no banco de dados.

    Args:
        id_partida (int): Id da partida que estamos atualizando.
        ultima_rodada (int): Novo valor par a última rodada.
        current_cursor (CursorBase): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        int: 1 se a partida foi atualizada com sucesso.
             0 se a partida não foi atualizada.

    """
    try:
        query = f"UPDATE Partida SET n_ultima_jogada={ultima_rodada} WHERE id_partida={id_partida}"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Última rodada da partida atualizada")
        return 1
    except Exception as e:
        if log:
            print("Não atualizou a última rodada da partida", e)
        return 0


def retorna_partidas(current_cursor: CursorBase, log: bool = False) -> Union[Tuple, int]:
    """Retorna todas as partidas que estão no banco de dados.

    Args:
        current_cursor (CursorBase): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        Union[Tuple, int]: Todas as partidas que estão no banco de dados ou
            0 caso tenha ocorrido algumm problema.

    """
    try:
        query = 'SELECT * FROM Partida'
        current_cursor.execute(query)
        columns = [column[0] for column in current_cursor.description]
        rows = [dict(zip(columns, row)) for row in current_cursor.fetchall()]
        if log:
            print(current_cursor.rowcount, "Partidas retornadas")
        return rows
    except Exception as e:
        if log:
            print("Não retornou as partidas", e)
        return 0
    

def dropa_tabela_partida(current_cursor: CursorBase, log: bool = False) -> int:
    """Deleta a tabela Partida do banco de dados.

    Args:
        current_cursor (CursorBase): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        int: 1 se a tabela foi deletada com sucesso.
             0 se a tabela não foi deletada.
             
    """
    try:
        query = 'DROP TABLE Partida'
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Tabela Partida removida")
        return 1
    except Exception as e:
        if log:
            print("Não removeu a Tabela Partida", e)
        return 0
