import numpy as np

# Definir la matriz A de coeficientes
A = np.array([
    [2, 3, -1, 4, -2, 5, -3, 1],
    [-3, 2, 4, -1, 3, -2, 5, -1],
    [4, -1, 3, 2, -3, 1, -2, 5],
    [-1, 5, -2, 3, 4, -1, 2, -3],
    [3, -2, 5, -1, 4, 2, -3, 1],
    [-2, 4, -3, 1, 5, -1, 2, -4],
    [5, -1, 2, -3, 4, 1, -2, 3],
    [1, -3, 4, -2, 5, -1, 2, -1]
])

b = np.array([10, -5, 8, 4, -7, 6, -3, 9])

x = np.linalg.solve(A, b)

# Mostrar los resultados
print("Las soluciones para las cada x^ son:")
for i in range(len(x)):
    print(f"x{i+1} = {x[i]}")
