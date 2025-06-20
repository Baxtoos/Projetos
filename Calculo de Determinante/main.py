from utilidades import testar_tempos, gerar_grafico

def main():
    tamanhos = [3, 5, 8, 20, 100]
    tempos_laplace, tempos_gauss = testar_tempos(tamanhos)
    gerar_grafico(tamanhos, tempos_laplace, tempos_gauss)

if __name__ == "__main__":
    main()
