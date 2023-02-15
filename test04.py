import numpy as np
import matplotlib.pyplot as plt

lista = list(range(20, 1000, 20))
print(lista)

# import pandas as pd

# Dados de entrada
x = np.array([0, 100, 200, 300, 400])
y = np.array([100, 150, 200, 250, 300])

# Espaçamento entre os pontos a serem calculados
spacing = 50

# Cálculo da elevação dos pontos intermediários
xi = np.arange(0, 400 + spacing, spacing)
yi = np.interp(xi, x, y)

# Saída dos resultados
print("Posições:", xi)
print("Elevações:", yi)

# Gráfico das cotas medidas e calculadas
plt.plot(x, y, "o", label="Medidas")
plt.plot(xi, yi, "-", label="Calculadas")
plt.legend()
plt.savefig("teste01.png", dpi=500)
plt.close("all")


# Criação do DataFrame com os resultados
# df = pd.DataFrame({'Posições': xi, 'Elevações': yi})

# Escrita dos resultados em um arquivo csv
# df.to_csv('resultados.csv', index=False)
