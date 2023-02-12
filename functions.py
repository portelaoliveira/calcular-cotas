import matplotlib.pyplot as plt
import math


def read_file(filename: str) -> list:
    """
    Função para ler arquivos .txt

    - filename: arquivo de entrada do tipo string;
    - retorna uma lista.
    """

    file = open(filename, "r")
    datas = file.readlines()

    return datas


def get_values(datas: list) -> list:
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


if __name__ == "__main__":
    datas = read_file("dados.txt")
    id, elevations, distances = get_values(datas)
    print(id)
