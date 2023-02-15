from functions import *
import os.path
from time import sleep

resposta = "2"
while resposta == "2":
    file = input("Digite o nome do arquivo: ")
    file_exists = os.path.exists(f"datas/{file}")

    while len(file) == 0 or file_exists == False:
        print(
            "O nome do arquivo não existe, por favor, informe um arquivo .txt válido."
        )

        file = input("Digite o nome do arquivo: ")
        file_exists = os.path.exists(f"datas/{file}")

    datas = read_file(f"datas/{file}")
    _, elevations, distances = get_values(datas)

    spacing = input("Digite o espaçamento das cotas a serem calculadas: ")

    while not spacing.isnumeric():
        print("Por favor, informe um número.")
        spacing = input("Digite o espaçamento das cotas a serem calculadas: ")

    spacing = float(spacing)

    while spacing >= 100:
        print(
            """
            O espaçamento que deseja-se calcular é maior que o espaçamento entre os pontos iniciais (100 m).\n
            Por favor, informe um valor menor que 100 m.
            """
        )
        spacing = float(input("Digite o espaçamento das cotas a serem calculadas: "))

    print(
        """ 
        Opções para que o espaçamento entre os marcos seja uma projeção em um plano
        horizontal ou para que acompanhe a topografia\n 
        1 - Horizontal;
        2 - Topografia.
    """
    )

    option = input("Digite um número, por favor:")

    while (
        not option.isnumeric()
        or len(option) == 0
        or int(option) > 2
        or int(option) <= 0
    ):
        print("Por favor, informe um número válido.")
        print("Digite\n 1 - Horizontal;\n 2 - Topografia.")
        option = input("Digite um número, por favor:")

    if option == "1":
        # Cálculo das cotas dos pontos intermediários para a projeção no plano horizontal
        print("Calculando...\n")
        option = "horizontal"
        x_new, y_new = calculate_cotas(distances, elevations, spacing, option)
        gen_plot(
            distances,
            elevations,
            x_new,
            y_new,
            f"horizontal_plane_with_spacing_{spacing}_m",
        )
        save_csv(
            x_new,
            y_new,
            f"horizontal_plane_with_spacing__{spacing}_m",
        )
        sleep(1)

    elif option == "2":
        # Cálculo das cotas dos pontos intermediários acompanhando a topografia
        print("Calculando...\n")
        option = "topographic"
        x_new, y_new = calculate_cotas(distances, elevations, spacing, option)
        gen_plot(
            distances,
            elevations,
            x_new,
            y_new,
            f"following_the_topography_with_spacing_{spacing}_m",
        )
        save_csv(
            x_new,
            y_new,
            f"following_the_topography_with_spacing__{spacing}_m",
        )
        sleep(1)

    print("Processo finalizado com sucesso.\n")

    print(
        """
        Deseja fechar o programa?\n
        1 - Sim
        2 - Não
    """
    )

    resposta = input("Digite um número, por favor:")

    while (
        not resposta.isnumeric()
        or len(resposta) == 0
        or int(resposta) > 2
        or int(resposta) <= 0
    ):
        print("Por favor, informe um número.")
        resposta = input("Digite um número, por favor:")


sleep(1)
print("\n")
print("Programa encerrado.")
