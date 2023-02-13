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


def calculate_angles(elevations: list, horizontal_distance: int = 100):
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


if __name__ == "__main__":
    datas = read_file("dados.txt")
    id, elevations, distances = get_values(datas)
    angles = calculate_angles(elevations)
    print(angles)
    # print(elevations)
