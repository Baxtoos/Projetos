import matplotlib.pyplot as plt

# Me dá o gráfico
def plotar_grafico(funcao, a, b, n):
    delta_x = (b - a) / n
    x_vals = [a + i * (b - a) / 1000 for i in range(1001)]
    y_vals = [funcao(x) for x in x_vals]

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, 'b', label='f(x)')

    # Gráfico pela esquerda
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
