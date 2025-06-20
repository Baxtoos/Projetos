import random
import math

def norma_vetor(vetor):
    return math.sqrt(sum(x ** 2 for x in vetor))

def normalizar_vetor(vetor):
    n = norma_vetor(vetor)
    return [x / n for x in vetor]

def multiplicar_matriz_vetor(matriz, vetor):
    return [sum(matriz[i][j] * vetor[j] for j in range(len(vetor))) for i in range(len(matriz))]

def produto_escalar(vetor1, vetor2):
    return sum(x * y for x, y in zip(vetor1, vetor2))

def subtrair_matrizes(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def aplicar_deflacao(matriz, autovalor, autovetor):
    n = len(autovetor)
    return subtrair_matrizes(matriz, [
        [autovalor * autovetor[i] * autovetor[j] for j in range(n)]
        for i in range(n)
    ])

def iteracao_potencia(matriz, tol=1e-8, max_iter=1000):
    n = len(matriz)
    x = [random.random() for _ in range(n)]
    x = normalizar_vetor(x)
    autovalor_antigo = 0

    for _ in range(max_iter):
        y = multiplicar_matriz_vetor(matriz, x)
        x_novo = normalizar_vetor(y)
        autovalor = produto_escalar(x_novo, multiplicar_matriz_vetor(matriz, x_novo))

        if abs(autovalor - autovalor_antigo) < tol:
            return autovalor, x_novo
        x = x_novo
        autovalor_antigo = autovalor

    return autovalor, x

def iteracao_potencia_com_deflacao(matriz, k=3, tol=1e-8, max_iter=1000):
    autovalores = []
    autovetores = []
    matriz_atual = [linha[:] for linha in matriz]

    for _ in range(k):
        autovalor, autovetor = iteracao_potencia(matriz_atual, tol, max_iter)
        autovalores.append(autovalor)
        autovetores.append(autovetor)
        matriz_atual = aplicar_deflacao(matriz_atual, autovalor, autovetor)

    return autovalores, autovetores
