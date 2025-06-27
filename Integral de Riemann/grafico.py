import matplotlib.pyplot as plt

# Me dá o gráfico
def plotar_grafico(funcao, a, b, n): #Define uma função chamada plotar_grafico com 4 parâmetros --- funcao ->função a ser desenhada --- a,b -> intervalos da integral --- n -> números de subintervalos
    delta_x = (b - a) / n ## fórmula para tamanho de cada subintervalo
    x_vals = [a + i * (b - a) / 1000 for i in range(1001)] #valor da função
    y_vals = [funcao(x) for x in x_vals] #Aplica a função funcao(x) para cada valor de x da lista anterior (calculo.py)

    fig, ax = plt.subplots() # Cria uma figura (fig) e um eixo (ax) onde os gráficos serão desenhados.
    ax.plot(x_vals, y_vals, 'b', label='f(x)') #Desenha a curva azul ('b') da função f(x) no gráfico e adiciona um rótulo para legenda 

    # Gráfico pela esquerda
    for i in range(n): #Inicia um laço para desenhar os retângulos da soma de Riemann.
        x = a + i * delta_x #ponto da esquerda de cada subintervalo
        y = funcao(x) #Calcula a altura do retângulo (valor da função naquele ponto).
        ax.add_patch(plt.Rectangle((x, 0), delta_x, y, edgecolor='black', facecolor='orange', alpha=0.5))#Desenha um retângulo no gráfico

    # Template gráfico
    ax.set_title('Aproximação da Integral - Soma de Riemann')
    ax.legend()
    plt.xlabel('x') #Adiciona o rótulo do eixo x.
    plt.ylabel('f(x)') #Adiciona o rótulo do eixo y.
    plt.grid(True) # Adiciona uma grade de fundo ao gráfico.
    plt.show() #Exibe
