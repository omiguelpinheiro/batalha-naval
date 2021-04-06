from typing import Optional, List, Dict

__all__ = ["gera_quadrado", "consulta_estado", "altera_estado"]  # O que será importado com "import quadrado"

_NUMERO_LINHAS: int = 10  # Número de linhas no tabuleiro
_NUMERO_COLUNAS: int = 10  # Número de colunas no tabuleiro


def gera_quadrado(estado: str, componentes: Optional[dict] = {}) -> dict:
    """Função que gera um quadrado para ser posicionado no tabuleiro.

    Args:
        estado: Estado do quadrado a ser posicionado.
        componentes: Dicionário especificando onde se encontram as outras
            partes do navio.

    Returns:
        O quadrado com estado e componentes incluídos caso o estado passado
            seja reconhecido ou um quadrado com estado ? caso contrário.

    """
    estado = estado.upper()
    if estado not in ["H", "D", "N", "W"]:
        quadrado = {"estado": "?", "componentes": componentes}
        return quadrado

    quadrado = {"estado": estado, "componentes": componentes}
    return quadrado


def consulta_estado(quadrado: dict) -> str:
    """Função que diz qual a situação do quadrado em questão.

    Args:
        quadrado: As informações do quadrado cujo estado deseja-se consultar.

    Returns:
        Uma letra representando o estado do quadrado que pode ser:
            H se tem um navio mas está oculto.
            D se tem um navio que foi atacado.
            N se não tem um navio mas está oculto.
            W se não tem um navio e foi atacado.

    """
    estado = quadrado["estado"]
    return estado


def altera_estado(quadrado: dict, novo_estado: str) -> dict:
    """Função que altera o estado do quadrado para novo_estado.

    Args:
        quadrado: O quadrado cujo estado será alterado.
        novo_estado: O novo estado do quadrado.

    Returns:
        Um quadrado com o estado alterado para ? se o estado passado
            não puder ser aceito, ou um quadrado com o estado alterado
            para novo_estado.

    """
    novo_estado = novo_estado.upper()

    if novo_estado not in ["H", "D", "N", "W"]:
        quadrado["estado"] = "?"
        return quadrado

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
