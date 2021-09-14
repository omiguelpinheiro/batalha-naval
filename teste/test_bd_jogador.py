from essencial.banco.bd_quadrado import dropa_tabela_quadrado
from essencial.banco.bd_jogador import atualiza_placar_jogador, atualiza_quantidade_navios_jogador, cria_jogador_banco, cria_tabela_jogador, dropa_tabela_jogador, le_ultimo_id_jogador, retorna_jogador, retorna_jogadores
from essencial.banco.bd_partida import dropa_tabela_partida
import pytest

from essencial.banco.conector import conecta_servidor, abre_cursor, cria_banco, usa_banco

class TestaMetodosBdJogador:
    @pytest.fixture(scope="class", autouse=True)
    def roda_antes_dos_testes(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        dropa_tabela_quadrado(cursor)
        dropa_tabela_partida(cursor)
        dropa_tabela_jogador(cursor)
    
    def testa_cria_tabela_jogador_falha(self):
        con = conecta_servidor()
        cursor = None
        retorno = cria_tabela_jogador(cursor)
        assert retorno == 0
    
    def testa_cria_tabela_jogador_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = cria_tabela_jogador(cursor)
        assert retorno == 1
    
    def testa_cria_jogador_banco_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        retorno = cria_jogador_banco("a", 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, cursor)
        assert retorno == 0
    
    def testa_cria_jogador_banco_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = cria_jogador_banco("a", 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, cursor)
        con.commit()
        assert retorno == 1
    
    def testa_le_ultimo_id_jogador_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        retorno = le_ultimo_id_jogador(cursor)
        assert retorno == -1

    def testa_le_ultimo_id_jogador_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = le_ultimo_id_jogador(cursor)
        assert retorno == 1
    
    def testa_atualiza_placar_jogador_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        retorno = atualiza_placar_jogador(1, 5, cursor)
        assert retorno == 0
    
    def testa_atualiza_placar_jogador_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = atualiza_placar_jogador(1, 5, cursor)
        assert retorno == 1
    
    def testa_atualiza_quantidade_navio_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = atualiza_quantidade_navios_jogador(4, 5, 3, cursor)
        assert retorno == 0
    
    def testa_atualiza_quantidade_navio_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = atualiza_quantidade_navios_jogador(1, 3, 3, cursor)
        assert retorno == 1
    
    def testa_retorna_jogador_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = retorna_jogador(2, cursor)
        assert retorno is None
    
    def testa_retorna_jogador_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = retorna_jogador(1, cursor)
        assert isinstance(retorno, tuple)
    
    def testa_retorna_jogadores_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        retorno = retorna_jogadores(cursor)
        assert retorno == 0
    
    def testa_retorna_jogadores_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = retorna_jogadores(cursor)
        assert isinstance(retorno, list)
    
    def testa_dropa_tabela_jogador_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = dropa_tabela_jogador(cursor)
        assert retorno == 1
    
    def testa_dropa_tabela_jogador_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        usa_banco(cursor)
        retorno = dropa_tabela_jogador(cursor)
        assert retorno == 0
    