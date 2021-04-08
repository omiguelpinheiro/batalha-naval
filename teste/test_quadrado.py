from essencial import quadrado


class TestaMetodosQuadrado:
    def testa_gera_quadrado_sucesso(self):
        quad = {"estado": "N", "estado_visivel": "N"}
        retorno = quadrado.gera_quadrado()
        assert retorno == quad

    def testa_altera_quadrado_estado_sucesso(self):
        esperado = {"estado": "H", "estado_visivel": "N"}
        original = quadrado.gera_quadrado()
        retorno = quadrado.altera_estado(original, "H")
        assert retorno == esperado

    def testa_altera_quadrado_estado_falha(self):
        esperado = {"estado": "E", "estado_visivel": "N"}
        original = quadrado.gera_quadrado()
        retorno = quadrado.altera_estado(original, "G")
        assert retorno == esperado

    def testa_consulta_numero_linhas(self):
        esperado = quadrado._NUMERO_LINHAS
        retorno = quadrado.consulta_numero_linhas()
        assert retorno == esperado

    def testa_consulta_numero_colunas(self):
        esperado = quadrado._NUMERO_COLUNAS
        retorno = quadrado.consulta_numero_colunas()
        assert retorno == esperado
