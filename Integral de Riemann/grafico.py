import matplotlib.pyplot as plt

# Me dá o gráfico
def plotar_grafico(funcao, a, b, n):#a: limite inferior da integral///b: limite superior da integral///n: número de subintervalos

    delta_x = (b - a) / n  #largura de cada subintervalo    
    x_vals = [a + i * (b - a) / 1000 for i in range(1001)] #Gera os pontos x da funcao
    y_vals = [funcao(x) for x in x_vals] #gera os pontos y da funcao

    fig, ax = plt.subplots() #cria figuras e eixos
    ax.plot(x_vals, y_vals, 'b', label='f(x)')#desenha a curva da funcao com a legenda f(x)

    # Gráfico pela esquerda
    for i in range(n):
        x = a + i * delta_x #x a esquerda do retangulo
        y = funcao(x) #altura
        ax.add_patch(plt.Rectangle((x, 0), delta_x, y, edgecolor='black', facecolor='orange', alpha=0.5)) #gera triangulo quase transparente que determina aprox a area

    #Adiciona título, legenda, rótulos dos eixos, e uma grade
    ax.set_title('Aproximação da Integral - Soma de Riemann (Esquerda)')
    ax.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()
