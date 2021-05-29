from logging import PlaceHolder
from xml.dom import minidom
from essencial.partida import le_ultimo_id_partida
from essencial.jogador import _lista_jogadores

"""
<root>

    <jogadores>
        <jogador_1>
            <id> int </id>
            <nome> varchar </nome>
            <tipo_1> int </tipo_1>
            <tipo_2> int </tipo_2>
            <tipo_3> int </tipo_3>
            <tipo_4> int </tipo_4>
                  
            </jogador_1>

        <jogador_2>
            <id> int </id>
            <nome> varchar </nome>
            <tipo_1> int </tipo_1>
            <tipo_2> int </tipo_2>
            <tipo_3> int </tipo_3>
            <tipo_4> int </tipo_4>
            </jogador_2>

    </jogadores>

    <partida>
        <id_ultima_partida> int </id_ultima_partida>
        <id> int </id>
        <id> int </id>
        <n_ultima_jogada> int </n_ultima_jogada>
        <finalizada> bool </finalizada>
    </partida>

</root>
"""
# insere os dados parte do jogador no xml. recebe o nome da seção onde será escrita


def gera_xml_jogador(pai, n):

    info_jogador = _lista_jogadores()
    label_jogadores = pai.createElement("jogadores")

    jogador_xml = label_jogadores.createElement(f"jogador {0+n}")
    jogador_xml.setAttribute("id", info_jogador[n]["id"])
    for i in range(4):
        jogador_xml.setAttribute(
            f"tipo_{i+1}", info_jogador[n]["navios_disponiveis"][i])
    return

# insere os dados partida no xml. recebe o nome da seção onde será escrita


def gera_xml_partida(pai):

    info_jogador = _lista_jogadores()
    id_partida = le_ultimo_id_partida()

    # inclui os dados a partida
    partida_xml = pai.createElement("partida")
    # nao preciso no id no resto do programa. so aqui.

    partida_xml.setAttribute("id_ultima_partida", id_partida)
    for i in range(2):
        partida_xml.setAttribute(f"jogador {i}", info_jogador[i]["id"])

    partida_xml.setAttribute("n_ultima_jogada", PlaceHolder)
    partida_xml.setAttribute("finalizada", PlaceHolder)

    return


def gera_xml_quadrado(pai):

    info_jogador = _lista_jogadores()

    gera_xml_quadrado = pai.createElement("quadrado")

    # linha,
    # coluna,
    # n_jogada,
    # estado,

    return


def gera_xml():

    # base do documento
    root = minidom.Document()

    xml = root.createElement('root')
    root.appendChild(xml)

    for k in range(2):
        gera_xml_jogador(root, k)

    gera_xml_partida(root)

    return
