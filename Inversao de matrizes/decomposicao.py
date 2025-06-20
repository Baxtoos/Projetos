def lu_decomposicao(matriz):
    n = len(matriz)
    L = [[0.0]*n for _ in range(n)]
    U = [[0.0]*n for _ in range(n)]

    for i in range(n):
        for k in range(i, n):
            soma = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = matriz[i][k] - soma
        for k in range(i, n):
            if i == k:
                L[k][i] = 1.0
            else:
                soma = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (matriz[k][i] - soma) / U[i][i]
    return L, U

def substituicao_adiantada(L, b):
    n = len(L)
    y = [0.0]*n
    for i in range(n):
        y[i] = b[i] - sum(L[i][j]*y[j] for j in range(i))
    return y

def substituicao_reversa(U, y):
    n = len(U)
    x = [0.0]*n
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(U[i][j]*x[j] for j in range(i+1, n))) / U[i][i]
    return x

def inversa_por_lu(matriz):
    n = len(matriz)
    L, U = lu_decomposicao(matriz)
    inversa = []
    for i in range(n):
        e = [0.0]*n
        e[i] = 1.0
        y = substituicao_adiantada(L, e)
        x = substituicao_reversa(U, y)
        inversa.append(x)
    return [list(col) for col in zip(*inversa)]  # transposta
