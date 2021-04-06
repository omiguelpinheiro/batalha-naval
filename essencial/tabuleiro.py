from essencial import quadrado
from essencial import util

__all__ = ["gera_tabuleiro", "mostra_tabuleiro"]  # O que será importado com "import tabuleiro"


def gera_tabuleiro() -> int:
    """Função que gera um tabuleiro.

    Returns:
        Retorna o tabuleiro criado.

    """
    tabuleiro = [[{} for coluna in range(quadrado.consulta_numero_colunas())] for linha in range(quadrado.consulta_numero_colunas())]
    for y, linha in enumerate(tabuleiro):
        for x, coluna in enumerate(linha):
            tabuleiro[y][x] = quadrado.gera_quadrado("N")

    return tabuleiro


def mostra_tabuleiro(tabuleiro: list):
    """Função que mostra uma representação do estado atual do tabuleiro.

    Args:
        tabuleiro: Uma lista de listas de quadrados, representando o tabuleiro
            que tem-se interesse em ver.

    """
    print("WAR ", end="")
    for x in range(len(tabuleiro[0])):
        print(x, end=" ")
    print()
    for y, linha in enumerate(tabuleiro):
        print(util.converte_numero_letra(y), end=" - ")
        for x, coluna in enumerate(linha):
            print(tabuleiro[y][x]["estado"], end=" ")
        print()
