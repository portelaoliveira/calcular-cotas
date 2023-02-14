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
    - horizontal_distance: Definindo a distância horizontal padrão entre os pontos do tipo int
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


def cubic_spline(
    x: list | np.ndarray, x0: list | np.ndarray, y0: list | np.ndarray
) -> list[float]:
    """
    Função para calcular o ângulo entre os pontos

    - x: lista ou array contendo os valores de x que devem ser calculados os valores de y;
    - x0: lista ou array contendo os valores de x em que y são conhecidos
    - y0: lista ou array contendo os valores de y referentes a x0
    - retorna uma lista dos valores de y interpolados a partir de x0 e y0
    """

    # return CubicSpline(x0,y0,bc_type='natural')(x).tolist()

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

    # find index (it requires x is already sorted)
    index = x0.searchsorted(x)
    np.clip(index, 1, N - 1, index)

    xi1, xi0 = x0[index], x0[index - 1]
    yi1, yi0 = y0[index], y0[index - 1]
    zi1, zi0 = z[index], z[index - 1]
    hi1 = xi1 - xi0

    # calculate cubic
    y = (
        zi0 / (6 * hi1) * (xi1 - x) ** 3
        + zi1 / (6 * hi1) * (x - xi0) ** 3
        + (yi1 / hi1 - zi1 * hi1 / 6) * (x - xi0)
        + (yi0 / hi1 - zi0 * hi1 / 6) * (xi1 - x)
    )
    return y


def gen_plot(x_axis: list[float], y_axis: list[float], name_figure: str):
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
    # print(angles)
    # print(elevations)

    x0 = distances
    y0 = elevations
    spacing = 5
    x = np.arange(np.min(x0), np.max(x0) + 0.01, spacing)
    y = cubic_spline(x, x0, y0)
