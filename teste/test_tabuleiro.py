from essencial import jogador
from teste.fixture.tabuleiro_fixture import tabuleiro_fixture


class TestaMetodosTabuleiro:
    # Esse teste por algum motivo esta tendo
    # um overlap com o do modulo jogador
    def testa_registra_tabuleiro(self):
        jog = jogador.consulta_jogador(1)
        assert jog["tabuleiro"] == tabuleiro_fixture
