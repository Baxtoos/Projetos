def obter_funcao(): #pega função do usuario
    entrada = input("Digite a função em x (ex: x**2, 2*x + 1, (x**2) + 3*x - 1): ")
    def funcao(x):
        return eval(entrada)
    return funcao

def obter_entradas(): #retorno das entradas
    limite1 = float(input('Limite inferior: '))
    limite2 = float(input('Limite superior: '))
    subintervalos = int(input('Número de subintervalos: '))
    return limite1, limite2, subintervalos
