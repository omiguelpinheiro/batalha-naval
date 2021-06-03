from essencial.banco.bd_quadrado import atualiza_quadrado, cria_quadrado_banco, cria_tabela_quadrado, dropa_tabela_quadrado, retorna_quadrados, retorna_ultima_jogada
from essencial.banco.bd_jogador import cria_jogador_banco, cria_tabela_jogador, dropa_tabela_jogador
from essencial.banco.bd_partida import dropa_tabela_partida
from essencial.jogador import registra_jogador
import pytest

from essencial.banco.conector import conecta_servidor, abre_cursor, cria_banco, usa_banco

class TestaMetodosBdQuadrado:
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
        cria_jogador_banco("a", 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, cursor)
        cria_jogador_banco("b", 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, cursor)
        con.commit()
    
    def testa_cria_tabela_quadrado_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        retorno = cria_tabela_quadrado(cursor)
        assert retorno == 0
    
    def testa_cria_quadrado_banco_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = cria_quadrado_banco(2, 2, 2, 2, "H", 2, cursor)
        assert retorno == 0

    def testa_cria_tabela_quadrado_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = cria_tabela_quadrado(cursor)
        assert retorno == 1
    
    def testa_cria_quadrado_banco_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno_1 = cria_quadrado_banco(1, 2, 2, 2, "H", 2, cursor)
        retorno_2 = cria_quadrado_banco(2, 2, 2, 2, "H", 2, cursor)
        con.commit()
        assert retorno_1 == 1 and retorno_2 == 1
    
    def testa_atualiza_quadrado_banco_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = atualiza_quadrado(1, 2, 2, 2, "W", 1, cursor)
        con.commit()
        assert retorno == 1
    
    def testa_atualiza_quadrado_banco_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        cursor = None
        retorno = atualiza_quadrado(8, 3, 4, 2, "W", 1, cursor)
        con.commit()
        assert retorno == 0
    
    def testa_retorna_ultima_jogada_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = retorna_ultima_jogada(1, 3, cursor)
        assert retorno == -1
    
    def testa_retorna_ultima_jogada_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = retorna_ultima_jogada(1, 2, cursor)
        assert retorno == 2
    
    def testa_retorna_quadrados_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        cursor = None
        retorno = retorna_quadrados(cursor)
        con.commit()
        assert retorno == 0
    
    def testa_retorna_quadrados_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = retorna_quadrados(cursor)
        con.commit()
        assert isinstance(retorno, list)
    
    def testa_dropa_tabela_quadrado_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = dropa_tabela_quadrado(cursor)
        con.commit()
        assert retorno == 1
    
    def testa_dropa_tabela_quadrado_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = dropa_tabela_quadrado(cursor)
        con.commit()
        assert retorno == 0
