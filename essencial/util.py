import string
import numbers

__all__ = ["converte_letra_numero", "converte_numero_letra"]  # O que será importado com "import util"

_dicionario_numero_letra: dict = {}  # Mapeia números para letras em ordem alfabética
_dicionario_letra_numero: dict = {}  # Mapeia letras para números em ordem crescente


def converte_letra_numero(let: str) -> int:
    """Converte uma letra para um número, sendo a = 0, B = 1, c = 2
        e assim por diante.

    Args:
        let: A letra cujo número se deseja descobrir.

    Returns:
        O número que representa a letra ou -1 se não foi passada uma letra.

    """
    if let not in string.ascii_letters:
        return -1
    letra_numero = _recebe_dicionario_letra_numero()
    let = let.upper()
    return letra_numero[let]


def converte_numero_letra(numero: int) -> str:
    """Converte um número para uma letra, sendo 0 = A, 1 = B, 2 = C e
        assim por diante.

    Args:
        numero: A letra cujo número se deseja descobrir.

    Returns:
        A letra que representa o número ou exclamação ("!") caso tenha passado
            um número inválido.

    """
    if not isinstance(numero, numbers.Number):
        return "!"
    numero_letra = _recebe_dicionario_numero_letra()
    numero = numero
    return numero_letra[numero]


def _recebe_dicionario_letra_numero() -> dict:
    """Retorna o dicionário com os valores que cada letra tem.

    Returns:
        Dicionário com valores de cada letra.

    """

    return _dicionario_letra_numero


def _recebe_dicionario_numero_letra() -> dict:
    """Retorna o dicionário com os valores que cada letra tem.

    Returns:
        Dicionário com valores de cada letra.

    """

    return _dicionario_numero_letra


def _cria_dicionario_letra_numero():
    """Cria dicionário que mapeia uma letra para um número.

    O dicionário mapeia a para 1, b para 2, c para 3 e assim por diante.

    Returns:
        Um dicionario que mapeia de uma letra para um número.

    """
    letras = string.ascii_uppercase

    return {letra: indice for indice, letra in enumerate(letras)}


def _cria_dicionario_numero_letra():
    """Cria dicionário que mapeia um número para uma letra.

    O dicionário mapeia 1 para a, 2 para b, 3 para c e assim por diante.

    Returns:
        Um dicionário que mapeia de um número para uma letra.

    """
    letras = string.ascii_uppercase

    return {indice: letra for indice, letra in enumerate(letras)}


_dicionario_numero_letra = _cria_dicionario_numero_letra()
_dicionario_letra_numero = _cria_dicionario_letra_numero()
