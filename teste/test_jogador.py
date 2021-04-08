from teste.fixture.tabuleiro_fixture import tabuleiro_fixture
from essencial import jogador


class TestaMetodosJogador:
    def testa_registra_jogador(self):
        retorno = jogador.registra_jogador("Miguel")
        assert retorno == 1

    def testa__lista_jogadores(self):
        jog = [{"nome": "Miguel", "placar": 0, "id": 0, "tabuleiro": tabuleiro_fixture, "posicoes_navios": [], "navios": {0: 1, 1: 2, 2: 0, 3: 2}, "maximo_pontos": 17}]
        retorno = jogador._lista_jogadores()
        assert retorno == jog

    def testa_consulta_jogador(self):
        jog = {"nome": "Miguel", "placar": 0, "id": 0, "tabuleiro": tabuleiro_fixture, "posicoes_navios": [], "navios": {0: 1, 1: 2, 2: 0, 3: 2}, "maximo_pontos": 17}
        retorno = jogador.consulta_jogador(0)
        assert retorno == jog

    def teste_falha_registra_jogador(self):
        jogador.registra_jogador("Leonardo")
        retorno = jogador.registra_jogador("Marina")
        assert retorno == 0

    def teste_posiciona_navio_falha_id_navio_fora_range(self):
        retorno = jogador.posiciona_navio(5, "A-5", "H", 0)
        assert retorno == 0

    def teste_posiciona_navio_falha_primeiro_quadrado_invalido(self):
        retorno = jogador.posiciona_navio(0, "!-5", "H", 0)
        assert retorno == -1

    def teste_posiciona_navio_falha_orientacao_invalida(self):
        retorno = jogador.posiciona_navio(0, "A-5", "T", 0)
        assert retorno == -2

    def teste_posiciona_navio_falha_id_jogador_invalida(self):
        retorno = jogador.posiciona_navio(0, "A-5", "H", 3)
        assert retorno == -3

    def teste_posiciona_navio_falha_acabou_navio_daquele_tipo(self):
        jogador.registra_jogador("Miguel")
        jogador.posiciona_navio(0, "A-8", "H", 0)
        retorno = jogador.posiciona_navio(0, "B-8", "H", 0)
        assert retorno == -4

    def teste_posiciona_navio_falha_erro_orientacao_horizontal(self):
        retorno = jogador.posiciona_navio(1, "B-2", "H", 0)
        assert retorno == -5

    def teste_posiciona_navio_falha_erro_orientacao_vertical(self):
        retorno = jogador.posiciona_navio(1, "C-2", "V", 0)
        assert retorno == -6

    def teste_posiciona_navio_sucesso_horizontal(self):
        retorno = jogador.posiciona_navio(3, "C-8", "H", 0)
        assert retorno == 1

    def teste_posiciona_navio_sucesso_vertical(self):
        retorno = jogador.posiciona_navio(3, "H-2", "V", 0)
        assert retorno == 1
