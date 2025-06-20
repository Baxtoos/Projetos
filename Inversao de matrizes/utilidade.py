import random

def gerar_matriz(n):
    return [[float(random.randint(1, 10)) for _ in range(n)] for _ in range(n)]

def copiar_matriz(matriz):
    return [linha[:] for linha in matriz]

def imprimir_matriz(matriz):
    for linha in matriz:
        print("  ".join(f"{num:8.4f}" for num in linha))
    print()
