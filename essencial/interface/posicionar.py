import pygame
import time
import sys

from essencial.extra.pygame_textinput import TextInput
from essencial.interface.desenhista import desenha_retangulo, desenha_texto, desenha_imagem, inicializa_desenhista, atualiza_desenhista, desenha_campo_texto
from essencial import jogador
from essencial.banco.bd_partida import atualiza_ultima_rodada, finaliza_partida, cria_partida_banco, finaliza_partida, le_ultimo_id_partida
from essencial.banco.bd_quadrado import retorna_ultima_jogada

CINZA = (105,105,105)
BRANCO = (255,255,255)
AMARELO = (255,255,0)

msg_titulo = "A BATALHA JÁ VAI COMEÇAR!"
msg_input_j1 = "Jogador "
msg_input = "Por favor digite o seu nome"

nome_navio_sub = "Submarino (0)"
nome_navio_contra = "Contratorpedeiro (1)"
nome_navio_tanque = "Navio-tanque (2)"
nome_navio_porta = "Porta-aviões (3)" 

CINZA = (105,105,105)
BRANCO = (255,255,255)
AMARELO = (255,255,0)
VERMELHO = (160, 50, 0)

caminho_fundo = "essencial/imagem/navio_batalha.jpg"
caminho_tabuleiro = "essencial/imagem/tabuleiro.png"
caminho_fonte = "essencial/fonte/Blockletter.otf"

caminho_j1_contratorpedeiro = "essencial/imagem/j1_contratorpedeiro.png"
caminho_j1_naviotanque = "essencial/imagem/j1_naviotanque.png"
caminho_j1_portaavioes = "essencial/imagem/j1_portaavioes.png"
caminho_j1_submarino = "essencial/imagem/j1_submarino.png"

caminho_j2_contratorpedeiro = "essencial/imagem/j2_contratorpedeiro.png"
caminho_j2_naviotanque = "essencial/imagem/j2_naviotanque.png"
caminho_j2_portaavioes = "essencial/imagem/j2_portaavioes.png"
caminho_j2_submarino = "essencial/imagem/j2_submarino.png"

def tela_posiciona_navio(tela, cursor, conexao):
    jogador._jogadores = []
    entrada_nome = TextInput(font_family=caminho_fonte,
                              font_size=30,
                              text_color=(0, 160, 255),
                              cursor_color=BRANCO,
                              max_string_length=30,
                              initial_string="")

    entrada_input = TextInput(font_family=caminho_fonte,
                              font_size=20,
                              text_color=(0, 160, 255),
                              cursor_color=BRANCO,
                              max_string_length=26,
                              initial_string="")
    jogadores_registrados = 0
    click = False
    registrou_jogadores = False
    selecionou_embarcacao = False
    selecinou_orientacao = False
    selecionou_primeiro_quadrado = False
    navios_posicionados = False
    vencedor = False
    criou_partida = False
    jogadores = None
    id_jogadores = [None, None]
    id_partida = None
    vez_do_jogador = 0

    embarcacao = None
    orientacao = None
    primeiro_quadrado = None

    jogador_atual = None

    registra_jogador_resultado = None
    posiciona_navio_resultado = 1
    resultado_ataque = 5

    caminho_musica_partida = "essencial/som/musica_partida.ogg"
    caminho_som_confirmacao = "essencial/som/confirmacao.ogg"
    caminho_som_erro = "essencial/som/erro.ogg"
    caminho_som_atingiu_navio = "essencial/som/atingiu_navio.ogg"
    caminho_som_destruiu_navio = "essencial/som/destruiu_navio.ogg"
    caminho_som_tiro_agua = "essencial/som/tiro_agua.ogg"

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(caminho_musica_partida))
    pygame.mixer.Channel(0).set_volume(0.15)

    while True:
        eventos = pygame.event.get()

        desenha_imagem(caminho_fundo, (0, 0), (1920, 1080), tela)
        tabuleiro_rect = desenha_imagem(caminho_tabuleiro, (-1, -1), (774, 774), tela)

        if not registrou_jogadores:
            pop_up = desenha_retangulo((-1, -1), (400, 250), CINZA, 0, tela)
            desenha_retangulo((-1, -1), (400, 250), BRANCO, 1, tela)

            desenha_retangulo((-1, 160), (380, 50), (0, 128, 0), 0, pop_up)
            desenha_retangulo((-1, 160), (380, 50), BRANCO, 1, pop_up)

            desenha_texto(msg_input_j1 + str(jogadores_registrados + 1), caminho_fonte, 30, (-1, 30), BRANCO, pop_up)
            desenha_texto(msg_input, caminho_fonte, 30, (-1, 80), BRANCO, pop_up)

            resultado_atualizacao = entrada_nome.update(eventos)
            desenha_campo_texto(entrada_nome, (-1, 160), pop_up)

        if registrou_jogadores and not criou_partida:
            jogadores = jogador._lista_jogadores()

            id_jogadores[0] = jogadores[0]["id"]
            id_jogadores[1] = jogadores[1]["id"]

            cria_partida_banco(jogadores[0]["id_banco"], jogadores[1]["id_banco"], cursor)
            conexao.commit()
            id_partida = le_ultimo_id_partida(cursor)
            criou_partida = True

        if criou_partida and not navios_posicionados:
            jogador_atual = jogador.consulta_jogador(vez_do_jogador)
            tabuleiro = jogador_atual["tabuleiro"]
            for y, linha in enumerate(tabuleiro):
                for x, coluna in enumerate(linha):
                    if tabuleiro[y][x]['estado'] == "H":
                        desenha_retangulo((82 + 70 * x, 82 + 70 * y), (50, 50), (0, 128, 0), 0, tabuleiro_rect)

            display_navios = desenha_retangulo((50, 180), (500, 250), CINZA, 0, tela)
            desenha_retangulo((50, 180), (500, 250), BRANCO, 1, tela)

            desenha_texto(msg_titulo, caminho_fonte, 40, (-1, 40), BRANCO, tela)

            desenha_imagem(caminho_j1_submarino, (10, 10), (62, 31), display_navios)
            desenha_texto(f"Quantidade {jogador_atual['navios_disponiveis'][0]} - {nome_navio_sub}", caminho_fonte, 16, (230, 10), BRANCO, display_navios)

            desenha_imagem(caminho_j1_contratorpedeiro, (10, 70), (93, 31), display_navios)
            desenha_texto(f"Quantidade {jogador_atual['navios_disponiveis'][1]} - {nome_navio_contra}", caminho_fonte, 16, (230, 70), BRANCO, display_navios)

            desenha_imagem(caminho_j1_naviotanque, (10, 130), (124, 31), display_navios)
            desenha_texto(f"Quantidade {jogador_atual['navios_disponiveis'][2]} - {nome_navio_tanque}", caminho_fonte, 16, (230, 130), BRANCO, display_navios)

            desenha_imagem(caminho_j1_portaavioes, (10, 190), (155, 31), display_navios)
            desenha_texto(f"Quantidade {jogador_atual['navios_disponiveis'][3]} - {nome_navio_porta}", caminho_fonte, 16, (230, 190), BRANCO, display_navios)

            display_interacao = desenha_retangulo((50, 500), (500, 250), CINZA, 0, tela)
            desenha_retangulo((50, 500), (500, 250), BRANCO, 1, tela)

            desenha_retangulo((-1, 180), (380, 50), (0, 128, 0), 0, display_interacao)
            desenha_retangulo((-1, 180), (380, 50), BRANCO, 1, display_interacao)

            if not selecionou_embarcacao:
                a = desenha_texto("TELA DE ENTRADA", caminho_fonte, 20, (-1, 10), (50, 50, 120), display_interacao)
                desenha_texto(f"JOGADOR {vez_do_jogador + 1}", caminho_fonte, 20, (-1, 30), (128, 128, 0), a)
                desenha_texto("Selecione a embarcação que deseja posicionar", caminho_fonte, 18, (-1, 80), BRANCO, display_interacao)
                desenha_texto("Valores aceitos são 0, 1, 2, 3", caminho_fonte, 18, (-1, 100), BRANCO, display_interacao)

                resultado_atualizacao = entrada_input.update(eventos)
                desenha_campo_texto(entrada_input, (-1, 180), display_interacao)      

            if selecionou_embarcacao and not selecinou_orientacao:
                desenha_texto("TELA DE ENTRADA", caminho_fonte, 20, (-1, 10), (50, 50, 120), display_interacao)
                desenha_texto(f"JOGADOR {vez_do_jogador + 1}", caminho_fonte, 20, (-1, 30), (128, 128, 0), a)
                desenha_texto("Selecione a orientação do navio V,v,H ou h", caminho_fonte, 18, (-1, 80), BRANCO, display_interacao)
                desenha_texto("É posicionado da esquerda pra direita ou de baixo pra cima ", caminho_fonte, 18, (-1, 100), BRANCO, display_interacao)

                resultado_atualizacao = entrada_input.update(eventos)
                desenha_campo_texto(entrada_input, (-1, 180), display_interacao)

            if selecinou_orientacao and not selecionou_primeiro_quadrado:
                desenha_texto("TELA DE ENTRADA", caminho_fonte, 20, (-1, 10), (50, 50, 120), display_interacao)
                desenha_texto(f"JOGADOR {vez_do_jogador + 1}", caminho_fonte, 20, (-1, 30), (128, 128, 0), a)
                desenha_texto("Selecione o primeiro quadrado do navio", caminho_fonte, 18, (-1, 80), BRANCO, display_interacao)
                desenha_texto("Valores aceitos são do tipo a8, A8", caminho_fonte, 18, (-1, 100), BRANCO, display_interacao)

                resultado_atualizacao = entrada_input.update(eventos)

                desenha_campo_texto(entrada_input, (-1, 180), display_interacao)

        if navios_posicionados:
            desenha_imagem(caminho_fundo, (0, 0), (1920, 1080), tela)

            tabuleiro_1 = desenha_imagem(caminho_tabuleiro, (330, 150), (2/3*774, 2/3*774), tela)
            tabuleiro_2 = desenha_imagem(caminho_tabuleiro, (1046, 150), (2/3*774, 2/3*774), tela)

            desenha_texto("Jogador 1", caminho_fonte, 45, (332, 90), BRANCO, tela)
            desenha_texto("Jogador 2", caminho_fonte, 45, (1046, 90), BRANCO, tela)

            display_interacao = desenha_retangulo((-1, 800), (500, 250), CINZA, 0, tela)
            desenha_retangulo((-1, -1), (500, 250), BRANCO, 1, display_interacao)

            jogador_1 = jogador.consulta_jogador(0)
            jogador_2 = jogador.consulta_jogador(1)
            tab_1 = jogador_1["tabuleiro"]
            for y, linha in enumerate(tab_1):
                for x, coluna in enumerate(linha):
                    if tab_1[y][x]['estado_visivel'] == "W":
                        desenha_retangulo((53 + 47 * x, 52 + 47 * y), (36, 36), (135, 206, 250), 0, tabuleiro_1)
                    elif tab_1[y][x]['estado_visivel'] == "D":
                        desenha_retangulo((53 + 47 * x, 52 + 47 * y), (36, 36), VERMELHO, 0, tabuleiro_1)
            tab_2 = jogador_2["tabuleiro"]
            for y, linha in enumerate(tab_2):
                for x, coluna in enumerate(linha):
                    if tab_2[y][x]['estado_visivel'] == "W":
                        desenha_retangulo((53 + 47 * x, 52 + 47 * y), (36, 36), (135, 206, 250), 0, tabuleiro_2)
                    elif tab_2[y][x]['estado_visivel'] == "D":
                        desenha_retangulo((53 + 47 * x, 52 + 47 * y), (36, 36), VERMELHO, 0, tabuleiro_2)

            a = desenha_texto("TELA DE ENTRADA", caminho_fonte, 20, (-1, 10), (50, 50, 120), display_interacao)
            desenha_texto(f"JOGADOR {vez_do_jogador + 1} ataca", caminho_fonte, 20, (-1, 30), (128, 128, 0), a)
            desenha_texto("Valores aceitos são do tipo a8, A8", caminho_fonte, 18, (-1, 100), BRANCO, display_interacao)

            desenha_retangulo((-1, 180), (380, 50), (0, 128, 0), 0, display_interacao)
            desenha_retangulo((-1, 180), (380, 50), BRANCO, 1, display_interacao)

            resultado_atualizacao = entrada_input.update(eventos)

            desenha_campo_texto(entrada_input, (-1, 180), display_interacao)

        if registra_jogador_resultado in [-1, -2]:
            pop_up_erro = desenha_retangulo((0, 300), (400, 120), VERMELHO, 0, pop_up)
            desenha_retangulo((-1, -1), (400, 120), BRANCO, 1, pop_up_erro)
            desenha_texto("ERRO", caminho_fonte, 30, (-1, 10), BRANCO, pop_up_erro)
            desenha_texto("Problema de conxão com o banco de dados!", caminho_fonte, 22, (-1, 60), BRANCO, pop_up_erro)

        if posiciona_navio_resultado < 1:
            pop_up_erro = desenha_retangulo((-1, 300), (400, 120), VERMELHO, 0, display_interacao)
            desenha_retangulo((-1, -1), (400, 120), BRANCO, 1, pop_up_erro)
            desenha_texto("ERRO", caminho_fonte, 30, (-1, 10), BRANCO, pop_up_erro)
            if posiciona_navio_resultado == 0:
                desenha_texto("ID do navio inválida!", caminho_fonte, 22, (-1, 60), BRANCO, pop_up_erro)
            elif posiciona_navio_resultado == -1:
                desenha_texto("Coordenada inválida!", caminho_fonte, 22, (-1, 60), BRANCO, pop_up_erro)
            elif posiciona_navio_resultado == -2:
                desenha_texto("Orientação inválida!", caminho_fonte, 22, (-1, 60), BRANCO, pop_up_erro)
            elif posiciona_navio_resultado == -4:
                desenha_texto("Você não tem mais navios desse tipo!", caminho_fonte, 22, (-1, 60), BRANCO, pop_up_erro)
            elif posiciona_navio_resultado == -5:
                desenha_texto("Faltou espaço na horizontal!", caminho_fonte, 22, (-1, 60), BRANCO, pop_up_erro)
            elif posiciona_navio_resultado == -6:
                desenha_texto("Faltou espaço na vertical!", caminho_fonte, 22, (-1, 60), BRANCO, pop_up_erro)
            elif posiciona_navio_resultado == -7:
                desenha_texto("Houve sobreposição de navios!", caminho_fonte, 22, (-1, 60), BRANCO, pop_up_erro)
            elif posiciona_navio_resultado in [-8, -9]:
                desenha_texto("Problema de conexão com o banco de dados!", caminho_fonte, 22, (-1, 60), BRANCO, pop_up_erro)

        if resultado_ataque <= 0:
            pop_up_erro = desenha_retangulo((600, -1), (400, 120), VERMELHO, 0, display_interacao)
            desenha_retangulo((-1, -1), (400, 120), BRANCO, 1, pop_up_erro)
            desenha_texto("ERRO", caminho_fonte, 30, (-1, 10), BRANCO, pop_up_erro)
            if resultado_ataque == 0:
                pass
            elif resultado_ataque == -1:
                desenha_texto("Coordenada inválida!", caminho_fonte, 22, (-1, 60), BRANCO, pop_up_erro)
            elif resultado_ataque == -2:
                desenha_texto("Coordenada já atacada!", caminho_fonte, 22, (-1, 60), BRANCO, pop_up_erro)
            elif resultado_ataque == -3 or posiciona_navio_resultado == -4:
                desenha_texto("Problema de conexão com o banco de dados!", caminho_fonte, 22, (-1, 60), BRANCO, pop_up_erro)

        for evento in eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONUP:
                click = True

        if resultado_atualizacao:
            if not registrou_jogadores:
                registra_jogador_resultado = jogador.registra_jogador(entrada_nome.get_text(), cursor, conexao)
                entrada_nome.clear_text()
                if registra_jogador_resultado == 1:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(caminho_som_confirmacao))
                    jogadores_registrados += 1
                    if jogadores_registrados == 2:
                        registrou_jogadores = True
                else:
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound(caminho_som_erro))
            if criou_partida and not selecionou_embarcacao and not navios_posicionados:
                embarcacao = entrada_input.get_text()
                entrada_input.clear_text()
                selecionou_embarcacao = True
            elif selecionou_embarcacao and not selecinou_orientacao and not navios_posicionados:
                orientacao = entrada_input.get_text()
                entrada_input.clear_text()
                selecinou_orientacao = True
            elif selecinou_orientacao and not selecionou_primeiro_quadrado and not navios_posicionados:
                primeiro_quadrado = entrada_input.get_text()
                entrada_input.clear_text()

                selecionou_embarcacao = False
                selecinou_orientacao = False
                selecionou_primeiro_quadrado = False

                posiciona_navio_resultado = jogador.posiciona_navio(embarcacao, primeiro_quadrado, orientacao, vez_do_jogador, cursor)
                if posiciona_navio_resultado == 1:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(caminho_som_confirmacao))
                else:
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound(caminho_som_erro))

                conjunto_navios = set(jogador_atual["navios_disponiveis"].values())
                if len(conjunto_navios) == 1 and 0 in conjunto_navios:
                    if vez_do_jogador == 0:
                        vez_do_jogador = 1
                    else:
                        navios_posicionados = True
                        vez_do_jogador = 0
            elif navios_posicionados and not vencedor:
                quadrado_ataque = entrada_input.get_text()
                entrada_input.clear_text()
                if vez_do_jogador == 0:
                    resultado_ataque = jogador.ataca_jogador(0, 1, quadrado_ataque, cursor)
                    if resultado_ataque == 1:
                        pygame.mixer.Channel(3).play(pygame.mixer.Sound(caminho_som_atingiu_navio))
                        pygame.mixer.Channel(4).play(pygame.mixer.Sound(caminho_som_destruiu_navio))
                        pygame.mixer.Channel(4).set_volume(0.3)
                        pygame.mixer.Channel(0).stop()
                        finaliza_partida(id_partida, jogador.consulta_jogador(vez_do_jogador)["id_banco"], cursor)
                        time.sleep(1)
                        return tela, jogador.consulta_jogador(vez_do_jogador)["nome"]
                    elif resultado_ataque == 2:
                        pygame.mixer.Channel(3).play(pygame.mixer.Sound(caminho_som_atingiu_navio))
                        pygame.mixer.Channel(3).set_volume(0.3)
                    elif resultado_ataque == 3:
                        pygame.mixer.Channel(4).play(pygame.mixer.Sound(caminho_som_destruiu_navio))
                        pygame.mixer.Channel(4).set_volume(0.3)
                    elif resultado_ataque == 4:
                        pygame.mixer.Channel(5).play(pygame.mixer.Sound(caminho_som_tiro_agua))
                    if resultado_ataque > 0:
                        vez_do_jogador = 1
                    if resultado_ataque <= 0:
                        pygame.mixer.Channel(2).play(pygame.mixer.Sound(caminho_som_erro))
                    atualiza_ultima_rodada(id_partida, retorna_ultima_jogada(jogador.consulta_jogador(0)["id_banco"], jogador.consulta_jogador(1)["id_banco"], cursor), cursor)
                else:
                    resultado_ataque = jogador.ataca_jogador(1, 0, quadrado_ataque, cursor)
                    if resultado_ataque == 1:
                        pygame.mixer.Channel(3).play(pygame.mixer.Sound(caminho_som_atingiu_navio))
                        pygame.mixer.Channel(4).play(pygame.mixer.Sound(caminho_som_destruiu_navio))
                        pygame.mixer.Channel(4).set_volume(0.3)
                        pygame.mixer.Channel(0).stop()
                        atualiza_ultima_rodada(id_partida, retorna_ultima_jogada(jogador.consulta_jogador(1)["id_banco"], jogador.consulta_jogador(0)["id_banco"], cursor), cursor)
                        finaliza_partida(id_partida, jogador.consulta_jogador(vez_do_jogador)["id_banco"], cursor)
                        time.sleep(1)
                        return tela, jogador.consulta_jogador(vez_do_jogador)["nome"]
                    elif resultado_ataque == 2:
                        pygame.mixer.Channel(3).play(pygame.mixer.Sound(caminho_som_atingiu_navio))
                        pygame.mixer.Channel(3).set_volume(0.3)
                    elif resultado_ataque == 3:
                        pygame.mixer.Channel(4).play(pygame.mixer.Sound(caminho_som_destruiu_navio))
                        pygame.mixer.Channel(4).set_volume(0.3)
                    elif resultado_ataque == 4:
                        pygame.mixer.Channel(5).play(pygame.mixer.Sound(caminho_som_tiro_agua))
                    if resultado_ataque > 0:
                        vez_do_jogador = 0
                    atualiza_ultima_rodada(id_partida, retorna_ultima_jogada(jogador.consulta_jogador(1)["id_banco"], jogador.consulta_jogador(0)["id_banco"], cursor), cursor)
        atualiza_desenhista()
