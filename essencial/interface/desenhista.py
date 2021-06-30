import pygame
import sys

from essencial.extra.pygame_textinput import TextInput

const_largura = None
const_altura = None

tela = None
main_clock = None
FPS = 60

fontes = {}

def inicializa_desenhista():
    global tela, main_clock
    pygame.init()
    tela = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
    main_clock = pygame.time.Clock()

    atualiza_desenhista()

def atualiza_desenhista():
    global const_largura
    global const_altura

    largura_tela, altura_tela = pygame.display.get_surface().get_size()

    const_largura = largura_tela / 1920
    const_altura = altura_tela / 1080

    main_clock.tick(FPS)
    pygame.display.update()
    

def obtem_constantes():
    global const_largura
    global const_altura
    return const_largura, const_altura

def transforma_coordenadas_tamanho(coordenadas, tamanho, pai):
    if isinstance(pai, pygame.Surface):
        pai = pai.get_rect()
    
    const_largura, const_altura = obtem_constantes()

    coordenada_x, coordenada_y = coordenadas
    tamanho_x, tamanho_y = tamanho

    tamanho_x = tamanho_x * const_largura
    tamanho_y = tamanho_y * const_altura

    if coordenada_x < 0:
        coordenada_x = pai.centerx - tamanho_x / 2
    else:
        coordenada_x = pai.x + coordenada_x * const_largura
    if coordenada_y < 0:
        coordenada_y = pai.centery - tamanho_y / 2
    else:
        coordenada_y = pai.y + coordenada_y * const_altura

    return int(coordenada_x), int(coordenada_y), int(tamanho_x), int(tamanho_y)

def desenha_retangulo(coordenadas, tamanho, cor, espessura, pai):
    coordenada_x, coordenada_y, tamanho_x, tamanho_y = transforma_coordenadas_tamanho(coordenadas, tamanho, pai)

    retangulo = pygame.Rect(coordenada_x, coordenada_y, tamanho_x, tamanho_y)
    
    return pygame.draw.rect(tela, cor, retangulo, espessura)


def desenha_imagem(caminho, coordenadas, tamanho, pai):
    coordenada_x, coordenada_y, tamanho_x, tamanho_y = transforma_coordenadas_tamanho(coordenadas, tamanho, pai)
    
    agua_de_fundo = pygame.transform.smoothscale(pygame.image.load(caminho).convert(), (tamanho_x, tamanho_y))

    return tela.blit(agua_de_fundo, (coordenada_x, coordenada_y))


def desenha_texto(texto, caminho_fonte, tamanho_fonte, coordenadas, cor, pai, background=None):
    const_x, const_y = obtem_constantes()

    if caminho_fonte in fontes and tamanho_fonte in fontes[caminho_fonte]:
        fonte = fontes[caminho_fonte][tamanho_fonte]
    else:
        fonte = pygame.font.Font(caminho_fonte, tamanho_fonte)
        fontes[caminho_fonte] = {tamanho_fonte: fonte}
    
    superficie_texto = fonte.render(texto, True, cor).convert_alpha()
    largura, altura = superficie_texto.get_size()

    coordenada_x, coordenada_y, *resto = transforma_coordenadas_tamanho(coordenadas, (largura, altura), pai)
    superficie_texto = pygame.transform.smoothscale(
        superficie_texto, (int(largura * const_x), int(altura * const_y)))

    return tela.blit(superficie_texto, (coordenada_x, coordenada_y))

def desenha_campo_texto(campo_texto, coordenadas, pai):
    const_x, const_y = obtem_constantes()
    
    largura, altura = campo_texto.update_consts(const_x, const_y)

    coordenada_x, coordenada_y, tamanho_x, tamanho_y = transforma_coordenadas_tamanho(coordenadas, (largura, altura), pai)
    return tela.blit(campo_texto.get_surface(), (coordenada_x, coordenada_y))

""""
atualiza_desenhista()

while True:
    caminho_imagem_de_fundo = "essencial/interface/posicionamento/oceangrid_final.png"
    caminho_agua = "essencial/interface/posicionamento/agua.jpg"
    caminho_flor = "essencial/interface/posicionamento/flor.jpg"
    caminho_fonte = "essencial/fonte/Blockletter.otf"

    desenha_retangulo((0, 0), (1920, 1080), (0, 0, 0), 0, tela)
    desenha_imagem(caminho_agua, (0, 0), (1920, 1080), tela)
    desenha_imagem(caminho_imagem_de_fundo, (-1, -1), (1300, 800), tela)

    retangulo_centro = desenha_retangulo((-1, -1), (500, 300), (0, 0, 0), 0, tela)
    texto_nome = desenha_texto("Texto teste aqui grande", caminho_fonte, 22, (-1, 40), (255, 255, 255), retangulo_centro)
    botao_ok = desenha_retangulo((50, 200), (150, 50), (255, 0, 0), 0, retangulo_centro)
    botao_cancelar = desenha_retangulo((250, 200), (150, 50), (255, 0, 0), 0, retangulo_centro)
    
    desenha_texto("OK", caminho_fonte, 16, (-1, -1), (255, 255, 255), botao_ok)
    desenha_texto("CANCELAR", caminho_fonte, 16, (-1, -1), (255, 255, 255), botao_cancelar)
    
    atualiza_desenhista()
    trata_eventos()
"""