from essencial import jogador, tabuleiro
from teste.fixture.tabuleiro_fixture import tabuleiro_fixture, tabuleiro_print_fixture


class TestaMetodosTabuleiro:
    def testa_registra_tabuleiro(self):
        jogador.registra_jogador("Miguel")
        jog = jogador.consulta_jogador(0)
        assert jog["tabuleiro"] == tabuleiro_fixture

    def testa_mostra_tabuleiro(self, capsys):
        jog = jogador.consulta_jogador(0)
        tabuleiro.mostra_tabuleiro(jog["tabuleiro"])
        captured = capsys.readouterr()
        assert captured.out == tabuleiro_print_fixture
