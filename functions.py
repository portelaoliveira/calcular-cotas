import matplotlib.pyplot as plt
import math


def read_file(filename: str) -> list[float]:
    """
    Função para ler arquivos .txt

    - filename: arquivo de entrada do tipo string;
    - retorna uma lista.
    """

    file = open(filename, "r")
    datas = file.readlines()

    return datas


def get_values(datas: list[float]) -> list[float]:
    """
    Função para pegar os valores do arquivo .txt

    - datas: arquivo de entrada do tipo list;
    - retorna uma lista dos valores.
    """

    id = []
    elevations = []
    distances = []
    # Definindo colunas
    for i in range(1, len(datas)):
        id_landmark = datas[i].split(",")[0]
        id.append(id_landmark)
        height = datas[i].split(",")[1]
        elevations.append(float(height))
        distance = datas[i].split(",")[2]
        distances.append(float(distance))

    return id, elevations, distances


def calculate_angles(
    elevations: list[float], horizontal_distance: int = 100
) -> list[float]:
    """
    Função para calcular o ângulo entre os pontos

    - elevations: lista contendo os valores das cotas do tipo list;
    - horizontal_distance: definindo a distância horizontal padrão entre os pontos do tipo int;
    - retorna uma lista dos valores.
    """

    # Definindo a distância horizontal padrão entre os pontos
    dx = horizontal_distance
    # Definindo ângulos entre os pontos
    a = (int(elevations[1]) - int(elevations[0])) / dx
    ab = math.degrees(math.atan(a))  # ângulo do ponto 1 ao 2
    b = (int(elevations[2]) - int(elevations[1])) / dx
    bc = math.degrees(math.atan(b))  # ângulo do ponto 2 ao 3
    c = (int(elevations[3]) - int(elevations[2])) / dx
    cd = math.degrees(math.atan(c))  # ângulo do ponto 3 ao 4
    d = (int(elevations[4]) - int(elevations[3])) / dx
    de = math.degrees(math.atan(d))  # ângulo do ponto 4 ao 5
    e = (int(elevations[5]) - int(elevations[4])) / dx
    ef = math.degrees(math.atan(e))  # ângulo do ponto 5 ao 6
    f = (int(elevations[6]) - int(elevations[5])) / dx
    fg = math.degrees(math.atan(f))  # ângulo do ponto 6 ao 7
    g = (int(elevations[7]) - int(elevations[6])) / dx
    gh = math.degrees(math.atan(g))  # ângulo do ponto 7 ao 8
    h = (int(elevations[8]) - int(elevations[7])) / dx
    hi = math.degrees(math.atan(h))  # ângulo do ponto 8 ao 9
    i = (int(elevations[9]) - int(elevations[8])) / dx
    ij = math.degrees(math.atan(i))  # ângulo do ponto 9 ao 10
    j = (int(elevations[10]) - int(elevations[9])) / dx
    jk = math.degrees(math.atan(j))  # ângulo do ponto 10 ao 11
    # Criando lista com os valores dos ângulos
    angles = [ab, bc, cd, de, ef, fg, gh, hi, ij, jk]

    return angles


def calculate_elevation_to_distance_20m(elevations, angles):
    anv = (math.tan(math.radians(angles[0]))) * (20) + int(elevations[0])
    bnv = (math.tan(math.radians(angles[0]))) * (20) + int(anv)
    cnv = (math.tan(math.radians(angles[0]))) * (20) + int(bnv)
    dnv = (math.tan(math.radians(angles[0]))) * (20) + int(cnv)
    fnv = (math.tan(math.radians(angles[1]))) * (20) + int(elevations[1])
    gnv = (math.tan(math.radians(angles[1]))) * (20) + int(fnv)
    hnv = (math.tan(math.radians(angles[1]))) * (20) + int(gnv)
    inv = (math.tan(math.radians(angles[1]))) * (20) + int(hnv)
    knv = (math.tan(math.radians(angles[2]))) * ((-20) * (-1)) + int(elevations[2])
    lnv = (math.tan(math.radians(angles[2]))) * ((-20) * (-1)) + int(knv)
    mnv = (math.tan(math.radians(angles[2]))) * ((-20) * (-1)) + int(lnv)
    nnv = (math.tan(math.radians(angles[2]))) * ((-20) * (-1)) + int(mnv)
    pnv = (math.tan(math.radians(angles[3]))) * (20) + int(elevations[3])
    qnv = (math.tan(math.radians(angles[3]))) * (20) + int(pnv)
    rnv = (math.tan(math.radians(angles[3]))) * (20) + int(qnv)
    snv = (math.tan(math.radians(angles[3]))) * (20) + int(rnv)
    unv = (math.tan(math.radians(angles[4]))) * ((-20) * (-1)) + int(elevations[4])
    vnv = (math.tan(math.radians(angles[4]))) * ((-20) * (-1)) + int(unv)
    wnv = (math.tan(math.radians(angles[4]))) * ((-20) * (-1)) + int(vnv)
    xnv = (math.tan(math.radians(angles[4]))) * ((-20) * (-1)) + int(wnv)
    znv = (math.tan(math.radians(angles[5]))) * (20) + int(elevations[5])
    aan = (math.tan(math.radians(angles[5]))) * (20) + int(znv)
    bbn = (math.tan(math.radians(angles[5]))) * (20) + int(aan)
    ccn = (math.tan(math.radians(angles[5]))) * (20) + int(bbn)
    een = (math.tan(math.radians(angles[6]))) * (20) + int(elevations[6])
    ffn = (math.tan(math.radians(angles[6]))) * (20) + int(een)
    ggn = (math.tan(math.radians(angles[6]))) * (20) + int(ffn)
    hhn = (math.tan(math.radians(angles[6]))) * (20) + int(ggn)
    jjn = (math.tan(math.radians(angles[7]))) * (20) + int(elevations[7])
    kkn = (math.tan(math.radians(angles[7]))) * (20) + int(jjn)
    lln = (math.tan(math.radians(angles[7]))) * (20) + int(kkn)
    mmn = (math.tan(math.radians(angles[7]))) * (20) + int(lln)
    oon = (math.tan(math.radians(angles[8]))) * ((-20) * (-1)) + int(elevations[8])
    ppn = (math.tan(math.radians(angles[8]))) * ((-20) * (-1)) + int(oon)
    qqn = (math.tan(math.radians(angles[8]))) * ((-20) * (-1)) + int(ppn)
    rrn = (math.tan(math.radians(angles[8]))) * ((-20) * (-1)) + int(qqn)
    ttn = (math.tan(math.radians(angles[9]))) * (20) + int(elevations[9])
    uun = (math.tan(math.radians(angles[9]))) * (20) + int(ttn)
    vvn = (math.tan(math.radians(angles[9]))) * (20) + int(uun)
    wwn = (math.tan(math.radians(angles[9]))) * (20) + int(vvn)

    distances = list(range(20, 1000, 20))

    new_elevations = [
        anv,
        bnv,
        cnv,
        dnv,
        fnv,
        gnv,
        hnv,
        inv,
        knv,
        lnv,
        mnv,
        nnv,
        pnv,
        qnv,
        rnv,
        snv,
        unv,
        vnv,
        wnv,
        xnv,
        znv,
        aan,
        bbn,
        ccn,
        een,
        ffn,
        ggn,
        hhn,
        jjn,
        kkn,
        lln,
        mmn,
        oon,
        ppn,
        qqn,
        rrn,
        ttn,
        uun,
        vvn,
        wwn,
    ]

    return new_elevations, distances


def gen_plot(x_axis: list[float], y_axis: list[float], name_figure: str):
    """
    Função para gerar e salvar gráficos no formato png

    - x_axis: lista contendo os valores para o eixo x do tipo list;
    - y_axis: lista contendo os valores para o eixo y do tipo list;
    - name_figure: nome de saída para figura.
    """

    plt.figure(1)
    plt.subplot(1, 1, 1)
    plt.plot(x_axis, y_axis, "ko-")
    plt.xlabel("Distância (m)")
    plt.ylabel("Valor de cota (m)")
    plt.grid(True)
    plt.savefig(name_figure, dpi=500)
    plt.close("all")


if __name__ == "__main__":
    datas = read_file("dados.txt")
    id, elevations, distances = get_values(datas)
    angles = calculate_angles(elevations)
    gen_plot(distances, elevations, "teste.png")
    # print(angles)
    # print(elevations)
