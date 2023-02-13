import numpy as np
import matplotlib.pyplot as plt


def linear_interpolation(x, y, x_new):
    """Função para realizar a interpolação linear entre dois pontos dados."""
    # Cálculo da reta
    a = (y[1] - y[0]) / (x[1] - x[0])
    b = y[0] - a * x[0]

    # Cálculo da cota no ponto x_new
    y_new = a * x_new + b

    return y_new


def calculate_cotas(x, y, spacing, option):
    """Função para calcular as cotas dos pontos intermediários."""
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


# Dados de entrada
x = [0, 100, 200, 300, 400]
y = [0, 10, 20, 30, 40]
spacing = 50
option = "topografica"

# Cálculo das cotas dos pontos intermediários
x_new, y_new = calculate_cotas(x, y, spacing, option)

# Saída em forma de tabela
print("Posição (m)\tCota (m)")
for i in range(len(x_new)):
    print("{}\t\t{}".format(x_new[i], y_new[i]))

# Gráfico das cotas medidas e calculadas
# plt.figure(1)
# plt.plot(x, y, "ro", label="Medidas")
# # plt.plot(x_new, y_new, "ro", label="pontos intermediários")
# plt.show()

plt.figure(1)
plt.subplot(1, 1, 1)
plt.plot(x, y, "ko-")
plt.xlabel("Distância (m)")
plt.ylabel("Valor de cota (m)")
plt.show()
