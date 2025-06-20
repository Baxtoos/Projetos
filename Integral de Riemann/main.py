import matplotlib.pyplot as plt

"""
Programa para calcular a aproximação da integral definida de uma função usando somas de Riemann.
Métodos implementados: Soma pela esquerda, direita e pelo ponto médio.
Também plota o gráfico da função e dos retângulos de Riemann.
"""

#Pega a funcao do usuario
def obter_funcao():
    entrada = input("Digite a função em x (ex: x**2, 2*x + 1, (x**2) + 3*x - 1): ")
    def funcao(x):
        return eval(entrada)
    return funcao

#pega e retorna as entradas
def obter_entradas():
    limite1 = float(input('Limite inferior: '))
    limite2 = float(input('Limite superior: '))
    subintervalos = int(input('Número de subintervalos: '))
    return limite1, limite2, subintervalos

#faz as somas de riemann (esquerda, meio e direita)
def soma_riemann(funcao, a, b, n, metodo='esquerda'):
    delta_x = (b - a) / n
    soma = 0
    for i in range(n):
        if metodo == 'esquerda':
            x = a + i * delta_x
        elif metodo == 'direita':
            x = a + (i + 1) * delta_x
        elif metodo == 'meio':
            x = a + (i + 0.5) * delta_x
        soma += funcao(x) * delta_x
    return soma

#printa resultados
def exibir_resultados(esq, dir, meio):
    print('\nResultados aproximados:')
    print('Soma pela esquerda: {:.6f}'.format(esq))
    print('Soma pela direita:  {:.6f}'.format(dir))
    print('Soma pelo meio:     {:.6f}'.format(meio))

#me da o grafico
def plotar_grafico(funcao, a, b, n):
    delta_x = (b - a) / n
    x_vals = [a + i * (b - a) / 1000 for i in range(1001)]
    y_vals = [funcao(x) for x in x_vals]

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, 'b', label='f(x)')

    #grafico pela esquerda
    for i in range(n):
        x = a + i * delta_x
        y = funcao(x)
        ax.add_patch(plt.Rectangle((x, 0), delta_x, y, edgecolor='black', facecolor='orange', alpha=0.5))

    ax.set_title('Aproximação da Integral - Soma de Riemann (Esquerda)')
    ax.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()

#main separada para nao dar erro
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
