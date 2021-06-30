import pygame
import time
import sys

from essencial.interface.desenhista import desenha_retangulo, desenha_texto, desenha_imagem, atualiza_desenhista

encerrada = True 

msg_novo = "Novo Jogo"
msg_sair = "Sair"

CINZA = (105,105,105)
BRANCO = (255,255,255)
AMARELO = (255,255,0)

caminho_fundo = "essencial/imagem/navio_fundo.jpg"
caminho_fonte = "essencial/fonte/Blockletter.otf"

def tela_vitoria(tela, vencedor):
    click = False
    caminho_som_vitoria = "essencial/som/som_vitoria.ogg"
    caminho_som_clique = "essencial/som/click_som.ogg"

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(caminho_som_vitoria))
    while True:
        msg_vitoria = f"Parabéns, {vencedor}! Você venceu."
        
        mouse_x, mouse_y = pygame.mouse.get_pos()

        desenha_imagem(caminho_fundo, (0, 0), (1920, 1080), tela)
        desenha_texto(msg_vitoria, caminho_fonte, 60, (-1, 240), BRANCO, tela)
        
        botao_novo = desenha_retangulo((-1, 500), (200, 50), CINZA, 0, tela)
        texto_novo = desenha_texto(msg_novo, caminho_fonte, 30, (-1, -1), BRANCO, botao_novo)
        
        botao_sair = desenha_retangulo((-1, 600), (200, 50), CINZA, 0, tela)
        texto_sair = desenha_texto(msg_sair, caminho_fonte, 30, (-1, -1), BRANCO, botao_sair)
        
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
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
                pygame.mixer.Channel(0).play(pygame.mixer.Sound(caminho_som_clique))
                time.sleep(0.3)
                return tela, False

        if botao_sair.collidepoint(mouse_x, mouse_y):
            texto_sair = desenha_texto(msg_sair, caminho_fonte, 30, (-1, -1), AMARELO, botao_sair)
            if click:
                pygame.quit()
                sys.exit()

        atualiza_desenhista()
