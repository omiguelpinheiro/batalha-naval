from essencial import tabuleiro

__all__ = ["consulta_jogador", "registra_jogador", "_jogadores"]  # O que será importado com "import jogador"

_jogadores: list = []  # Lista de jogadores registrados até o momento.


def registra_jogador(nome: str) -> int:
    """Função que registra um jogador em _jogadores.

    Args:
        nome: Nome do jogador a ser inserido.

    Returns:
        0 se já existem dois jogadores registrados e 1 caso tenha registrado com sucesso.

    """
    jogadores = _lista_jogadores()

    jogador = dict()
    jogador["nome"] = nome
    jogador["placar"] = 28

    if len(jogadores) == 0:
        jogador["id"] = 0
    elif len(jogadores) == 1:
        jogador["id"] = 1
    else:
        return 0

    _registra_tabuleiro(jogador)

    _jogadores.append(jogador)
    return 1


def consulta_jogador(id_jogador: int) -> dict:
    """Função que retorna um dicionário com as informações do jogador
    especificado por id_jogador.

    Args:
        id_jogador: ID do jogador cujas informações deseja-se obter.

    Returns:
        Dicionário com as informações do jogador especificado ou um
            dicionário vazio caso o jogador não seja encontrado.

    """
    jogadores = _lista_jogadores()
    for jogador in jogadores:
        if jogador["id"] == id_jogador:
            return jogador
    return _jogadores


def _lista_jogadores() -> list:
    """Função que retorna a lista de jogadores atualmente na partida.

    Returns:
        list: Lista dos jogadores registrados atualmente.

    """
    jogadores = _jogadores
    return jogadores


def _registra_tabuleiro(jogador: dict):
    """Adiciona o tabuleiro ao jogador.

    Args:
        jogador: Jogador que receberá o tabuleiro.

    """
    tab = tabuleiro.gera_tabuleiro()
    jogador["tabuleiro"] = tab
    return jogador
