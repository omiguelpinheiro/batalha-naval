from essencial.interface.desenhista import *

CINZA = (105,105,105)
BRANCO = (255,255,255)
AMARELO = (255,255,0)

msg_titulo = "A BATALHA JÁ VAI COMEÇAR!"
msg_input_j1 = "Digite o nome do Jogador 1:"

CINZA = (105,105,105)
BRANCO = (255,255,255)
AMARELO = (255,255,0)

click = False


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


caminho_atacou_agua = "essencial/imagem/quadrado_agua.png"
caminho_atacou_navio = "essencial/imagem/quadrado_destruido.png"



atualiza_desenhista()
while True:
    desenha_imagem(caminho_fundo, (0, 0), (1920, 1080), tela)
 
    desenha_texto("Jogador 1", caminho_fonte, 45, (300, 200), BRANCO, tela)
    desenha_texto("Jogador 2", caminho_fonte, 45, (1016, 200), BRANCO, tela)

    desenha_imagem(caminho_tabuleiro, (300, -1), (2*774/3, 2*774/3), tela)
    desenha_imagem(caminho_tabuleiro, (1016, -1), (2*774/3, 2*774/3), tela)

    atualiza_desenhista()
    trata_eventos()


