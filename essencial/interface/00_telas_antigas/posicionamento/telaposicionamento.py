import pygame
from essencial.extra.pygame_textinput import TextInput
import sys
import os

from pygame.locals import *
# from essencial.banco.conector import inicializa_banco, conexao
from essencial.jogador import registra_jogador

#### ISSO AQUI JA DEVERIA ESTAR FEITO EM OUTROS MODULOS ####
# cursor = inicializa_banco(conexao)
# conexao.commit()
#### ISSO AQUI JA DEVERIA ESTAR FEITO EM OUTROS MODULOS ####

pygame.init()

fonte = pygame.font.Font("essencial/fonte/fonte_militar.ttf", 28)

# force window position to be centred
os.environ["SDL_VIDEO_CENTERED"] = "1"

mainClock = pygame.time.Clock()
FPS = 60

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AMARELO = (255, 255, 0)

largura_maxima = 1920
altura_maxima = 1080

# get the current screen size
info = pygame.display.Info()
width, height = info.current_w, info.current_h
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

imagem_de_fundo = pygame.image.load("essencial/interface/posicionamento/oceangrid_final.png").convert()
imagem_de_fundo = pygame.transform.smoothscale(imagem_de_fundo, (924, 924))

agua_de_fundo = pygame.image.load("essencial/interface/posicionamento/agua.jpg")
agua_de_fundo = pygame.transform.smoothscale(agua_de_fundo, (1920, 1080))

entrada_texto = TextInput(font_family="essencial/fonte/fonte_militar.ttf", text_color=(BRANCO), font_size=24, cursor_color=BRANCO, max_string_length=30, initial_string="oiee")

tamanho_insere_jogador = fonte.size("Insira o nome do jogador 1")
fonte.render(None, True, BRANCO)

while True:
    screen.blit(agua_de_fundo, (0, 0))
    screen.blit(imagem_de_fundo, (498, 78))

    tela_inserir_jogador = pygame.Rect(760, 390, 400, 300)
    texto_inserir_jogador = fonte.render('Insira o nome do jogador 1', True, BRANCO)
 
    pygame.draw.rect(screen, PRETO, tela_inserir_jogador, 0, True)
    screen.blit(texto_inserir_jogador, ((760 + 200) - tamanho_insere_jogador[0] / 2, (390 + 30)))

    eventos = pygame.event.get()
    for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    running = False
                    pygame.display.quit()
                    # pygame.quit()
                    # sys.exit()

            if evento.type == pygame.QUIT:
                pygame.display.quit()
                # pygame.quit()
                # sys.exit()

    # Feed it with events every frame
    entrada_texto.update(eventos)
    # Blit its surface onto the screen
    screen.blit(entrada_texto.get_surface(), ((760 + 40), (390 + 90)))

    mainClock.tick(FPS)
    pygame.display.update()

    if entrada_texto.update(eventos):
        pass
        # registra_jogador(entrada_texto.get_text(), cursor, conexao)
