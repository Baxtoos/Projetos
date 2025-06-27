def obter_funcao():  # Pega função do usuário
    entrada = input("Digite a função em x (ex: x**2, 2*x + 1): ")  # Recebe do usuário uma expressão matemática em x (string)

    def funcao(x):  # Cria uma função funcao(x) que avalia a expressão digitada usando eval com segurança
        try:
            return eval(entrada, {"x": x, "__builtins__": {}})  # Eval limitado: só permite uso da variável x
        except Exception as e:
            print("Erro ao avaliar a função:", e)
            return 0  # Retorna 0 em caso de erro

    return funcao  # Retorna a função criada para ser usada nos cálculos

def obter_entradas():  # Retorna os valores fornecidos pelo usuário
    limite1 = float(input('Limite inferior: '))
    limite2 = float(input('Limite superior: '))
    subintervalos = int(input('Número de subintervalos: '))
    return limite1, limite2, subintervalos
