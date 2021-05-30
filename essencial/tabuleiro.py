from essencial import quadrado
from essencial.banco.bd_quadrado import *

__all__ = ["gera_tabuleiro"]  # O que será importado com "import tabuleiro"


def gera_tabuleiro(id_jogador_banco) -> int:
    """Função que gera um tabuleiro.

    Returns:
        Retorna o tabuleiro criado.

    """
    tabuleiro = [[{} for coluna in range(quadrado.consulta_numero_colunas())] for linha in range(quadrado.consulta_numero_linhas())]
    for y, linha in enumerate(tabuleiro):
        for x, coluna in enumerate(linha):
            tabuleiro[y][x] = quadrado.gera_quadrado()
            cria_quadrado_banco(id_jogador_banco, x, y, 0, "N", -1, con)
    return tabuleiro
