import pygame
import sys

from pygame.locals import *

# importar do programa principal:
# estado da partida pra saber se a tela deve ser exibida
# nome do jogador correspondende ao id do vencedor (pra exibir na tela)

estado = "encerrada"
nome_vencedor = "Leonardo"

# mensagens e botões:
msg_vitoria = f"Parabéns, {nome_vencedor}! Você venceu."
msg_novo_jogo = "Novo Jogo"
msg_sair = "Sair"

# inicio:
pygame.init()

# utilizando a funcionalidade time do pygame para atualizar os frames da tela
mainClock = pygame.time.Clock()
FPS = 60

# configurando a tela
largura = 800
alura = 600
centro_x = largura / 2
centro_y = alura / 2

largura_botao = 200
altura_botao = 50

pygame.display.set_caption("Batalha Naval")
screen = pygame.display.set_mode([largura, alura])

imagem_de_fundo = pygame.image.load("water.png").convert()

# posições dos elementos na tela

# texto
x_msg_vitoria = centro_x - 270
y_msg_vitoria = centro_y - 50

x_msg_novo_jogo = centro_x / 2 + 100
y_msg_novo_jogo = centro_y

x_msg_sair = centro_x / 2 + 100
y_msg_sair = centro_y + 100

# botoes
x_botao_novo_jogo = centro_x / 2 + 100
y_botao_novo_jogo = centro_y

x_botao_sair = centro_x / 2 + 100
y_botao_sair = centro_y


# configurando a fonte
font_title = pygame.font.SysFont(None, 50)
font_common = pygame.font.SysFont(None, 50)
fonte_militar = pygame.font.Font("fonte_militar.ttf", 16)

# Definindo as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AMARELO = (255, 255, 0)

# Configurações de interação:
click = False

# Função de exibir o texto na tela


def escreve_na_tela(text, font, colour, surface, x, y):

    textobj = font.render(text, 1, colour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Função da tela de início
def tela_de_vitoria():

    while True:
        pygame.event.get()

        screen.fill(PRETO)

        screen.blit(imagem_de_fundo, [0, 0])

        escreve_na_tela(msg_vitoria, font_title, BRANCO,
                        screen, x_msg_vitoria, y_msg_vitoria)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Criando os botões de 'Novo jogo' e 'Sair'
        # Texto
        botao_novo_jogo = pygame.Rect(
            x_msg_novo_jogo, y_msg_novo_jogo, largura_botao, altura_botao
        )
        botao_sair = pygame.Rect(
            x_msg_sair, y_msg_sair, largura_botao, altura_botao)

        # Retangulos:
        pygame.draw.rect(screen, BRANCO, botao_novo_jogo, 1)
        pygame.draw.rect(screen, BRANCO, botao_sair, 1)

        escreve_na_tela(msg_novo_jogo, font_common, BRANCO,
                        screen, x_msg_novo_jogo, y_msg_novo_jogo)
        escreve_na_tela(msg_sair, font_common, BRANCO,
                        screen, x_msg_sair, y_msg_sair)

        if botao_novo_jogo.collidepoint(mouse_x, mouse_y):
            escreve_na_tela(msg_novo_jogo, font_common, AMARELO,
                            screen, x_msg_novo_jogo, y_msg_novo_jogo)
            if click:
                pass
        if botao_sair.collidepoint(mouse_x, mouse_y):
            escreve_na_tela(msg_sair, font_common, AMARELO,
                            screen, x_msg_sair, y_msg_sair)
            if click:
                pygame.quit()
                sys.exit()

        # Atualizações
        mainClock.tick(FPS)
        pygame.display.update()

        # Sair do jogo quando clicar no X
        click = False
        for evento in pygame.event.get():
            if evento.type == MOUSEBUTTONDOWN:
                if evento.button == 1:
                    click = True

            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


# Execution
while True:
    if estado == "encerrada":
        tela_de_vitoria()
        pygame.display.flip()
