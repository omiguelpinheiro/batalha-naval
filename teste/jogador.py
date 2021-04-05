from essencial import jogador


class TestaMetodosJogador:
    def testa_registra_jogador(self):
        retorno = jogador.registra_jogador("Miguel")
        assert retorno == 1

    def testa__lista_jogadores(self):
        retorno = jogador._lista_jogadores()
        assert retorno == [{"nome": "Miguel", "placar": 28, "id": 0}]

    def testa_consulta_jogador(self):
        retorno = jogador.consulta_jogador(0)
        assert retorno == {"nome": "Miguel", "placar": 28, "id": 0}

    def teste_falha_registra_jogador(self):
        jogador.registra_jogador("Leonardo")
        retorno = jogador.registra_jogador("Marina")
        assert retorno == 0
