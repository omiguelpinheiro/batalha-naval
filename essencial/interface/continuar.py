from essencial.interface.desenhista import *

msg_selecione = "Selecione o jogo a ser carregado:"
msg_voltar = "Voltar"

CINZA = (105,105,105)
BRANCO = (255,255,255)
AMARELO = (255,255,0)

atualiza_desenhista()

click = False


caminho_fundo = "essencial/imagem/navio_fundo.jpg"
caminho_fonte = "essencial/fonte/Blockletter.otf"

while True:

    mouse_x, mouse_y = pygame.mouse.get_pos()

    desenha_imagem(caminho_fundo, (0, 0), (1920, 1080), tela)
    desenha_texto(msg_selecione, caminho_fonte, 45, (-1, 200), BRANCO, tela)

    botao_voltar = desenha_retangulo((250, 200), (200, 50), CINZA, 0, tela)
    texto_voltar = desenha_texto(msg_voltar, caminho_fonte, 30, (-1, -1), BRANCO, botao_voltar)

    if botao_voltar.collidepoint(mouse_x, mouse_y):
        texto_voltar = desenha_texto(msg_voltar, caminho_fonte, 30, (-1, -1), AMARELO, botao_voltar)
    atualiza_desenhista()
    trata_eventos()


