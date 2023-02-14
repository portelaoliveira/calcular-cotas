import math

import matplotlib.pyplot as plt
import numpy as np

# from scipy.interpolate import CubicSpline


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


def cubic_spline(x, x0, y0) -> list[float]:
    """
    Função para calcular o ângulo entre os pontos

    - x: lista ou array contendo os valores de x que devem ser calculados os valores de y;
    - x0: lista ou array contendo os valores de x em que y são conhecidos
    - y0: lista ou array contendo os valores de y referentes a x0
    - retorna uma lista dos valores de y interpolados a partir de x0 e y0
    """

    x0 = np.asfarray(x0)
    y0 = np.asfarray(y0)

    xdiff = np.diff(x0)
    dydx = np.diff(y0)
    dydx /= xdiff

    N = len(x0)

    w = np.empty(N - 1, float)
    z = np.empty(N, float)

    w[0] = 0.0
    z[0] = 0.0
    for i in range(1, N - 1):
        m = xdiff[i - 1] * (2 - w[i - 1]) + 2 * xdiff[i]
        w[i] = xdiff[i] / m
        z[i] = (6 * (dydx[i] - dydx[i - 1]) - xdiff[i - 1] * z[i - 1]) / m
    z[-1] = 0.0

    for i in range(N - 2, -1, -1):
        z[i] = z[i] - w[i] * z[i + 1]

    # encontrar índice (requer x já está classificado)
    index = x0.searchsorted(x)
    np.clip(index, 1, N - 1, index)

    xi1, xi0 = x0[index], x0[index - 1]
    yi1, yi0 = y0[index], y0[index - 1]
    zi1, zi0 = z[index], z[index - 1]
    hi1 = xi1 - xi0

    # calcular cúbico
    y = (
        zi0 / (6 * hi1) * (xi1 - x) ** 3
        + zi1 / (6 * hi1) * (x - xi0) ** 3
        + (yi1 / hi1 - zi1 * hi1 / 6) * (x - xi0)
        + (yi0 / hi1 - zi0 * hi1 / 6) * (xi1 - x)
    )
    return y


def calculate_elevation_to_distance_20m(
    elevations: list[float], angles: list[float]
) -> list[float]:
    """
    Função para calcular as novas cotas para a distância horizontal em 20 m.

    - elevations: valores das cotas iniciais;
    - angles: ângulos calculados entre cada ponto das cotas iniciais.
    """

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

    new_distances_20m = [
        20,
        40,
        60,
        80,
        120,
        140,
        160,
        180,
        220,
        240,
        260,
        280,
        320,
        340,
        360,
        380,
        420,
        440,
        460,
        480,
        520,
        540,
        560,
        580,
        620,
        640,
        660,
        680,
        720,
        740,
        760,
        780,
        820,
        840,
        860,
        880,
        920,
        940,
        960,
        980,
    ]

    new_elevations_to_20m = [
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

    return new_elevations_to_20m, new_distances_20m


def calculate_elevation_to_distance_25m(
    elevations: list[float], angles: list[float]
) -> list[float]:
    """
    Função para calcular as novas cotas para a distância horizontal em 25 m.

    - elevations: valores das cotas iniciais;
    - angles: ângulos calculados entre cada ponto das cotas iniciais.
    """

    anv = (math.tan(math.radians(angles[0]))) * (25) + int(elevations[0])
    bnv = (math.tan(math.radians(angles[0]))) * (25) + int(anv)
    cnv = (math.tan(math.radians(angles[0]))) * (25) + int(bnv)
    env = (math.tan(math.radians(angles[1]))) * (25) + int((elevations[1]))
    fnv = (math.tan(math.radians(angles[1]))) * (25) + int(env)
    gnv = (math.tan(math.radians(angles[1]))) * (25) + int(fnv)
    inv = (math.tan(math.radians(angles[2]))) * ((-25) * (-1)) + int(elevations[2])
    jnv = (math.tan(math.radians(angles[2]))) * ((-25) * (-1)) + int(inv)
    knv = (math.tan(math.radians(angles[2]))) * ((-25) * (-1)) + int(jnv)
    mnv = (math.tan(math.radians(angles[3]))) * (25) + int(elevations[3])
    nnv = (math.tan(math.radians(angles[3]))) * (25) + int(mnv)
    onv = (math.tan(math.radians(angles[3]))) * (25) + int(nnv)
    qnv = (math.tan(math.radians(angles[4]))) * ((-25) * (-1)) + int(elevations[4])
    rnv = (math.tan(math.radians(angles[4]))) * ((-25) * (-1)) + int(qnv)
    snv = (math.tan(math.radians(angles[4]))) * ((-25) * (-1)) + int(rnv)
    unv = (math.tan(math.radians(angles[5]))) * (25) + int(elevations[5])
    vnv = (math.tan(math.radians(angles[5]))) * (25) + int(unv)
    wnv = (math.tan(math.radians(angles[5]))) * (25) + int(vnv)
    ynv = (math.tan(math.radians(angles[6]))) * (25) + int(elevations[6])
    znv = (math.tan(math.radians(angles[6]))) * (25) + int(ynv)
    aan = (math.tan(math.radians(angles[6]))) * (25) + int(znv)
    ccn = (math.tan(math.radians(angles[7]))) * (25) + int(elevations[7])
    ddn = (math.tan(math.radians(angles[7]))) * (25) + int(ccn)
    een = (math.tan(math.radians(angles[7]))) * (25) + int(ddn)
    ggn = (math.tan(math.radians(angles[8]))) * ((-25) * (-1)) + int(elevations[8])
    hhn = (math.tan(math.radians(angles[8]))) * ((-25) * (-1)) + int(ggn)
    iin = (math.tan(math.radians(angles[8]))) * ((-25) * (-1)) + int(hhn)
    kkn = (math.tan(math.radians(angles[9]))) * (25) + int(elevations[9])
    lln = (math.tan(math.radians(angles[9]))) * (25) + int(kkn)
    mmn = (math.tan(math.radians(angles[9]))) * (25) + int(lln)

    new_elevations_to_25m = [
        anv,
        bnv,
        cnv,
        env,
        fnv,
        gnv,
        inv,
        jnv,
        knv,
        mnv,
        nnv,
        onv,
        qnv,
        rnv,
        snv,
        unv,
        vnv,
        wnv,
        ynv,
        znv,
        aan,
        ccn,
        ddn,
        een,
        ggn,
        hhn,
        iin,
        kkn,
        lln,
        mmn,
    ]
    new_distances_25m = [
        25,
        50,
        75,
        125,
        150,
        175,
        225,
        250,
        275,
        325,
        350,
        375,
        425,
        450,
        475,
        525,
        550,
        575,
        625,
        650,
        675,
        725,
        750,
        775,
        825,
        850,
        875,
        925,
        950,
        975,
    ]

    return new_elevations_to_25m, new_distances_25m


def gen_plot_for_the_initial_values(
    x_axis: list[float], y_axis: list[float], name_figure: str
):
    """
    Função para gerar e salvar gráficos no formato png para os valores iniciais das cotas

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


def gen_plot_for_the_new_values(
    x_axis: list[float],
    y_axis: list[float],
    new_x_axis: list[float],
    new_y_axis: list[float],
    name_figure: str,
):
    """
    Função para gerar e salvar gráficos no formato png para os novos valores das cotas

    - x_axis: lista contendo os valores para o eixo x do tipo list;
    - y_axis: lista contendo os valores para o eixo y do tipo list;
    - name_figure: nome de saída para figura.
    """

    plt.subplot(1, 1, 1)
    plt.plot(x_axis, y_axis, "ko-")
    plt.plot(new_x_axis, new_y_axis, "ro")
    plt.xlabel("Distância (m)")
    plt.ylabel("Valor de cota (m)")
    plt.grid(True)
    plt.savefig(name_figure, dpi=500)
    plt.close("all")


if __name__ == "__main__":
    datas = read_file("dados.txt")
    id, elevations, distances = get_values(datas)
    angles = calculate_angles(elevations)
    new_elevations_to_20m, new_distances_to_20m = calculate_elevation_to_distance_20m(
        elevations, angles
    )
    new_elevations_to_25m, new_distances_to_25m = calculate_elevation_to_distance_25m(
        elevations, angles
    )
    gen_plot_for_the_initial_values(distances, elevations, "teste.png")
    gen_plot_for_the_new_values(
        distances, elevations, new_distances_to_20m, new_elevations_to_20m, "teste1.png"
    )
    gen_plot_for_the_new_values(
        distances, elevations, new_distances_to_25m, new_elevations_to_25m, "teste2.png"
    )

    x0 = distances
    y0 = elevations
    spacing = 20
    x = np.arange(np.min(x0), np.max(x0) + 0.01, spacing)
    y = cubic_spline(x, x0, y0)

    gen_plot_for_the_new_values(x0, y0, x, y, "teste3.png")
