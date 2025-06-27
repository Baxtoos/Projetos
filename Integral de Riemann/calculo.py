def soma_riemann(funcao, a, b, n):  # Soma de Riemann pela esquerda
    delta_x = (b - a) / n #Tamanho de cada subintervalo
    soma = 0 #Acumula valor da area total
    for i in range(n): #vai de 0 a n repetições
        x = a + i * delta_x  # ponto da esquerda de cada subintervalo
        soma += funcao(x) * delta_x #calcula a área do retângulo 
    return soma #retorna o valor total da área

def exibir_resultados(soma): #mostrar o resultado da soma calculada.
    print('\nResultados aproximados:')
    print('Soma: {:.6f}'.format(soma)) #Mostra o valor da soma com 6 casas decimais.
