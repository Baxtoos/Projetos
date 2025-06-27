from entrada import obter_funcao, obter_entradas
from calculo import soma_riemann, exibir_resultados
from grafico import plotar_grafico

# Define a função principal do programa para não dar erro
def main():
    funcao = obter_funcao()
    limite1, limite2, subintervalos = obter_entradas()

    soma = soma_riemann(funcao, limite1, limite2, subintervalos)

    exibir_resultados(soma)
    plotar_grafico(funcao, limite1, limite2, subintervalos)

if __name__ == "__main__":
    main()
