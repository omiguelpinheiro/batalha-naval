from typing import Optional, List, Dict

__all__ = ["gera_quadrado", "consulta_estado", "altera_estado"]  # O que será importado com "import quadrado"

_NUMERO_LINHAS: int = 10  # Número de linhas no tabuleiro
_NUMERO_COLUNAS: int = 10  # Número de colunas no tabuleiro


def gera_quadrado() -> dict:
    """Gera um quadrado para ser posicionado no tabuleiro.

    O quadrado será um dicionário com entradas "estado" = "N" e
    "estado_visivel" = "N".

    Os estados possíveis para a chave "estado" são:
        H se tem um navio mas está oculto.
        D se tem um navio que foi atacado.
        N se não tem um navio e não foi atacado.
        W se não tem um navio e foi atacado.

    Os estados possíveis para a chave "estado_visivel" são:
        N se não tem um navio e não foi atacado.
        D se tem um navio que foi atacado.
        W se não tem um navio e foi atacado.

    Returns:
        Um quadrado.

    """
    return {"estado": "N", "estado_visivel": "N"}


def consulta_estado(quadrado: dict) -> str:
    """Diz qual o estado interno do quadrado.

    Args:
        quadrado: O quadrado cujo estado deseja-se consultar.

    Returns:
        Uma letra representando o estado do quadrado que pode ser:
            H se tem um navio mas está oculto.
            D se tem um navio que foi atacado.
            N se não tem um navio e não foi atacado.
            W se não tem um navio e foi atacado.

    """
    return quadrado["estado"]


def altera_estado(quadrado: dict, novo_estado: str) -> dict:
    """Altera o estado do quadrado.

    Args:
        quadrado: O quadrado cujo estado será alterado.
        novo_estado: O novo estado do quadrado.

    Returns:
        A função retornará:
            Um quadrado com o estado alterado para novo_estado caso
                nenhum problema ocorra.
            Um quadrado com o estado alterado para E se o estado passado
                não puder ser aceito.

    """
    novo_estado = novo_estado.upper()
    if novo_estado not in ["H", "D", "N", "W"]:
        # Checa erro de estado
        quadrado["estado"] = "E"
    else:
        # Tudo certo
        quadrado["estado"] = novo_estado
    return quadrado


def consulta_numero_linhas():
    """Obtém o número de linhas no tabuleiro

    Returns:
        Número de linhas no tabuleiro
    """
    return _NUMERO_LINHAS


def consulta_numero_colunas():
    """Obtém o número de colunas no tabuleiro

    Returns:
        Número de colunas no tabuleiro
    """
    return _NUMERO_COLUNAS
