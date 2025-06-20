import time
import random
import sys
import matplotlib.pyplot as plt  # grafico

sys.setrecursionlimit(10000)  # aumenta limite

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

def determinante_gauss(matriz):
    n = len(matriz)
    det = 1
    for i in range(n):
        if matriz[i][i] == 0:  # se for 0 troca de linha
            trocou = False
            for j in range(i+1, n):
                if matriz[j][i] != 0:
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    det *= -1  # troca de linha inverte sinal
                    trocou = True
                    break
            if not trocou:
                return 0  # det = 0

        # Eliminação
        for j in range(i+1, n):
            fator = matriz[j][i] / matriz[i][i]
            for k in range(i, n):
                matriz[j][k] -= fator * matriz[i][k]

    # Produto da diagonal principal
    for i in range(n):
        det *= matriz[i][i]
    return det

# valores aleatórios
def gerar_matriz(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

# tempos
tamanhos = [3, 5, 8, 20, 100]
tempos_laplace = []  # lista para armazenar os tempos do Laplace
tempos_gauss = []    # lista para armazenar os tempos do Gauss

print("\n===== Testes de Tempo =====\n")

for n in tamanhos:
    matriz = gerar_matriz(n)

    print(f"\nMatriz {n}x{n}:")

    # Teste Laplace (máximo 8x8)
    if n <= 8:
        inicio = time.perf_counter()
        det_laplace = determinante_laplace(matriz)
        fim = time.perf_counter()
        tempo_laplace = fim - inicio
        tempos_laplace.append(tempo_laplace)
        print(f"Laplace: Determinante = {det_laplace} | Tempo: {tempo_laplace:.4f} segundos")
    else:
        tempos_laplace.append(None)  # para manter o alinhamento das listas

    # Teste Gauss (máximo 100x100)
    matriz_copia = [linha.copy() for linha in matriz]  # copy matriz
    inicio = time.perf_counter()
    det_gauss = determinante_gauss(matriz_copia)
    fim = time.perf_counter()
    tempo_gauss = fim - inicio
    tempos_gauss.append(tempo_gauss)
    print(f"Gauss: Determinante = {det_gauss} | Tempo: {tempo_gauss:.4f} segundos")

# Gera gráfico
plt.figure(figsize=(10, 6))
x_labels = [str(t) for t in tamanhos]

# Plota gráfico Laplace (até 8x8)
laplace_plot = [t if t is not None else 0 for t in tempos_laplace]
plt.plot(x_labels, laplace_plot, marker='o', color='blue', label='Expansão de Laplace (Recursivo)')

# Plota gráfico Gauss
plt.plot(x_labels, tempos_gauss, marker='o', color='green', label='Eliminação de Gauss')

plt.title('Comparação de Tempo de Execução: Laplace vs Gauss')
plt.xlabel('Tamanho da Matriz (n x n)')
plt.ylabel('Tempo (segundos)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
