from essencial import quadrado


class TestaMetodosQuadrado:
    def testa_gera_quadrado_sucesso(self):
        quad = {"estado": "H", "componentes": {}}
        retorno = quadrado.gera_quadrado("H")
        assert retorno == quad

    def testa_gera_quadrado_falha(self):
        quad = {"estado": "?", "componentes": {}}
        retorno = quadrado.gera_quadrado("G")
        assert retorno == quad

    def testa_gera_quadrado_com_componentes(self):
        quad = {"estado": "H", "componentes": {"esquerda": False, "cima": True, "direita": False, "baixo": True}}
        retorno = quadrado.gera_quadrado("H", {"esquerda": False, "cima": True, "direita": False, "baixo": True})
        assert retorno == quad

    def testa_consulta_estado(self):
        quad = quadrado.gera_quadrado("H")
        retorno = quadrado.consulta_estado(quad)
        assert retorno == "H"

    def testa_altera_estado_sucesso(self):
        quad = quadrado.gera_quadrado("H")
        retorno = quadrado.altera_estado(quad, "N")
        assert retorno == {"estado": "N", "componentes": {}}

    def testa_altera_estado_falha(self):
        quad = quadrado.gera_quadrado("H")
        retorno = quadrado.altera_estado(quad, "F")
        assert retorno == {"estado": "?", "componentes": {}}
