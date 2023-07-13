import os
from typing import Callable, Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


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

    try:
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

    except (ValueError, IndexError):
        return None, None, None


def linear_interpolation(
    x: list[float], y: list[float], x_new: list[float]
) -> list[float]:
    """
    Função para realizar a interpolação linear entre dois pontos dados.

    - x: lista com os valores para o eixo x;
    - y: lista com os valores para o eixo y;
    - x_new: lista com novos valores para o eixo x.
    retorna os novos valores para y.
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
    ou acompanhando a topografia (option: horizontal ou topographic);
    retorna os valores das cotas dos pontos intermediários.
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
                    x_spacing[i - 1 : i + 1],
                    y_spacing[i - 1 : i + 1],
                    x_spacing[i],
                )
            )

    return x_new, y_new


def gen_plot(
    x: list[float],
    y: list[float],
    x_new: list[float],
    y_new: list[float],
    path_folder: str,
    figure_name: str,
) -> None:
    """
    Função para plotar e salvar os valores das cotas iniciais e intermediárias.

    - x: lista com os valores iniciais para o eixo x;
    - y: lista com os valores iniciais para o eixo y;
    - x_new: lista com os novos valores para o eixo x;
    - y_new: lista com os novos valores para o eixo y;
    - figure_name: nome da figura.
    """

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("Gráfico das cotas iniciais e intermediárias", fontsize=16)
    ax1.plot(x, y, "ko--")
    ax1.set_title("Cota dos pontos iniciais")
    ax1.set_xlabel("Distância (m)")
    ax1.set_ylabel("Valor da cota (m)")

    ax2.plot(x_new, y_new, "mo--")
    ax2.set_title("Cota dos pontos intermediários")
    ax2.set_xlabel("Distância (m)")
    ax2.set_ylabel("Valor da cota (m)")

    ax1.grid()
    ax2.grid()
    os.makedirs(f"{path_folder}/figures/", exist_ok=True)
    fig.savefig(f"{path_folder}/figures/{figure_name}.png", dpi=500)


def save_csv(
    x_new: list[float],
    y_new: list[float],
    path_folder: str,
    table_name: str,
) -> None:
    """
    Função para salvar as novas posições e cotas calculadas.

    - x_new: lista com os novos valores para o eixo x;
    - y_new: lista com os novos valores para o eixo y;
    - table_name: nome da tabela.
    """

    # Criação do DataFrame com os resultados
    df = pd.DataFrame(
        {"NOVA DISTÂNCIA (m)": x_new, "COTA INTERMEDIÁRIA (m)": y_new}
    )

    # Escrita dos resultados em um arquivo csv
    os.makedirs(f"{path_folder}/tables/", exist_ok=True)
    df.to_csv(f"{path_folder}/tables/{table_name}.csv", index=False, sep=";")


def gen_intermediate_cotas(
    file_name_txt: str,
    path_folder: str,
    spacing_cotas_in: float,
    option_in: str,
    on_success: Optional[Callable] = None,
    on_error: Optional[Callable] = None,
) -> None:
    """
    Função para gerar o resultado das cotas intermediárias.

    - file_name_txt: entrar com o arquivo .txt;
    - path_folder: path da pasta onde os arquivos gerados serão salvos;
    - spacing_cotas_in: espaçamento entre os pontos que se deseja calcular.
    - option_in: escolher se a projeção é no plano horizontal ou acompanhando a topografia.
    - on_success: popup informando o status do processo.
    - on_error: popup informando o status do processo.
    """

    datas = read_file(file_name_txt)

    if len(datas) == 0:
        on_error("Arquivo .txt vazio. Verifique!")
        return

    _, elevations, distances = get_values(datas)

    if elevations is None or distances is None:
        on_error(
            "Conteúdo do arquivo .txt inválido. Verifique o conteúdo do"
            " arquivo!"
        )
        return

    spacing_between_starting_points = float(distances[1] - distances[0])

    spacing_cotas = float(spacing_cotas_in)

    if spacing_cotas >= spacing_between_starting_points:
        on_error(
            "O espaçamento que deseja-se calcular é maior que o espaçamento"
            " entre os pontos iniciais"
            f" ({spacing_between_starting_points} m)\n informado na coluna"
            " DISTÂNCIA no conteúdo do arquivo .txt de entrada."
        )
        return

    option_projection = option_in.lower()

    if option_projection == "horizontal":
        """
        Cálculo das cotas dos pontos intermediários para a projeção no plano horizontal.
        """
        option_horizontal = "horizontal"
        x_new, y_new = calculate_cotas(
            distances, elevations, spacing_cotas, option_horizontal
        )
        gen_plot(
            x=distances,
            y=elevations,
            x_new=x_new,
            y_new=y_new,
            path_folder=path_folder,
            figure_name=f"horizontal_plane_with_spacing_{spacing_cotas}_m",
        )
        save_csv(
            x_new=x_new,
            y_new=y_new,
            path_folder=path_folder,
            table_name=f"horizontal_plane_with_spacing__{spacing_cotas}_m",
        )

    elif option_projection == "topografia":
        """
        Cálculo das cotas dos pontos intermediários acompanhando a topografia.
        """

        option_topographic = "topographic"
        x_new, y_new = calculate_cotas(
            distances, elevations, spacing_cotas, option_topographic
        )
        gen_plot(
            x=distances,
            y=elevations,
            x_new=x_new,
            y_new=y_new,
            path_folder=path_folder,
            figure_name=(
                f"following_the_topography_with_spacing_{spacing_cotas}_m"
            ),
        )
        save_csv(
            x_new=x_new,
            y_new=y_new,
            path_folder=path_folder,
            table_name=(
                f"following_the_topography_with_spacing__{spacing_cotas}_m"
            ),
        )

    if on_success is not None:
        on_success()


if __name__ == "__main__":
    gen_intermediate_cotas("../../datas/dados.txt")
