from functions import *
import os.path

file = input("Digite o nome do arquivo: ")
file_exists = os.path.exists(f"datas/{file}")

while len(file) == 0 or file_exists == False:
    print("O nome do arquivo não existe, por favor, informe um arquivo .txt válido.")

    file = input("Digite o nome do arquivo: ")
    file_exists = os.path.exists(f"datas/{file}")

datas = read_file(f"datas/{file}")
_, elevations, distances = get_values(datas)

spacing = input("Digite o espaçamento das cotas a serem calculadas: ")

while not spacing.isnumeric():
    print("Por favor, informe um número.")
    spacing = input("Digite o espaçamento das cotas a serem calculadas: ")

spacing = float(spacing)

while spacing > 100:
    print(
        """
        O espaçamento que deseja-se calcular é maior que o espaçamento entre os pontos iniciais (100 m).\n
        Por favor, informe um valor menor ou igual a 100 m.
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

option = input("Digite:")

while not option.isnumeric() or len(option) == 0:
    print("Por favor, informe um número.")
    print("Digite\n 1 - Horizontal;\n 2 - Topografia.")
    option = input("Digite:")

if option == "1":
    # Cálculo das cotas dos pontos intermediários
    option = "horizontal"
    x_new, y_new = calculate_cotas(distances, elevations, spacing, option)
    gen_plot(distances, elevations, x_new, y_new)
    save_csv(x_new, y_new)

elif option == "2":
    # Cálculo das cotas dos pontos intermediários
    option = "topographic"
    x_new, y_new = calculate_cotas(distances, elevations, spacing, option)
    gen_plot(distances, elevations, x_new, y_new)
    save_csv(x_new, y_new)
