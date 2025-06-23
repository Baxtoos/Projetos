from entrada import obter_funcao, obter_entradas
from calculo import soma_riemann, exibir_resultados
from grafico import plotar_grafico

# Main separada para não dar erro
def main():
    funcao = obter_funcao() 
    limite1, limite2, subintervalos = obter_entradas()

    soma_esquerda = soma_riemann(funcao, limite1, limite2, subintervalos, 'esquerda')
    soma_direita  = soma_riemann(funcao, limite1, limite2, subintervalos, 'direita')
    soma_meio     = soma_riemann(funcao, limite1, limite2, subintervalos, 'meio')

    exibir_resultados(soma_esquerda, soma_direita, soma_meio)
    plotar_grafico(funcao, limite1, limite2, subintervalos)

if __name__ == "__main__":
    main()
    