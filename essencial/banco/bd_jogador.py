from typing import List, Tuple, Union
from mysql.connector.cursor import CursorBase


def cria_tabela_jogador(current_cursor: CursorBase, log: bool = False) -> int:
    """Cria tabela Jogador onde os dados do jogador ficarão.

    Args:
        current_cursor (CursorBase): Cursor aberto que executará as queries.
        log (bool, optional): [description]. Ativa e desativa o logging.

    Returns:
        int: 1 se a tabela for criada com sucesso.
             0 se a tabela não for criada.

    """
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
        if log:
            print("Tabela Jogador não foi criada", e)
        return 0


def cria_jogador_banco(nome: str, navios_tipo_1: int, navios_tipo_2: int, navios_tipo_3: int, navios_tipo_4: int,
                             tamanho_tipo_1: int, tamanho_tipo_2: int, tamanho_tipo_3: int, tamanho_tipo_4: int,
                             placar: int, maximo_pontos: int, current_cursor: CursorBase, log: bool = False) -> int:
    """Insere um jogador no banco de dados.

    Args:
        nome (str): Nome do jogador.
        navios_tipo_1 (int): Navios do tipo 1 ainda a ser posicionados.
        navios_tipo_2 (int): Navios do tipo 2 ainda a ser posicionados.
        navios_tipo_3 (int): Navios do tipo 3 ainda a ser posicionados.
        navios_tipo_4 (int): Navios do tipo 4 ainda a ser posicionados.
        tamanho_tipo_1 (int): Tamanho do navio tipo 1 para essa partida.
        tamanho_tipo_2 (int): Tamanho do navio tipo 2 para essa partida.
        tamanho_tipo_3 (int): Tamanho do navio tipo 3 para essa partida.
        tamanho_tipo_4 (int): Tamanho do navio tipo 4 para essa partida.
        placar (int): Placar do jogador.
        maximo_pontos (int): Pontos que o jogador precisa para vencer essa partida.
        current_cursor (CursorBase): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        int: 1 se o jogador foi inserido com sucesso.
             0 se o jogador não foi inserido.

    """
    try:
        query = f"INSERT INTO Jogador(nome, navios_tipo_1, navios_tipo_2, navios_tipo_3, navios_tipo_4, \
                                            tamanho_tipo_1, tamanho_tipo_2, tamanho_tipo_3, tamanho_tipo_4, \
                                            placar, maximo_pontos) VALUES ('{nome}', {navios_tipo_1}, {navios_tipo_2}, {navios_tipo_3}, {navios_tipo_4}, \
                                            {tamanho_tipo_1}, {tamanho_tipo_2}, {tamanho_tipo_3}, {tamanho_tipo_4}, {placar}, {maximo_pontos})"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Jogador inserido")
        return 1
    except Exception as e:
        if log:
            print("Não inseriu o jogador", e)
        return 0


def le_ultimo_id_jogador(current_cursor: CursorBase, log: bool = False) -> int:
    """Retorna do banco de dados o maior id_jogador da tabela Jogador.

    Args:
        current_cursor (CursorBase): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        int: O maior id_jogador registrado no banco de dados caso dê certo.
             -1 caso algum erro ocorra.

    """
    try:
        query = "SELECT id_jogador FROM Jogador ORDER BY id_jogador DESC LIMIT 1"
        current_cursor.execute(query)
        last_id = current_cursor.fetchone()
        if log:
            print(current_cursor.rowcount, "Id jogador retornado")
        return last_id[0]
    except Exception as e:
        if log:
            print("Id jogador não retornado", e)
        return -1

# atualiza algum row na tabela jogador
def atualiza_placar_jogador(id_jogador: int, placar: int, current_cursor: CursorBase, log: bool = False) -> int:
    """Atualiza o placar do jogador no banco de dados.

    Args:
        id_jogador (int): A id do jogador que será atualizado.
        placar (int): O novo placar do jogador.
        current_cursor (CursorBase): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        int: 1 se o jogador foi atualizado no banco de dados.
             0 se o jogador não foi atualizado.

    """
    try:
        query = f"UPDATE Jogador SET placar={placar} WHERE id_jogador={id_jogador}"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, f"Placar do jogador {id_jogador} atualizado")
        return 1
    except Exception as e:
        if log:
            print("Placar do jogador não foi atualizado", e)
        return 0


def atualiza_quantidade_navios_jogador(id_jogador: int, id_navio: int, quantidade: int, current_cursor: CursorBase, log: bool = False) -> int:
    """Atualiza no banco de dados a quantidade de navios de um tipo que um jogador tem.

    Args:
        id_jogador (int): A id do jogador que será atualizado.
        id_navio (int): A id do navio que será atualizado.
        quantidade (int): Qual a nova quantidade de navios que o jogador tem.
        current_cursor (CursorBase): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        int: 1 se o jogador teve seus navios atualizados.
             0 se o jogador não teve seus navios atualizados.

    """
    try:
        query = f"UPDATE Jogador SET navios_tipo_{id_navio + 1} = {quantidade} WHERE id_jogador={id_jogador}"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, f"Navios do jogador {id_jogador} atualizado")
        return 1
    except Exception as e:
        if log:
            print("Navios do jogador não foi atualizado", e)
        return 0


def retorna_jogador(id_jogador: int, current_cursor: CursorBase, log: bool = False) -> Union[Tuple, int]:
    """Obtém um jogador do banco de dados.

    Args:
        id_jogador (int): Id do jogador que se deseja obter.
        current_cursor (CursorBase): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        Union[Tuple, int]: Tupla com os dados do jogador caso tenha funcionado ou
            0 caso alguma coisa tenha dado errado.

    """
    try:
        query = f"SELECT * FROM Jogador WHERE id_jogador={id_jogador}"
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, f"Jogador {id_jogador} selecionado")
        return current_cursor.fetchone()
    except Exception as e:
        if log:
            print("Jogador não foi selecionado", e)
        return 0


def retorna_jogadores(current_cursor: CursorBase, log: bool = False) -> List[Tuple]:
    """Retorna todos os jogadores que estão no banco de dados.

    Args:
        current_cursor (CursorBase): Cursor aberto que executará as queries.
        log (bool, optional): Ativa e desativa o logging. Default é False.

    Returns:
        List[Tuple]: Todos os jogadores que estão no banco de dados.

    """
    try:
        query = 'SELECT * FROM Jogador'
        current_cursor.execute(query)
        columns = [column[0] for column in current_cursor.description]
        rows = [dict(zip(columns, row)) for row in current_cursor.fetchall()]
        if log:
            print(current_cursor.rowcount, "Jogadores retornados")
        return rows
    except Exception as e:
        if log:
            print("Não retornou os jogadores", e)
        return 0


def dropa_tabela_jogador(current_cursor: CursorBase, log: bool = False) -> int:
    """Deleta a tabela Jogador do banco de dados.

    Args:
        current_cursor (CursorBase): [description]
        log (bool, optional): [description]. Defaults to False.

    Returns:
        int: [description]
        
    """
    try:
        query = 'DROP TABLE Jogador'
        current_cursor.execute(query)
        if log:
            print(current_cursor.rowcount, "Tabela Jogador removida")
        return 1
    except Exception as e:
        if log:
            print("Não removeu a Tabela Jogador", e)
        return 0
