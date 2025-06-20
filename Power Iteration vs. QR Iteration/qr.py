import math

def matriz_identidade(n):
    return [[float(i == j) for j in range(n)] for i in range(n)]

def transposta(matriz):
    return [list(linha) for linha in zip(*matriz)]

def multiplicar_matrizes(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def norma(vetor):
    return math.sqrt(sum(x ** 2 for x in vetor))

def refletor_householder(vetor):
    n = len(vetor)
    v = vetor[:]
    sinal = -1 if vetor[0] < 0 else 1
    v[0] += sinal * norma(vetor)
    norma_v = norma(v)
    return [vi / norma_v for vi in v]

def decomposicao_qr(matriz):
    n = len(matriz)
    Q = matriz_identidade(n)
    R = [linha[:] for linha in matriz]

    for k in range(n - 1):
        x = [R[i][k] for i in range(k, n)]
        v = refletor_householder(x)
        H = matriz_identidade(n)
        for i in range(k, n):
            for j in range(k, n):
                H[i][j] -= 2 * v[i - k] * v[j - k]

        R = multiplicar_matrizes(H, R)
        Q = multiplicar_matrizes(Q, transposta(H))

    return Q, R

def maximo_abaixo_diagonal(matriz):
    n = len(matriz)
    return max(abs(matriz[i][j]) for i in range(n) for j in range(i))

def iteracao_qr_sem_deslocamento(matriz, tol=1e-10, max_iter=1000):
    n = len(matriz)
    A = [linha[:] for linha in matriz]

    for _ in range(max_iter):
        Q, R = decomposicao_qr(A)
        A = multiplicar_matrizes(R, Q)
        if maximo_abaixo_diagonal(A) < tol:
            break

    return [A[i][i] for i in range(n)]

def iteracao_qr_com_deslocamento(matriz, tol=1e-10, max_iter=1000):
    n = len(matriz)
    A = [linha[:] for linha in matriz]

    for _ in range(max_iter):
        deslocamento = A[n-1][n-1]
        B = [[A[i][j] - (deslocamento if i == j else 0) for j in range(n)] for i in range(n)]
        Q, R = decomposicao_qr(B)
        A = multiplicar_matrizes(R, Q)
        for i in range(n):
            A[i][i] += deslocamento
        if maximo_abaixo_diagonal(A) < tol:
            break

    return [A[i][i] for i in range(n)]
