import os
import xml.etree.cElementTree as ET

from xml.etree.ElementTree import ElementTree
from essencial.banco.conector import conecta_servidor, inicializa_banco
from essencial.banco.bd_jogador import retorna_jogadores
from essencial.banco.bd_partida import retorna_partidas
from essencial.banco.bd_quadrado import retorna_quadrados
from essencial.tabuleiro import gera_tabuleiro_vazio
from typing import Dict, List, Tuple
from xml.dom import minidom


def cria_xml_tabuleiro(tabuleiro: Dict) -> ElementTree:
    """Cria a representação do tabuleiro em XML.

    Args:
        tabuleiro (Dict): O tabuleiro que será convertido.

    Returns:
        ElementTree: O tabuleiro em XML.
    """
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


def cria_xml_jogador(jogador: Dict) -> ElementTree:
    """Cria a representação do jogador em XML.

    Args:
        jogador (Dict): O jogador que será convertido.

    Returns:
        ElementTree: O jogador em XML.
    """
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


def cria_xml_partida(partida: Dict) -> ElementTree:
    """Cria a representação da partida em XML.

    Args:
        partida (Dict): A partida que será convertida.

    Returns:
        ElementTree: A partida em XML.
    """
    par = ET.Element("partida")

    ET.SubElement(par, "id_partida").text = str(partida["id_partida"])
    ET.SubElement(par, "id_jogador1").text = str(partida["id_jogador1"])
    ET.SubElement(par, "id_jogador2").text = str(partida["id_jogador2"])
    ET.SubElement(par, "n_ultima_jogada").text = str(partida["n_ultima_jogada"])
    ET.SubElement(par, "finalizada").text = str(partida["finalizada"])
    ET.SubElement(par, "vencedor").text = str(partida["vencedor"])
    
    return par


def gera_xml(dados: Dict) -> int:
    """Função que gera o XML de uma partida.

    Args:
        dados (Dict): Dicionário contendo as informações das partidas, jogadores e quadrados.

    Returns:
        int: 1 se o XML foi construído com sucesso.
             0 se o XML não foi construído.
    """
    try:
        # root = ET.Element("partidas")
        i = 0
        for partida in dados:
            par = cria_xml_partida(partida)
            print(type(par))
            jog_1 = cria_xml_jogador(partida["jogador_1"])
            print(type(jog_1))
            tab_1 = cria_xml_tabuleiro(partida["jogador_1"]["tabuleiro"])
            print(type(tab_1))
            jog_2 = cria_xml_jogador(partida["jogador_2"])
            tab_2 = cria_xml_tabuleiro(partida["jogador_2"]["tabuleiro"])
            jog_1.append(tab_1)
            jog_2.append(tab_2)
            par.append(jog_1)
            par.append(jog_2)
            # root.append(par)

            string_bonita = parse_xml_pretty_string(par)

            if not os.path.exists("essencial/saves"):
                os.makedirs("essencial/saves")
            with open(f"essencial/saves/save_{i}.xml", "w") as f:
                f.write(string_bonita)
                
            i += 1
        return 1
    except Exception as e:
        print("Não conseguiu salvar os saves rsrs", e)
        return 0


def retorna_banco_como_dicionario(partidas: List[Tuple], jogadores: List[Tuple], quadrados: List[Tuple]) -> Dict:
    """Transforma informações obtidas do banco em um dicionário.

    Args:
        partidas (List[Tuple]): Informações sobre as partidas que estão no banco.
        jogadores (List[Tuple]): Informações sobre os jogadores que estão no banco.
        quadrados (List[Tuple]): Informçãoes sobre os quadrados que estão no banco.

    Returns:
        Dict: Um dicionário com uma estrutura organizada que facilita a sua transformação em XML.
    """
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


def parse_xml_pretty_string(root: ElementTree) -> str:
    """Transforma um ElementTree em uma string bonita.

    Args:
        root (ElementTree): Quem se deseja transformar.

    Returns:
        str: String preparada para ser utilizada num PrettyPrint do XML.
    """
    return minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
