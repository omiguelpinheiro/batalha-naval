from mysql.connector.connection import MySQLConnection
from essencial.banco.bd_quadrado import atualiza_quadrado, cria_quadrado_banco, cria_tabela_quadrado, retorna_ultima_jogada
from essencial import quadrado, tabuleiro, util
from essencial.banco.bd_jogador import *

__all__ = ["consulta_jogador", "registra_jogador", "_jogadores"]  # O que será importado com "import jogador"


_jogadores: list = []  # Lista de jogadores registrados até o momento.
_tamanho_navios: dict = {0: 2, 1: 3, 2: 4, 3: 5}  # Dicionário de pares chave-valor (tipo_navio, tamanho)


def registra_jogador(nome: str, cursor: CursorBase, con: MySQLConnection) -> int:
    """Registra um novo jogador na partida.

    Jogador é um dicionário com as seguintes chaves:
        nome (str): O nome do jogador.
        navios (list): Informações sobre os navios do jogador.
        placar (int): O placar do jogador.
        navios_disponíveis (dict): Pares chave valor dizendo quantos navios
            de cada tipo o jogador posicionará. Os pares são do
            tipo (tipo: int, quantidade: int).
        maximo_pontos (str): A quantidade de pontos que o jogador precisa para ganhar.
        id (int): A id do jogador na partida.
        id_banco (int): A id do jogador no banco de dados.

    Args:
        nome (str): O nome do jogador.
        current_cursor (CursorBase): Cursor aberto que executará as queries.
        con (MySQLConnection): Uma conexão estabelecida com o banco de dados.

    Returns:
        A função retornará:
           -2: Se não conseguiu ler a última ID de Jogador.
           -1: Se o jogador não foi criado no banco.
            0: Se já tem 2 jogadores cadastrados.
            1: O jogador foi cadastrado com sucesso.

    """
    jogadores = _lista_jogadores()

    jogador = {
        'navios': [],
        'nome': nome,
        'placar': 0,
        'navios_disponiveis': {0: 4, 1: 3, 2: 2, 3: 1},
    }

    maximo_pontos = 0
    if maximo_pontos == 0:
        for navio in jogador["navios_disponiveis"]:
            maximo_pontos += jogador["navios_disponiveis"][navio] * _tamanho_navios[navio]

    jogador["maximo_pontos"] = maximo_pontos

    if len(jogadores) == 0:
        jogador["id"] = 0
    elif len(jogadores) == 1:
        jogador["id"] = 1
    else:
        return 0

    tamanho_tipo_1 = _tamanho_navios[0]
    tamanho_tipo_2 = _tamanho_navios[1]
    tamanho_tipo_3 = _tamanho_navios[2]
    tamanho_tipo_4 = _tamanho_navios[3]

    navios_tipo_1 = jogador["navios_disponiveis"][0]
    navios_tipo_2 = jogador["navios_disponiveis"][1]
    navios_tipo_3 = jogador["navios_disponiveis"][2]
    navios_tipo_4 = jogador["navios_disponiveis"][3]

    result = cria_jogador_banco(jogador["nome"], navios_tipo_1, navios_tipo_2, navios_tipo_3, navios_tipo_4, tamanho_tipo_1, tamanho_tipo_2, tamanho_tipo_3, tamanho_tipo_4, 0, maximo_pontos, cursor)
    if result == 0:
        return -1
    try:
        con.commit()
    except Exception as e:
        return -1

    ultimo_id = le_ultimo_id_jogador(cursor)
    if ultimo_id == -1:
        return -2
    jogador["id_banco"] = ultimo_id

    _registra_tabuleiro(jogador, cursor)

    _jogadores.append(jogador)

    return 1


def consulta_jogador(id_jogador: int) -> dict:
    """Retorna informações do jogador.

    Args:
        id_jogador: ID do jogador cujas informações deseja-se obter.

    Returns:
        Dicionário com as informações do jogador especificado ou um
            dicionário vazio caso o jogador não seja encontrado.

    """
    jogadores = _lista_jogadores()
    for jogador in jogadores:
        if jogador["id"] == id_jogador:
            return jogador
    return {}


def posiciona_navio(id_navio: int, quadrado_inicio: str, orientacao: str, id_jogador: int, cursor: CursorBase) -> int:
    """Posiciona um navio no tabuleiro de um jogador.

    Preenche quadrados da direita para a esquerda caso a orientação seja
    horizontal ou de baixo para cima caso a orientação seja vertical.

    Para saber quais ids de navios existem referencie _tamanho_navios
    que mapeia uma id de navio para o seu tamanho.

    Tipos quadrado_inicio aceitos são "A-8", "a-8", "A8" e "a8".

    Tipos de orientacao aceitas são "V", "v", "H", "h".

    id_jogador precisa ser 0 ou 1.

    Args:
        id_navio: Tipo do navio a ser posicionado.
        quadrado_inicio: Quadrado a partir de onde começará a ser posicionado o navio.
        orientacao: Orientação do navio. Horizontal ou vertical.
        id_jogador: ID do jogador cujo tabuleiro será preenchido.
        current_cursor (CursorBase): Cursor aberto que executará as queries.

    Returns:
        A função retornará:
            1: O navio foi posicionado com sucesso.
            0: ID de navio inválida.
           -1: Coordenada para quadrado de início inválida.
           -2: Orientação inválida.
           -3: ID de jogador inválida.
           -4: Já acabaram os navios desse tipo.
           -5: Mapa insuficiente para posicionar navio na horizontal.
           -6: Mapa insuficiente para posicionar navio na vertical.
           -7: Sobreposição de navios.
           -8: Não atualizou a quantidade de navios no banco de dados.
           -9: Não atualizou o quadrado no banco de dados.

    """
    if "-" in quadrado_inicio:
        quadrado_inicio = quadrado_inicio.split("-")

    try:
        if len(quadrado_inicio) <= 1 or len(quadrado_inicio) >= 3:
            return -1
        int(quadrado_inicio[1])
    except Exception as e:
        return -1

    numero_linha = util.converte_letra_numero(quadrado_inicio[0])
    numero_coluna = int(quadrado_inicio[1])

    if not isinstance(id_navio, int):
        try:
            id_navio = int(id_navio)
        except Exception as e:
            return 0
    if id_navio < 0 or id_navio > 3:
                return 0

    orientacao = orientacao.upper()

    tamanho_navio = _tamanho_navios[id_navio]

    if not quadrado_inicio[0].isalpha() or not quadrado_inicio[1].isnumeric():
        return -1
    if orientacao not in ["V", "H"]:
        return -2
    if id_jogador not in [0, 1]:
        return -3
    if consulta_jogador(id_jogador)["navios_disponiveis"][id_navio] <= 0:
        return -4
    if int(quadrado_inicio[1]) + 1 - tamanho_navio < 0 and orientacao == "H":
        return -5
    if util.converte_letra_numero(quadrado_inicio[0]) + 1 - tamanho_navio < 0 and orientacao == "V":
        return -6

    coordenada_navio = []

    for parte in range(tamanho_navio):
        if orientacao == "H":
            coordenada_navio.append([numero_linha, numero_coluna - parte])


        elif orientacao == "V":
            coordenada_navio.append([numero_linha - parte, numero_coluna])
    for navio in _jogadores[id_jogador]["navios"]:
       for parte in navio["ocupando"]:
          if parte in coordenada_navio:
                return -7

    navio = {"tipo": id_navio, "ocupando": coordenada_navio, "destruido": False}

    _jogadores[id_jogador]["navios"].append(navio)
    _jogadores[id_jogador]["navios_disponiveis"][id_navio] -= 1
    retorno = atualiza_quantidade_navios_jogador(_jogadores[id_jogador]["id_banco"], id_navio, _jogadores[id_jogador]["navios_disponiveis"][id_navio], cursor)
    if retorno == 0:
        return -8

    if orientacao == "V":
        for parte in range(tamanho_navio):
            quadrado_original = _jogadores[id_jogador]["tabuleiro"][numero_linha - parte][numero_coluna]
            quadrado_novo = quadrado.altera_estado(quadrado_original, "H")
            _jogadores[id_jogador]["tabuleiro"][numero_linha - parte][numero_coluna] = quadrado_novo
            retorno = atualiza_quadrado(_jogadores[id_jogador]["id_banco"], numero_linha - parte, numero_coluna, 0, "H", len(_jogadores[id_jogador]["navios"]) - 1, cursor)
            if retorno == 0:
                return -9
    return 1


def ataca_jogador(id_atacante: int, id_atacado: int, coordenada: str, cursor: CursorBase) -> int:
    """Ataca um jogador.

    Tipos quadrado_inicio aceitos são "A-8", "a-8", "A8" e "a8".

    Args:
        id_atacante: ID do jogador que está atacando.
        id_atacado: ID do jogador que está sendo atacado.
        coordenada: Coordenada do quadrante atacado.
        current_cursor (CursorBase): Cursor aberto que executará as queries.

    Returns:
        A função retornará:
            4: Jogador foi atacado com sucesso e atingiu água.
            3: Jogador foi atacado com sucesso e teve um navio destruído.
            2: Jogador foi atacado com sucesso e destruiu uma parte do navio.
            1: jogador foi atacado com sucesso e ocorreu vitória do atacante.
           -1: Coordenada de quadrante inválida.
           -2: Coordenada de quadrante já foi atacada.
           -3: Não atualizou o placar do jogador.
           -4: Não criou o quadrado da jogada no banco.
    
    """
    
    if "-" in coordenada:
        coordenada = coordenada.split("-")
    try:
        if len(coordenada) <= 1 or ((not coordenada[0].isalpha() or not coordenada[1].isnumeric()) and len(coordenada) >= 3):
            return -1
        int(coordenada[1])
    except Exception as e:
        return -1

    numero_linha = util.converte_letra_numero(coordenada[0])
    numero_coluna = int(coordenada[1])

    estado_quadrado_visivel = _jogadores[id_atacado]["tabuleiro"][numero_linha][numero_coluna]["estado_visivel"]
    if estado_quadrado_visivel in ["D", "W"]:
        return -2

    estado_quadrado = _jogadores[id_atacado]["tabuleiro"][numero_linha][numero_coluna]["estado"]
    if estado_quadrado == "H":
        _jogadores[id_atacado]["tabuleiro"][numero_linha][numero_coluna]["estado_visivel"] = "D"
        _jogadores[id_atacado]["tabuleiro"][numero_linha][numero_coluna]["estado"] = "D"
        _jogadores[id_atacante]["placar"] += 1
        retorno = atualiza_placar_jogador(_jogadores[id_atacante]["id_banco"], _jogadores[id_atacante]["placar"], cursor)
        if retorno == 0:
            return -3
        for i, navio in enumerate(_jogadores[id_atacado]["navios"]):
            if [numero_linha, numero_coluna] in navio["ocupando"]:
                _jogadores[id_atacado]["navios"][i]["ocupando"].remove([numero_linha, numero_coluna])
                retorno = cria_quadrado_banco(_jogadores[id_atacado]["id_banco"], numero_linha, numero_coluna, retorna_ultima_jogada(_jogadores[0]["id_banco"], _jogadores[1]["id_banco"], cursor) + 1, "D", i, cursor)
                if retorno == 0:
                    return -4
                if len(_jogadores[id_atacado]["navios"][i]["ocupando"]) == 0 and _jogadores[id_atacante]["placar"] == _jogadores[id_atacante]["maximo_pontos"]:
                    return 1
                elif len(_jogadores[id_atacado]["navios"][i]["ocupando"]) == 0:
                    return 3
                return 2
    if estado_quadrado == "N":
        _jogadores[id_atacado]["tabuleiro"][numero_linha][numero_coluna]["estado"] = "W"
        _jogadores[id_atacado]["tabuleiro"][numero_linha][numero_coluna]["estado_visivel"] = "W"
        retorno = cria_quadrado_banco(_jogadores[id_atacado]["id_banco"], numero_linha, numero_coluna, retorna_ultima_jogada(_jogadores[0]["id_banco"], _jogadores[1]["id_banco"], cursor) + 1, "W", -1, cursor)
        if retorno == 0:
            return -4
        return 4


def _lista_jogadores() -> list:
    """Função que retorna a lista de jogadores atualmente na partida.

    Returns:
        list: Lista dos jogadores registrados atualmente.

    """
    return _jogadores


def _registra_tabuleiro(jogador: dict, cursor: CursorBase):
    """Adiciona o tabuleiro ao jogador.

    Args:
        jogador: Jogador que receberá o tabuleiro.
        current_cursor (CursorBase): Cursor aberto que executará as queries.

    """
    tab = tabuleiro.gera_tabuleiro(jogador["id_banco"], cursor)
    jogador["tabuleiro"] = tab
    return jogador
