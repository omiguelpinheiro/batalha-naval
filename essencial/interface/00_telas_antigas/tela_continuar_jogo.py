import pygame, sys
import essencial.interface.tela_inicial as tela_init

from pygame.locals import *

# Iniciando o pygame
pygame.init()

# Utilizando a funcionalidade time do pygame para atualizar os frames da tela
mainClock = pygame.time.Clock()
FPS = 60

# Configurando a fonte
font_common = pygame.font.SysFont(None,50)
font_back = pygame.font.SysFont(None,30)

# Definindo as mensagens
msg_title = 'Batalha Naval'
msg_back = 'Voltar'

# Definindo as cores em RGB
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)

# Configurando a tela
window_width = 800
window_height = 800
center_x = window_width/2
center_y = window_height/2

pygame.display.set_caption(msg_title)
screen = pygame.display.set_mode([window_width,window_height], 0, 32)

background_2 = pygame.image.load("essencial/interface/background_batalha_naval_tela_continuarJogo.png")
icon_img = pygame.image.load("essencial/interface/background_batalha_naval_tela_inicial.png")
icon = pygame.display.set_icon(icon_img)

# Posição de cada mensagem
msg_pos_x_back_black = 17.7
msg_pos_x_back_white = 15

msg_pos_y_back = 15




# Função da tela de carregar jogo
def continuar_jogo():

    click = False

    while True:

        # Customizando a tela
        screen.blit(background_2,(0,0))

        # Pegando a posição do mouse
        mx,my = pygame.mouse.get_pos()

        # Criando o botão de 'Voltar'
        button_1 = pygame.Rect(5,5,90,40) # Botão de 'Voltar'

        # Desenhando os quadrados
        pygame.draw.rect(screen,WHITE,button_1,1)

        tela_init.draw_text(msg_back,font_back, BLACK, screen, msg_pos_x_back_black, msg_pos_y_back)
        tela_init.draw_text(msg_back,font_back, WHITE, screen, msg_pos_x_back_white, msg_pos_y_back)

        if button_1.collidepoint((mx,my)):
            tela_init.draw_text(msg_back,font_back, YELLOW, screen, msg_pos_x_back_white, msg_pos_y_back)
            if click:
                tela_init.main_menu() # Conectar com a tela inicial

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    tela_init.main_menu() # Conectar com a tela inicial

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Desenhando o quadrado dos saves presentes no arquivo xml.
            # Terão, no máximo, 5 saves aparecendo na tela. Caso o jogador salve um novo jogo,
            # este entra na quinta posição e o save presente na posição um é preenchido pelo save da segunda posição e assim sucessivamente.

        for i in range(5):
            button_bloco11 = pygame.Rect(center_x-300,center_y-300+100*i,400,80) # Bloco da esquerda
            button_bloco12 = pygame.Rect(center_x+100,center_y-300+100*i,200,80) # Bloco da direita
            button_shadow = pygame.Rect(center_x-290,center_y-290+100*i,600,80) # Sombra da área total ocupada pelos dois blocos

            pygame.draw.rect(screen,BLACK,button_shadow)
            pygame.draw.rect(screen,WHITE,button_bloco11)
            pygame.draw.rect(screen,WHITE,button_bloco12)
            pygame.draw.rect(screen,BLACK,button_bloco11,1)
            pygame.draw.rect(screen,BLACK,button_bloco12,1)

        pygame.display.update()
        mainClock.tick(FPS)
