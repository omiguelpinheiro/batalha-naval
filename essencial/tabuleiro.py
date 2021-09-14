from typing import Dict
from essencial import quadrado
from essencial.banco.conector import abre_cursor
from essencial.banco.bd_quadrado import *

__all__ = ["gera_tabuleiro"]  # O que será importado com "import tabuleiro"


def gera_tabuleiro(id_jogador_banco: int, cursor: CursorBase) -> Union[Dict, int]:
    """Função que gera um tabuleiro.

    args:
        id_jogador_banco (int): A id do jogador no banco de dados.
        current_cursor (CursorBase): Cursor aberto que executará as queries.

    Returns:
        Retorna o tabuleiro criado ou -1 caso não tenha sido criado com sucesso.

    """
    tabuleiro = gera_tabuleiro_vazio()
    for y, linha in enumerate(tabuleiro):
        for x, coluna in enumerate(linha):
            tabuleiro[y][x] = quadrado.gera_quadrado()
            retorno = cria_quadrado_banco(id_jogador_banco, x, y, 0, "N", -1, cursor)
            if retorno == 0:
                return -1
    return tabuleiro

def gera_tabuleiro_vazio() -> Dict:
    """Cria um tabuleiro vazio.

    Returns:
        Dict: Tabuleiro vazio.
        
    """
    return [
        [{} for coluna in range(quadrado.consulta_numero_colunas())]
        for linha in range(quadrado.consulta_numero_linhas())
    ]