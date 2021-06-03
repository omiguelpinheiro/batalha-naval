from typing import Container
from mysql.connector import cursor
from mysql.connector.cursor import CursorBase
import essencial.banco.conector
import pytest

class TestaMetodosConector:
    @pytest.fixture(scope="class", autouse=True)
    def roda_antes_dos_testes(self):
        con = essencial.banco.conector.conecta_servidor()
        cursor = essencial.banco.conector.abre_cursor(con)
        essencial.banco.conector.deleta_banco(cursor)

    def testa_conecta_servidor_falha(self):
        retorno = essencial.banco.conector.conecta_servidor("host_errado")
        assert retorno == 0
    
    def testa_conecta_servidor_sucesso(self):
        retorno = essencial.banco.conector.conecta_servidor()
        assert retorno.is_connected() == True
    
    def testa_abre_cursor_falha(self):
        con = None
        retorno = essencial.banco.conector.abre_cursor(con)
        assert retorno == 0

    def testa_abre_cursor_sucesso(self):
        con = essencial.banco.conector.conecta_servidor()
        retorno = essencial.banco.conector.abre_cursor(con)
        assert isinstance(retorno, CursorBase)

    def testa_cria_banco_falha(self):
        cursor = None
        retorno = essencial.banco.conector.cria_banco(cursor)
        assert retorno == 0

    def testa_cria_banco_sucesso(self):
        con = essencial.banco.conector.conecta_servidor()
        cursor = essencial.banco.conector.abre_cursor(con)
        retorno = essencial.banco.conector.cria_banco(cursor)
        assert retorno == 1
    
    def testa_deleta_banco_sucesso(self):
        con = essencial.banco.conector.conecta_servidor()
        cursor = essencial.banco.conector.abre_cursor(con)
        retorno = essencial.banco.conector.deleta_banco(cursor)
        assert retorno == 1
    
    def testa_deleta_banco_falha(self):
        con = essencial.banco.conector.conecta_servidor()
        cursor = None
        retorno = essencial.banco.conector.deleta_banco(cursor)
        assert retorno == 0
    
    def testa_usa_banco_sucesso(self):
        con = essencial.banco.conector.conecta_servidor()
        cursor = essencial.banco.conector.abre_cursor(con)
        essencial.banco.conector.cria_banco(cursor)
        retorno = essencial.banco.conector.usa_banco(cursor)
        assert retorno == 1
    
    def testa_usa_banco_falha(self):
        con = essencial.banco.conector.conecta_servidor()
        cursor = essencial.banco.conector.abre_cursor(con)
        retorno = essencial.banco.conector.usa_banco(cursor)
        assert retorno == 1

    def testa_inicializa_banco_sucesso(self):
        con = essencial.banco.conector.conecta_servidor()
        retorno = essencial.banco.conector.inicializa_banco(con)
        assert isinstance(retorno, CursorBase)

    def testa_inicializa_banco_falha(self):
        con = None
        retorno = essencial.banco.conector.inicializa_banco(con)
        assert retorno == 0