import matplotlib.pyplot as plt
import numpy as np


def read_file(filename: str) -> list[float]:
    """
    Função para ler arquivos .txt.

    - filename: arquivo de entrada;
    - retorna uma lista.
    """

    file = open(filename, "r")
    datas = file.readlines()

    return datas


def get_values(datas: list[float]) -> list[float]:
    """
    Função para pegar os valores do arquivo .txt.

    - datas: arquivo de entrada;
    - retorna uma lista com os valores.
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


def linear_interpolation(
    x: list[float], y: list[float], x_new: list[float]
) -> list[float]:
    """
    Função para realizar a interpolação linear entre dois pontos dados.

    - x: lista com os valores para o eixo x;
    - y: lista com os valores para o eixo y;
    - x_new: lista com novos valores para o eixo x.
    """
    # Cálculo da reta
    a = (y[1] - y[0]) / (x[1] - x[0])
    b = y[0] - a * x[0]

    # Cálculo da cota no ponto x_new
    y_new = a * x_new + b

    return y_new


def calculate_cotas(
    x: list[float], y: list[float], spacing: float, option: str
) -> list[float]:
    """
    Função para calcular as cotas dos pontos intermediários.

    - x: lista com os valores para o eixo x;
    - y: lista com os valores para o eixo y;
    - spacing: espaçamento entre os pontos que se deseja calcular;
    - option: escolha das opções para o espaçamento entre os marcos - projeção em um plano horizontal
    ou acompanhando a topografia (option: horizontal ou topographic).
    """
    x_new = []
    y_new = []

    if option == "horizontal":
        # Cálculo das cotas dos pontos intermediários com projeção horizontal
        for i in range(1, len(x)):
            for j in range(int(spacing), int((x[i] - x[i - 1])), int(spacing)):
                x_new.append(x[i - 1] + j)
                y_new.append(
                    linear_interpolation(
                        x[i - 1 : i + 1], y[i - 1 : i + 1], x[i - 1] + j
                    )
                )
    else:
        # Cálculo das cotas dos pontos intermediários com projeção topográfica
        x_spacing = np.arange(x[0], x[-1] + spacing, spacing)
        y_spacing = np.interp(x_spacing, x, y)

        for i in range(1, len(x_spacing)):
            x_new.append(x_spacing[i])
            y_new.append(
                linear_interpolation(
                    x_spacing[i - 1 : i + 1], y_spacing[i - 1 : i + 1], x_spacing[i]
                )
            )

    return x_new, y_new


def gen_plot(x, y, x_new, y_new):
    """
    Função para calcular as cotas dos pontos intermediários.

    - x: lista com os valores para o eixo x;
    - y: lista com os valores para o eixo y;
    - x_new: lista com os novos valores para o eixo x;
    - y_new: lista com os novos valores para o eixo y.
    """

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle("Gráfico das cotas iniciais e intermediárias", fontsize=16)
    ax1.plot(x, y, "ko--")
    ax1.set_title("Cota dos pontos iniciais")
    ax1.set_xlabel("Distância (m)")
    ax1.set_ylabel("Valor da cota (m)")

    ax2.plot(x_new, y_new, "mo--")
    ax2.set_title("Cota dos pontos intermediários")
    ax2.set_xlabel("Distância (m)")
    ax2.set_ylabel("Valor da cota (m")

    ax1.grid()
    ax2.grid()
    fig.savefig("topographic2", dpi=500)


if __name__ == "__main__":
    datas = read_file("dados.txt")
    _, elevations, distances = get_values(datas)
    spacing = 20
    option = "topographic"
    # option = "horizontal"

    # Cálculo das cotas dos pontos intermediários
    x_new, y_new = calculate_cotas(distances, elevations, spacing, option)
    gen_plot(distances, elevations, x_new, y_new)
