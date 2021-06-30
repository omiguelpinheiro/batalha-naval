import pytest

from essencial.banco.bd_jogador import cria_tabela_jogador
from essencial.banco.bd_partida import dropa_tabela_partida
from essencial.banco.bd_quadrado import cria_quadrado_banco, cria_tabela_quadrado, dropa_tabela_quadrado
from essencial.banco.bd_jogador import dropa_tabela_jogador
from essencial.banco.conector import abre_cursor, conecta_servidor, cria_banco, usa_banco
from teste.fixture.tabuleiro_fixture import tabuleiro_fixture
from essencial import jogador


class TestaMetodosJogador:
    @pytest.fixture(scope="class", autouse=True)
    def roda_antes_dos_testes(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        dropa_tabela_partida(cursor)
        dropa_tabela_quadrado(cursor)
        dropa_tabela_jogador(cursor)
        cria_tabela_jogador(cursor)
        cria_tabela_quadrado(cursor)
        con.commit()
        jogador._jogadores = []

    def testa_registra_jogador(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = jogador.registra_jogador("a", cursor, con)
        assert retorno == 1

    def testa_falha_banco_registra_jogador(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        retorno = jogador.registra_jogador("a", cursor, con)
        assert retorno == -1

    def testa__lista_jogadores(self):
        jog = [{"nome": "a", "navios": [], "placar": 0, "id": 0, "tabuleiro": tabuleiro_fixture, "navios_disponiveis": {0: 4, 1: 3, 2: 2, 3: 1}, "maximo_pontos": 30, "id_banco": 1}]
        retorno = jogador._lista_jogadores()
        assert retorno == jog

    def testa_consulta_jogador(self):
        jog = {"nome": "a", "navios": [], "placar": 0, "id": 0, "tabuleiro": tabuleiro_fixture, "navios_disponiveis": {0: 4, 1: 3, 2: 2, 3: 1}, "maximo_pontos": 30, "id_banco": 1}
        retorno = jogador.consulta_jogador(0)
        assert retorno == jog

    def teste_falha_registra_jogador(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        jogador.registra_jogador("b", cursor, con)
        retorno = jogador.registra_jogador("c", cursor, con)
        assert retorno == 0

    def teste_posiciona_navio_falha_id_navio_fora_range(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        retorno = jogador.posiciona_navio(5, "A-5", "H", 0, cursor)
        assert retorno == 0

    def teste_posiciona_navio_falha_primeiro_quadrado_invalido(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        retorno = jogador.posiciona_navio(0, "!-5", "H", 0, cursor)
        assert retorno == -1

    def teste_posiciona_navio_falha_orientacao_invalida(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        retorno = jogador.posiciona_navio(0, "A-5", "T", 0, cursor)
        assert retorno == -2

    def teste_posiciona_navio_falha_id_jogador_invalida(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        retorno = jogador.posiciona_navio(0, "A-5", "H", 3, cursor)
        assert retorno == -3

    def teste_posiciona_navio_falha_acabou_navio_daquele_tipo(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        jogador.registra_jogador("Miguel", cursor, con)
        jogador.posiciona_navio(3, "A-8", "H", 0, cursor)
        retorno = jogador.posiciona_navio(3, "B-8", "H", 0, cursor)
        assert retorno == -4

    def teste_posiciona_navio_falha_erro_orientacao_horizontal(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        retorno = jogador.posiciona_navio(0, "B-0", "H", 0, cursor)
        assert retorno == -5

    def teste_posiciona_navio_falha_erro_orientacao_vertical(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        retorno = jogador.posiciona_navio(0, "a-8", "V", 0, cursor)
        assert retorno == -6

    def teste_posiciona_navio_sucesso_horizontal(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        retorno = jogador.posiciona_navio(0, "C-5", "H", 0, cursor)
        assert retorno == 1

    def teste_posiciona_navio_sucesso_vertical(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        retorno = jogador.posiciona_navio(0, "H-2", "V", 0, cursor)
        assert retorno == 1
