def ler_matriz_txt(caminho):
    with open(caminho, 'r') as f:
        linhas = f.readlines()
    return [[float(num) for num in linha.strip().split()] for linha in linhas]

def imprimir_lista(nome, lista):
    print(f"{nome}: [" + ", ".join(f"{v:.6f}" for v in lista) + "]")
