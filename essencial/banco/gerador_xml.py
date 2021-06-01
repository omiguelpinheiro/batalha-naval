import xml.etree.cElementTree as ET

from essencial.tabuleiro import gera_tabuleiro_vazio
from essencial.banco.bd_quadrado import retorna_quadrados
from essencial.banco.bd_partida import retorna_partidas
from essencial.banco.conector import conecta_servidor, inicializa_banco
from essencial.banco.bd_jogador import retorna_jogadores
from xml.dom import minidom

# insere os dados parte do jogador no xml. recebe o nome da seção onde será escrita
def cria_xml_tabuleiro(tabuleiro):
    tab = ET.Element("tabuleiro")

    for linha_de_quadrado in tabuleiro:
        for q in linha_de_quadrado:
            quadrado = ET.SubElement(tab, f"quadrado_{int(q['linha'])}{int(q['coluna'])}")
            ET.SubElement(quadrado, "id_dono").text = str(tabuleiro[int(q['linha'])][int(q['coluna'])]["id_dono"])
            ET.SubElement(quadrado, "linha").text = str(tabuleiro[int(q['linha'])][int(q['coluna'])]["linha"])
            ET.SubElement(quadrado, "coluna").text = str(tabuleiro[int(q['linha'])][int(q['coluna'])]["coluna"])
            ET.SubElement(quadrado, "n_jogada").text = str(tabuleiro[int(q['linha'])][int(q['coluna'])]["n_jogada"])
            ET.SubElement(quadrado, "estado").text = str(tabuleiro[int(q['linha'])][int(q['coluna'])]["estado"])
            ET.SubElement(quadrado, "id_navio").text = str(tabuleiro[int(q['linha'])][int(q['coluna'])]["id_navio"])
    return tab

def cria_xml_jogador(jogador):
    jog = ET.Element(f"jogador_{jogador['id_jogador']}")

    ET.SubElement(jog, "id_jogador").text = str(jogador["id_jogador"])
    ET.SubElement(jog, "nome").text = str(jogador["nome"])
    ET.SubElement(jog, "navios_tipo_1").text = str(jogador["navios_tipo_1"])
    ET.SubElement(jog, "navios_tipo_2").text = str(jogador["navios_tipo_2"])
    ET.SubElement(jog, "navios_tipo_3").text = str(jogador["navios_tipo_3"])
    ET.SubElement(jog, "navios_tipo_4").text = str(jogador["navios_tipo_4"])
    ET.SubElement(jog, "tamanho_tipo_1").text = str(jogador["tamanho_tipo_1"])
    ET.SubElement(jog, "tamanho_tipo_2").text = str(jogador["tamanho_tipo_2"])
    ET.SubElement(jog, "tamanho_tipo_3").text = str(jogador["tamanho_tipo_3"])
    ET.SubElement(jog, "tamanho_tipo_4").text = str(jogador["tamanho_tipo_4"])
    ET.SubElement(jog, "placar").text = str(jogador["placar"])
    ET.SubElement(jog, "maximo_pontos").text = str(jogador["maximo_pontos"])

    return jog

def cria_xml_partida(partida):
    par = ET.Element("partida")

    ET.SubElement(par, "id_partida").text = str(partida["id_partida"])
    ET.SubElement(par, "id_jogador1").text = str(partida["id_jogador1"])
    ET.SubElement(par, "id_jogador2").text = str(partida["id_jogador2"])
    ET.SubElement(par, "n_ultima_jogada").text = str(partida["n_ultima_jogada"])
    ET.SubElement(par, "finalizada").text = str(partida["finalizada"])
    ET.SubElement(par, "vencedor").text = str(partida["vencedor"])
    
    return par

def gera_xml(data):
    # root = ET.Element("partidas")
    i = 0
    for partida in data:
        par = cria_xml_partida(partida)
        jog_1 = cria_xml_jogador(partida["jogador_1"])
        tab_1 = cria_xml_tabuleiro(partida["jogador_1"]["tabuleiro"])
        jog_2 = cria_xml_jogador(partida["jogador_2"])
        tab_2 = cria_xml_tabuleiro(partida["jogador_2"]["tabuleiro"])
        jog_1.append(tab_1)
        jog_2.append(tab_2)
        par.append(jog_1)
        par.append(jog_2)
        # root.append(par)

        string_bonita = parse_xml_pretty_string(par)

        with open(f"essencial/saves/save_{i}.xml", "w") as f:
            f.write(string_bonita)
            
        i += 1

def retorna_banco_como_dicionario(partidas, jogadores, quadrados):
    data = list()

    p = 0
    j = 0
    q = 0

    while p < len(partidas):
        partida = dict()
        partida["id_partida"] = partidas[p]["id_partida"]
        partida["id_jogador1"] = partidas[p]["id_jogador1"]
        partida["id_jogador2"] = partidas[p]["id_jogador2"]
        partida["n_ultima_jogada"] = partidas[p]["n_ultima_jogada"]
        partida["finalizada"] = partidas[p]["finalizada"]
        partida["vencedor"] = partidas[p]["vencedor"]
        while j < len(jogadores):
            if jogadores[j]["id_jogador"] == partidas[p]["id_jogador1"]:
                partida["jogador_1"] = jogadores.pop(j)
                partida["jogador_1"]["tabuleiro"] = gera_tabuleiro_vazio()
                while q < len(quadrados):
                    if quadrados[q]["id_dono"] == partidas[p]["id_jogador1"] and quadrados[q]["n_jogada"] == 0:
                        quadrado = quadrados.pop(q)
                        partida["jogador_1"]["tabuleiro"][int(quadrado["linha"])][int(quadrado["coluna"])] = quadrado
                    else:
                        q += 1
                q = 0
            elif jogadores[j]["id_jogador"] == partidas[p]["id_jogador2"]:
                partida["jogador_2"] = jogadores.pop(j)
                partida["jogador_2"]["tabuleiro"] = gera_tabuleiro_vazio()
                while q < len(quadrados):
                    if quadrados[q]["id_dono"] == partidas[p]["id_jogador2"] and quadrados[q]["n_jogada"] == 0:
                        quadrado = quadrados.pop(q)
                        partida["jogador_2"]["tabuleiro"][int(quadrado["linha"])][int(quadrado["coluna"])] = quadrado
                    else:
                        q += 1
                q = 0
            else:
                j += 1
        j = 0
        data.append(partida)
        p += 1

    return data

def parse_xml_pretty_string(root):
    return minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")

def main():
    con = conecta_servidor()
    cursor = inicializa_banco(con)
    partidas = retorna_partidas(cursor)
    jogadores = retorna_jogadores(cursor)
    quadrados = retorna_quadrados(cursor)

    data = retorna_banco_como_dicionario(partidas, jogadores, quadrados)
    gera_xml(data)
