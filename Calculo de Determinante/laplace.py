import sys
sys.setrecursionlimit(10000)  # aumenta limite

# Função: Determinante por Laplace
def determinante_laplace(matriz):
    n = len(matriz)
    if n == 1:
        return matriz[0][0]
    if n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    det = 0
    for col in range(n):
        submatriz = []
        for linha in range(1, n):
            linha_sub = matriz[linha][:col] + matriz[linha][col+1:]
            submatriz.append(linha_sub)
        cofator = ((-1) ** col) * matriz[0][col]
        det += cofator * determinante_laplace(submatriz)
    return det
