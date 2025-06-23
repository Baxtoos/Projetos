def soma_riemann(funcao, a, b, n, metodo='esquerda'): #faz todas as somas (esquerda, meio e direita)
    delta_x = (b - a) / n #calcula o tamanho de cada subintervalo
    soma = 0 #inicializa varialvel que vai ir somando a area dos retangulos 
    for i in range(n):
        if metodo == 'esquerda':##pontos de avaliacao da funcao
            x = a + i * delta_x
        elif metodo == 'direita':
            x = a + (i + 1) * delta_x
        elif metodo == 'meio':
            x = a + (i + 0.5) * delta_x
        soma += funcao(x) * delta_x #calcula area dos retangulos
    return soma #acumula e retorna soma que é uma aprox da integral     

# Printa resultados
def exibir_resultados(esq, dir, meio):
    print('\nResultados aproximados:')
    print('Soma pela esquerda: {:.6f}'.format(esq))
    print('Soma pela direita:  {:.6f}'.format(dir))
    print('Soma pelo meio:     {:.6f}'.format(meio))
