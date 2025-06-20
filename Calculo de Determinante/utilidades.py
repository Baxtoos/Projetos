import time
import random
import matplotlib.pyplot as plt  # grafico
from laplace import determinante_laplace
from gauss import determinante_gauss

# valores aleatórios
def gerar_matriz(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

# Teste de tempo
def testar_tempos(tamanhos):
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

    return tempos_laplace, tempos_gauss

# Gera gráfico
def gerar_grafico(tamanhos, tempos_laplace, tempos_gauss):
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
