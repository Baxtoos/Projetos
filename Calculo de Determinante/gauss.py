# Função: Determinante por Gauss
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
