import curses
import time

from essencial import util


def inicia_cli():
    console = curses.initscr()
    curses.echo()
    console.clear()
    console.refresh()
    return console


def desenha_tabuleiro(j, inicial_x, inicial_y, console, esconde_navios=False):
    tabuleiro = j["tabuleiro"]
    if not console:
        inicia_cli()
    console.addstr(0 + inicial_y, 0 + inicial_x, f"P{j['id'] + 1}: {j['nome']}")
    console.addstr(1 + inicial_y, 0 + inicial_x, "BTN ")
    for x in range(len(tabuleiro[0])):
        console.addstr(1 + inicial_y, 3 + x * 2 + inicial_x, f" {x}")
    for y, linha in enumerate(tabuleiro):
        console.addstr(2 + y + inicial_y, 0 + inicial_x, f"{util.converte_numero_letra(y)} -")
        for x, coluna in enumerate(linha):
            if esconde_navios:
                console.addstr(2 + y + inicial_y, 3 + x * 2 + inicial_x, f" {tabuleiro[y][x]['estado_visivel']}")
            else:
                console.addstr(2 + y + inicial_y, 3 + x * 2 + inicial_x, f" {tabuleiro[y][x]['estado']}")
    console.refresh()


def _desenha_linha_vertical(inicial_x, inicial_y, tamanho, console):
    if not console:
        inicia_cli()
    for y in range(tamanho):
        console.addstr(y + inicial_y, inicial_x, "|")
    console.refresh()


def desenha_mapa(jogador1, jogador2):
    console = inicia_cli()
    desenha_tabuleiro(jogador1, 0, 0, console, True)
    _desenha_linha_vertical(25, 0, 12, console)
    desenha_tabuleiro(jogador2, 28, 0, console, True)
    console.refresh()


def pede_dado(y, x, tamanho, console):
    dado = console.getstr(y, x, tamanho)
    console.refresh()
    return dado


def escreve_na_tela(y, x, texto, console):
    console.addstr(y, x, str(texto))
    console.refresh()


def encerra_cli():
    curses.cbreak()
    curses.endwin()


def limpa_cli(console):
    console.clear()
    console.refresh()
