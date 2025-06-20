def gauss_jordan_inversa(matriz):
    n = len(matriz)
    identidade = [[float(i == j) for i in range(n)] for j in range(n)]
    for i in range(n):
        #pivo != 0
        if matriz[i][i] == 0:
            for j in range(i+1, n):
                if matriz[j][i] != 0:
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    identidade[i], identidade[j] = identidade[j], identidade[i]
                    break
        # Normaliza i do pivo
        pivo = matriz[i][i]
        for j in range(n):
            matriz[i][j] /= pivo
            identidade[i][j] /= pivo
        # Zera outras linhas
        for k in range(n):
            if k != i:
                fator = matriz[k][i]
                for j in range(n):
                    matriz[k][j] -= fator * matriz[i][j]
                    identidade[k][j] -= fator * identidade[i][j]
    return identidade
