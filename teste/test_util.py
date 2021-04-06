from essencial import util
from teste.fixture.util_fixture import dicionario_numero_letra, dicionario_letra_numero


class TestaMetodosUtil:
    def testa__cria_dicionario_numero_letra(self):
        util._cria_dicionario_numero_letra()
        assert util._dicionario_numero_letra == dicionario_numero_letra

    def testa__cria_dicionario_letra_numero(self):
        util._cria_dicionario_letra_numero()
        assert util._dicionario_letra_numero == dicionario_letra_numero

    def testa__recebe_dicionario_numero_letra(self):
        numero_letra = util._recebe_dicionario_numero_letra()
        assert numero_letra == dicionario_numero_letra

    def testa__recebe_dicionario_letra_numero(self):
        letra_numero = util._recebe_dicionario_letra_numero()
        assert letra_numero == dicionario_letra_numero

    def testa_converte_letra_numero_sucesso(self):
        retorno = util.converte_letra_numero("s")
        assert retorno == 18

    def testa_converte_letra_numero_falha(self):
        retorno = util.converte_letra_numero("´")
        assert retorno == -1

    def testa_converte_numero_letra_sucesso(self):
        retorno = util.converte_numero_letra(5)
        assert retorno == "F"

    def testa_converte_numero_letra_falha(self):
        retorno = util.converte_numero_letra("x")
        assert retorno == "!"
