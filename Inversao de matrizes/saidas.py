import time
from gauss import gauss_jordan_inversa
from decomposicao import inversa_por_lu
from utilidade import gerar_matriz, copiar_matriz

def testar_metodos(tamanhos):
    for n in tamanhos:
        matriz = gerar_matriz(n)
        
        # Gauss-Jordan
        A1 = copiar_matriz(matriz)
        inicio = time.perf_counter()
        gauss_jordan_inversa(A1)
        tempo_gj = time.perf_counter() - inicio

        # LU
        A2 = copiar_matriz(matriz)
        inicio = time.perf_counter()
        inversa_por_lu(A2)
        tempo_lu = time.perf_counter() - inicio

        print(f"Matriz {n}x{n}: Gauss-Jordan = {tempo_gj:.6f}s | LU = {tempo_lu:.6f}s")
