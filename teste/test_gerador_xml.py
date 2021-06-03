import pytest
import xml.etree.cElementTree as ET

from essencial.banco.gerador_xml import cria_xml_tabuleiro, cria_xml_jogador, cria_xml_partida, gera_xml, retorna_banco_como_dicionario
from essencial import jogador
from essencial.banco.conector import conecta_servidor, abre_cursor, cria_banco, usa_banco
from essencial.banco.bd_jogador import dropa_tabela_jogador, cria_tabela_jogador, cria_jogador_banco, retorna_jogadores
from essencial.banco.bd_quadrado import dropa_tabela_quadrado, cria_tabela_quadrado, cria_quadrado_banco, retorna_quadrados
from essencial.banco.bd_partida import cria_partida_banco, dropa_tabela_partida, cria_tabela_partida, retorna_partidas

class TestaMetodosGeradorXml:
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
        cria_tabela_partida(cursor)
        cria_tabela_quadrado(cursor)
        jogador.registra_jogador("a", cursor, con)
        jogador.registra_jogador("b", cursor, con)
        con.commit()
        cria_partida_banco(1, 2, cursor)
        con.commit()
        jogador.ataca_jogador(0, 1, "a8", cursor)
        jogador.ataca_jogador(0, 1, "a8", cursor)
        jogador.ataca_jogador(0, 1, "a8", cursor)
        con.commit()
        
    def testa_cria_xml_tabuleiro_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        partidas = retorna_partidas(cursor)
        quadrados = retorna_quadrados(cursor)
        jogadores = retorna_jogadores(cursor)
        data = retorna_banco_como_dicionario(partidas, jogadores, quadrados)
        retorno = cria_xml_tabuleiro(data[0]["jogador_1"])
        assert retorno == 0

    def testa_cria_xml_tabuleiro_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        partidas = retorna_partidas(cursor)
        quadrados = retorna_quadrados(cursor)
        jogadores = retorna_jogadores(cursor)
        data = retorna_banco_como_dicionario(partidas, jogadores, quadrados)
        retorno = cria_xml_tabuleiro(data[0]["jogador_1"]["tabuleiro"])
        assert isinstance(retorno, ET.Element)
    
    def testa_cria_xml_jogador_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        partidas = retorna_partidas(cursor)
        quadrados = retorna_quadrados(cursor)
        jogadores = retorna_jogadores(cursor)
        data = retorna_banco_como_dicionario(partidas, jogadores, quadrados)
        retorno = cria_xml_jogador(data[0])
        assert retorno == 0
    
    def testa_cria_xml_jogador_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        partidas = retorna_partidas(cursor)
        quadrados = retorna_quadrados(cursor)
        jogadores = retorna_jogadores(cursor)
        data = retorna_banco_como_dicionario(partidas, jogadores, quadrados)
        retorno = cria_xml_jogador(data[0]["jogador_1"])
        assert isinstance(retorno, ET.Element)
    
    def testa_cria_xml_partida_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        partidas = retorna_partidas(cursor)
        quadrados = retorna_quadrados(cursor)
        jogadores = retorna_jogadores(cursor)
        data = retorna_banco_como_dicionario(partidas, jogadores, quadrados)
        retorno = cria_xml_partida(data)
        assert retorno == 0
    
    def testa_cria_xml_partida_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        partidas = retorna_partidas(cursor)
        quadrados = retorna_quadrados(cursor)
        jogadores = retorna_jogadores(cursor)
        data = retorna_banco_como_dicionario(partidas, jogadores, quadrados)
        retorno = cria_xml_partida(data[0])
        assert isinstance(retorno, ET.Element)
    
    def testa_gera_xml_falha(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        partidas = retorna_partidas(cursor)
        quadrados = retorna_quadrados(cursor)
        jogadores = retorna_jogadores(cursor)
        data = retorna_banco_como_dicionario(partidas, jogadores, quadrados)
        retorno = gera_xml(partidas)
        assert retorno == 0
    
    def testa_gera_xml_sucesso(self):
        con = conecta_servidor()
        cursor = abre_cursor(con)
        cria_banco(cursor)
        usa_banco(cursor)
        partidas = retorna_partidas(cursor)
        quadrados = retorna_quadrados(cursor)
        jogadores = retorna_jogadores(cursor)
        data = retorna_banco_como_dicionario(partidas, jogadores, quadrados)
        retorno = gera_xml(data)
        assert retorno == 1
    
