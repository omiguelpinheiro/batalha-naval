import traceback

from essencial.banco.conector import inicializa_banco, conexao
from essencial.banco.bd_partida import dropa_tabela_partida, retorna_partidas
from essencial.banco.bd_jogador import dropa_tabela_jogador, retorna_jogadores
from essencial.banco.bd_quadrado import dropa_tabela_quadrado, retorna_quadrados
from essencial.banco.gerador_xml import gera_xml, retorna_banco_como_dicionario

from essencial.interface.inicio import tela_inicio
from essencial.interface.posicionar import tela_posiciona_navio
from essencial.interface.vitoria import tela_vitoria

mensagem_inserir_jogador_1 = "Digite o nome do jogador 1: "
mensagem_inserir_jogador_2 = "Digite o nome do jogador 2: "

mensagem_selecao_embarcacao = "Selecione a embarcação que deseja posicionar: "

mensagem_primeiro_quadrado = "Primeiro quadrado do navio ficará em: "
mensagem_exemplo_entrada = "A-8, h-2, C4 e d7 são exemplos de entradas reconhecidas."

mensagem_orientacao = "Deseja posicionar o barco na horizontal (H/h) ou na vertical (V/v)?"
mensagem_explicacao_orientacao = "O navio será posicionado para a esquerda ou para cima."

mensagem_erro_quadrado = "Último erro: quadrado inválido."
mensagem_erro_orientacao = "Último erro: orientação inválida."
mensagem_erro_barco_falta = "Último erro: todos os barcos desse tipo foram colocados."
mensagem_erro_falta_espaco_tabuleiro = "Último erro: falta espaço no tabuleiro."
mensagem_erro_sobreposicao_barcos = "Último erro: ocorreu sobreposição de barcos."

mensagem_pede_ataque = "Jogador 0 | Qual quadrante deseja atacar? (Ex. A-8, h-2, C4 e d7): "

mensagem_erro_quadrado_ja_atacado = "Último erro: esse quadrado já foi atacado."

id_jogadores = [None, None]

navios = {0: "porta_aviao", 1: "navio_tanque",
          2: "contratorpedeiro", 3: "submarino"}

cursor = inicializa_banco(conexao)
conexao.commit()

def inicia_partida():
    tela = None
    try:
        para = False
        while not para:
            retorno_tela_inicio = tela_inicio(tela)
            if not isinstance(retorno_tela_inicio, int):
                tela, vencedor = tela_posiciona_navio(retorno_tela_inicio, cursor, conexao)
            tela, para = tela_vitoria(tela, vencedor)
    except Exception as e:
        print("Não chegou no final da execução da partida", e)
        traceback.print_exc()
    finally:
        p = retorna_partidas(cursor)
        q = retorna_quadrados(cursor)
        j = retorna_jogadores(cursor)

        dados = retorna_banco_como_dicionario(p, j, q)
        gera_xml(dados)

        dropa_tabela_partida(cursor)
        dropa_tabela_quadrado(cursor)
        dropa_tabela_jogador(cursor)
