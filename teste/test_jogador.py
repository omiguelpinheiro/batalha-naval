from teste.fixture.tabuleiro_fixture import tabuleiro_fixture

from essencial import jogador


class TestaMetodosJogador:
    def testa_registra_jogador(self):
        retorno = jogador.registra_jogador("Miguel")
        assert retorno == 1

    def testa__lista_jogadores(self):
        jog = [{"nome": "Miguel", "placar": 28, "id": 0, "tabuleiro": tabuleiro_fixture}]
        retorno = jogador._lista_jogadores()
        assert retorno == jog

    def testa_consulta_jogador(self):
        jog = {"nome": "Miguel", "placar": 28, "id": 0, "tabuleiro": tabuleiro_fixture}
        retorno = jogador.consulta_jogador(0)
        assert retorno == jog

    def teste_falha_registra_jogador(self):
        jogador.registra_jogador("Leonardo")
        retorno = jogador.registra_jogador("Marina")
        assert retorno == 0
