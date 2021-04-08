from essencial import quadrado

__all__ = ["gera_tabuleiro"]  # O que será importado com "import tabuleiro"


def gera_tabuleiro() -> int:
    """Função que gera um tabuleiro.

    Returns:
        Retorna o tabuleiro criado.

    """
    tabuleiro = [[{} for coluna in range(quadrado.consulta_numero_colunas())] for linha in range(quadrado.consulta_numero_colunas())]
    for y, linha in enumerate(tabuleiro):
        for x, coluna in enumerate(linha):
            tabuleiro[y][x] = quadrado.gera_quadrado()

    return tabuleiro
