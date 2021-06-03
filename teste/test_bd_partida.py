from essencial.banco.bd_quadrado import dropa_tabela_quadrado
from essencial.banco.bd_jogador import cria_jogador_banco, cria_tabela_jogador, dropa_tabela_jogador
from essencial.banco.bd_partida import atualiza_ultima_rodada, cria_partida_banco, cria_tabela_partida, dropa_tabela_partida, finaliza_partida, le_ultimo_id_partida, retorna_partidas
from essencial.jogador import registra_jogador
import pytest

from essencial.banco.conector import conecta_servidor, abre_cursor, cria_banco, usa_banco

class TestaMetodosBdJogador:
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
    
    def testa_cria_tabela_partida_falha(self):
        con = conecta_servidor()
        cursor = None
        retorno = cria_tabela_partida(cursor)
        assert retorno == 0
    
    def testa_cria_tabela_partida_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = cria_tabela_partida(cursor)
        assert retorno == 1
    
    def testa_cria_partida_banco_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        retorno = cria_partida_banco(1, 3, cursor)
        assert retorno == 0
    
    def testa_le_ultimo_id_partida_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = le_ultimo_id_partida(cursor)
        assert retorno == -1

    def testa_cria_partida_banco_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = cria_partida_banco(1, 2, cursor)
        con.commit()
        assert retorno == 1

    def testa_le_ultimo_id_partida_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = le_ultimo_id_partida(cursor)
        assert retorno == 1

    def testa_finaliza_partida_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        retorno = finaliza_partida(5, 1, cursor)
        assert retorno == 0

    def testa_finaliza_partida_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = finaliza_partida(1, 1, cursor)
        con.commit()
        assert retorno == 1
    
    def testa_atualiza_ultima_rodada_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        retorno = atualiza_ultima_rodada(1, 1, cursor)
        con.commit()
        assert retorno == 0

    def testa_atualiza_ultima_rodada_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = atualiza_ultima_rodada(1, 1, cursor)
        con.commit()
        assert retorno == 1
    
    def testa_retorna_partidas_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        retorno = retorna_partidas(cursor)
        assert retorno == 0

    def testa_retorna_partidas_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = retorna_partidas(cursor)
        assert isinstance(retorno, list)
    
    def testa_dropa_tabela_partida_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = dropa_tabela_partida(cursor)
        assert retorno == 1
    
    def testa_dropa_tabela_partida_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = dropa_tabela_partida(cursor)
        assert retorno == 0