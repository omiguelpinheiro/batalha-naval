import pygame
import time
import sys
import essencial.interface.desenhista

from essencial.interface.desenhista import desenha_retangulo, desenha_texto, desenha_imagem, inicializa_desenhista, atualiza_desenhista

msg_titulo = "BATALHA NAVAL"
msg_novo = "Novo Jogo"
msg_cont = "Carregar" 
msg_sair = "Sair"

CINZA = (105,105,105)
BRANCO = (255,255,255)
AMARELO = (255,255,0)

caminho_fundo = "essencial/imagem/navio_fundo.jpg"
caminho_fonte = "essencial/fonte/Blockletter.otf"

def tela_inicio(tela):
    if tela is None:
        inicializa_desenhista()
    click = False
    caminho_musica_inicio = "essencial/som/musica_inicio.ogg"
    caminho_som_click = "essencial/som/click_som.ogg"
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(caminho_musica_inicio))
    pygame.mixer.Channel(0).set_volume(0.5)
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        desenha_imagem(caminho_fundo, (0, 0), (1920, 1080), essencial.interface.desenhista.tela)
        desenha_texto(msg_titulo, caminho_fonte, 80, (-1, 200), BRANCO, essencial.interface.desenhista.tela)

        botao_novo = desenha_retangulo((-1, 500), (200, 50), CINZA, 0, essencial.interface.desenhista.tela)
        texto_novo = desenha_texto(msg_novo, caminho_fonte, 30, (-1, -1), BRANCO, botao_novo)

        botao_carregar = desenha_retangulo((-1, 600), (200, 50), CINZA, 0, essencial.interface.desenhista.tela)
        texto_carregar = desenha_texto(msg_cont, caminho_fonte, 30, (-1, -1), BRANCO, botao_carregar)

        botao_sair = desenha_retangulo((-1, 700), (200, 50), CINZA, 0, essencial.interface.desenhista.tela)
        texto_sair = desenha_texto(msg_sair, caminho_fonte, 30, (-1, -1), BRANCO, botao_sair)

        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONUP:
                click = True

        if botao_novo.collidepoint(mouse_x, mouse_y):
            texto_novo = desenha_texto(msg_novo, caminho_fonte, 30, (-1, -1), AMARELO, botao_novo)
            if click:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound(caminho_som_click))
                time.sleep(0.2)
                pygame.mixer.Channel(0).stop()
                pygame.mixer.Channel(1).stop()
                return essencial.interface.desenhista.tela

        if botao_carregar.collidepoint(mouse_x, mouse_y):       
            botao_carregar = desenha_texto(msg_cont, caminho_fonte, 30, (-1, -1), AMARELO, botao_carregar)
            if click:
                return 2

        if botao_sair.collidepoint(mouse_x, mouse_y):
            texto_sair = desenha_texto(msg_sair, caminho_fonte, 30, (-1, -1), AMARELO, botao_sair)
            if click:
                pygame.quit()
                sys.exit()

        atualiza_desenhista()