import time

from essencial import cli, jogador
from essencial.banco.conector import con
from essencial.banco.bd_partida import drop_tabela_partida, cria_partida_banco
from essencial.banco.bd_jogador import drop_tabela_jogador
from essencial.banco.bd_quadrado import drop_tabela_quadrado
from essencial.jogador import _lista_jogadores

from xml.dom import minidom

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
          
def inicia_partida():
    try:
        console = cli.inicia_cli()

        cli.escreve_na_tela(0, 0, mensagem_inserir_jogador_1, console)
        nome_jogador_1 = cli.pede_dado(
            0, len(mensagem_inserir_jogador_1), 25, console).decode()
        cli.escreve_na_tela(0, len(mensagem_inserir_jogador_1) +
                            len(nome_jogador_1), " -> Inserido", console)
        cli.escreve_na_tela(1, 0, mensagem_inserir_jogador_2, console)
        nome_jogador_2 = cli.pede_dado(
            1, len(mensagem_inserir_jogador_2), 25, console).decode()
        cli.escreve_na_tela(1, len(mensagem_inserir_jogador_2) +
                            len(nome_jogador_2), " -> Inserido", console)

        cli.limpa_cli(console)

        jogador.registra_jogador(nome_jogador_1)
        jogador.registra_jogador(nome_jogador_2)

        jogadores = jogador._lista_jogadores()

        id_jogadores[0] = jogadores[0]["id"]
        id_jogadores[1] = jogadores[1]["id"]

        cria_partida_banco(jogadores[0]["id_banco"], jogadores[1]["id_banco"], con)

        for id_jogador in id_jogadores:
            while True:
                jog = jogador.consulta_jogador(id_jogador)
                # Desenha tabuleiro
                cli.desenha_tabuleiro(jog, 0, 0, console)
                cli.escreve_na_tela(10, 28, str(id_jogador), console)

                # Desenha mural de embarcações
                cli.escreve_na_tela(
                    0, 28, f"Num      Embarcações            Ocupa     Qtd", console)
                cli.escreve_na_tela(
                    1, 28, f" 0       Porta-aviões       5 Quadrados    {jog['navios_disponiveis'][0]}", console)
                cli.escreve_na_tela(
                    2, 28, f" 1       Navio-tanque       4 Quadrados    {jog['navios_disponiveis'][1]}", console)
                cli.escreve_na_tela(
                    3, 28, f" 2     Contratorpedeiro     3 Quadrados    {jog['navios_disponiveis'][2]}", console)
                cli.escreve_na_tela(
                    4, 28, f" 3        Submarino         2 Quadrados    {jog['navios_disponiveis'][3]}", console)

                # Desenha mensagem para selecionar embarcação mais prompt de input
                cli.escreve_na_tela(6, 28, mensagem_selecao_embarcacao, console)
                navio = cli.pede_dado(
                    6, 28 + len(mensagem_selecao_embarcacao), 1, console).decode()
                # Apaga mensagem e prompt acima
                cli.escreve_na_tela(
                    6, 28, " " * (len(mensagem_selecao_embarcacao) + 3), console)

                # Desenha mensagem pedindo a orientação e como funciona o posicionamento do navio e o prompt de input
                cli.escreve_na_tela(6, 28, mensagem_orientacao, console)
                cli.escreve_na_tela(7, 28, mensagem_explicacao_orientacao, console)
                orientacao = cli.pede_dado(
                    6, 28 + len(mensagem_orientacao), 1, console).decode().upper()
                # Apaga mensagem e prompt acima
                cli.escreve_na_tela(
                    6, 28, " " * (len(mensagem_orientacao) + 3), console)
                cli.escreve_na_tela(
                    7, 28, " " * (len(mensagem_explicacao_orientacao) + 3), console)

                # Desenha mensagem pedindo o primeiro quadrado que o navio vai ficar e o prompt de input
                cli.escreve_na_tela(6, 28, mensagem_primeiro_quadrado, console)
                cli.escreve_na_tela(7, 28, mensagem_exemplo_entrada, console)
                primeiro_quadrado = cli.pede_dado(
                    6, 28 + len(mensagem_primeiro_quadrado), 3, console).decode().upper()
                # Apaga mensagem e prompt cima
                cli.escreve_na_tela(
                    6, 28, " " * (len(mensagem_primeiro_quadrado) + 3), console)
                cli.escreve_na_tela(
                    7, 28, " " * (len(mensagem_exemplo_entrada) + 3), console)

                retorno = jogador.posiciona_navio(
                    int(navio), primeiro_quadrado, orientacao, id_jogador)
                if retorno == -1:
                    cli.escreve_na_tela(8, 28, mensagem_erro_quadrado, console)
                elif retorno == -2:
                    cli.escreve_na_tela(8, 28, mensagem_erro_orientacao, console)
                elif retorno == -4:
                    cli.escreve_na_tela(8, 28, mensagem_erro_barco_falta, console)
                elif retorno in [-5, -6]:
                    cli.escreve_na_tela(
                        8, 28, mensagem_erro_falta_espaco_tabuleiro, console)
                elif retorno == -7:
                    cli.escreve_na_tela(
                        8, 28, mensagem_erro_sobreposicao_barcos, console)
                else:
                    cli.escreve_na_tela(
                        8, 28, " " * (len(mensagem_erro_barco_falta) + 3), console)
                conjunto_navios = set(jog["navios_disponiveis"].values())
                if len(conjunto_navios) == 1 and 0 in conjunto_navios:
                    break

        jogador.registra_jogador("Miguel")
        jogador.registra_jogador("Leonardo")

        jogador.posiciona_navio(0, "a8", "H", 0)

        jogador.posiciona_navio(0, "a8", "H", 1)

        while True:
            atacante = jogador.consulta_jogador(id_jogadores[0])
            atacado = jogador.consulta_jogador(id_jogadores[1])

            cli.desenha_mapa(jogador.consulta_jogador(0),
                            jogador.consulta_jogador(1))
            cli.escreve_na_tela(
                13, 0, f"Jogador {id_jogadores[0]} | Qual quadrante deseja atacar? (Ex. A-8, h-2, C4 e d7): ", console)
            coordenada = cli.pede_dado(
                13, len(mensagem_pede_ataque), 3, console).decode()
            retorno = jogador.ataca_jogador(
                id_jogadores[0], id_jogadores[1], coordenada)
            cli.escreve_na_tela(17, 0, mensagem_erro_quadrado, console)
            if retorno == -1:
                cli.escreve_na_tela(14, 0, mensagem_erro_quadrado, console)
            if retorno == -2:
                cli.escreve_na_tela(
                    14, 0, mensagem_erro_quadrado_ja_atacado, console)
            if retorno == 1:
                cli.desenha_mapa(jogador.consulta_jogador(0),
                                jogador.consulta_jogador(1))
                cli.escreve_na_tela(
                    13, 0, f"{atacante['nome']} venceu o jogo! Parabéns!", console)
                cli.pede_dado(14, 0, 0, console).decode()
                break
            if retorno == 3:
                raise Exception("VOCE DESTRUIU UM NAVIO")
            indice_0 = id_jogadores.pop(0)
            id_jogadores.append(indice_0)
        cli.encerra_cli()
    except Exception as e:
        print("Não chegou no final da execução da partida", e)
    finally:
        drop_tabela_partida(con)
        drop_tabela_quadrado(con)
        drop_tabela_jogador(con)
