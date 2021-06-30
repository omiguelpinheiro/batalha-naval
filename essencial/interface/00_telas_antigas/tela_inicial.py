import pygame, sys
import essencial.interface.tela_continuar_jogo as tela_continuar

from pygame.locals import *

# Iniciando o pygame
pygame.init()
pygame.mixer.init()

# Utilizando a funcionalidade time do pygame para atualizar os frames da tela
mainClock = pygame.time.Clock()
FPS = 120

# Configurando a fonte
font_title = pygame.font.SysFont(None,130)
font_common = pygame.font.SysFont(None,50)

# Definindo as mensagens
msg_title = 'Batalha Naval'
msg_new_game = 'Novo jogo'
msg_continue = 'Continuar'
msg_exit = 'Sair'

# Configurando a tela
window_width = 800
window_height = 800
center_x = window_width/2
center_y = window_height/2

pygame.display.set_caption(msg_title)
screen = pygame.display.set_mode([window_width,window_height], 0, 32)

background_1 = pygame.image.load("essencial/interface/background_batalha_naval_tela_inicial.png")
icon_img = pygame.image.load("essencial/interface/background_batalha_naval_tela_inicial.png")
icon = pygame.display.set_icon(icon_img)

# Definindo as cores
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)

# Posição e dimensões de cada botão
    # Menu principal
        # Posição
sqrt_pos_x_menu = center_x/2+100

sqrt_pos_y_new_game = center_y
sqrt_pos_y_continue = center_y+100
sqrt_pos_y_exit = center_y+200

        # Dimensões
button_width = 200
button_height = 50

# Posição de cada mensagem
    # Título
msg_pos_x_title_black = center_x/2 - 90
msg_pos_x_title_white = center_x/2 - 100
msg_pos_y_title = center_y/2

    # Menu principal
msg_pos_x_menu_black = center_x/2+115
msg_pos_x_menu_white = center_x/2+110

msg_pos_y_new_game = center_y+10
msg_pos_y_continue = center_y+110
msg_pos_y_exit = center_y+210


# Função da música de fundo
def sound_on():
    # soundtrack = pygame.mixer.Sound('essencial/som/bensound-instinct_japan.mp3')
    # soundtrack.play()
    pass

# Função de exibir o texto na tela  
def draw_text(text,font,colour,surface,x,y):

    textobj = font.render(text,1,colour)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj,textrect)


# Função da tela de início
def main_menu():

    sound_on()

    click = False

    while True:

        # Customizando a tela
        screen.blit(background_1,(0,0))
        draw_text(msg_title,font_title, BLACK, screen, msg_pos_x_title_black, msg_pos_y_title)
        draw_text(msg_title,font_title, WHITE, screen,msg_pos_x_title_white, msg_pos_y_title)

        # Pegando a posição do mouse
        mx,my = pygame.mouse.get_pos()

        # Criando os botões de 'Novo jogo', 'Continuar' e 'Sair'
        button_new_game = pygame.Rect(sqrt_pos_x_menu,sqrt_pos_y_new_game,button_width,button_height) # Botão de 'Novo jogo'
        button_continue = pygame.Rect(sqrt_pos_x_menu,sqrt_pos_y_continue,button_width,button_height) # Botão de 'Continuar'
        button_exit = pygame.Rect(sqrt_pos_x_menu,sqrt_pos_y_exit,button_width,button_height) # Botão de 'Sair'

        # Desenhando os quadrados
        pygame.draw.rect(screen,WHITE,button_new_game,1) # O último parâmetro, 1, mostra que o retângulo não será preenchido
        pygame.draw.rect(screen,WHITE,button_continue,1)
        pygame.draw.rect(screen,WHITE,button_exit,1)

        # Escrevendo nos quadrados
        draw_text(msg_new_game,font_common, BLACK, screen, msg_pos_x_menu_black, msg_pos_y_new_game)
        draw_text(msg_new_game,font_common, WHITE, screen, msg_pos_x_menu_white, msg_pos_y_new_game)

        draw_text(msg_continue,font_common, BLACK, screen, msg_pos_x_menu_black, msg_pos_y_continue)
        draw_text(msg_continue,font_common, WHITE, screen, msg_pos_x_menu_white, msg_pos_y_continue)

        draw_text(msg_exit,font_common, BLACK, screen, msg_pos_x_menu_black, msg_pos_y_exit)
        draw_text(msg_exit,font_common, WHITE, screen, msg_pos_x_menu_white, msg_pos_y_exit)

        # Fazendo as colisões dos botões
        if button_new_game.collidepoint((mx,my)):
            draw_text(msg_new_game,font_common, YELLOW, screen, msg_pos_x_menu_white, msg_pos_y_new_game)
            if click:
                pass

        if button_continue.collidepoint((mx,my)):
            draw_text(msg_continue,font_common, YELLOW, screen, msg_pos_x_menu_white, msg_pos_y_continue)
            if click:
                tela_continuar.continuar_jogo() # Conectar com a tela de carregamento
        
        if button_exit.collidepoint((mx,my)):
            draw_text(msg_exit,font_common, YELLOW, screen, msg_pos_x_menu_white, msg_pos_y_exit)
            if click:
                quit() # Sair

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(FPS)


while True:
    main_menu()
    pygame.display.flip()


