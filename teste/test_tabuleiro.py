from essencial.banco.bd_quadrado import cria_tabela_quadrado
from essencial.tabuleiro import gera_tabuleiro, gera_tabuleiro_vazio
from essencial.banco.conector import abre_cursor, conecta_servidor, usa_banco
import pytest
from essencial.banco.bd_quadrado import cria_tabela_quadrado, dropa_tabela_quadrado
from essencial.banco.bd_jogador import cria_jogador_banco, cria_tabela_jogador, dropa_tabela_jogador
from essencial.banco.bd_partida import dropa_tabela_partida
import pytest

from essencial.banco.conector import conecta_servidor, abre_cursor, cria_banco, usa_banco
from teste.fixture.tabuleiro_fixture import tabuleiro_fixture, tabuleiro_vazio


class TestaMetodosTabuleiro:
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
        cria_jogador_banco("a", 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, cursor)
        con.commit()
    
    def testa_gera_tabuleiro_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        retorno = gera_tabuleiro(5, cursor)
        assert retorno == -1

    def testa_gera_tabuleiro_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        retorno = gera_tabuleiro(1, cursor)
        assert retorno == tabuleiro_fixture
    
    def testa_gera_tabuleiro_vazio_sucesso(self):
        retorno = gera_tabuleiro_vazio()
        assert retorno == tabuleiro_vazio