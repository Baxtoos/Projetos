import time
from potencia import iteracao_potencia_com_deflacao
from qr import iteracao_qr_sem_deslocamento, iteracao_qr_com_deslocamento

def erro_relativo(aprox, real):
    return abs(aprox - real) / abs(real)

def avaliar_metodo(nome, metodo, matriz, referencia, extrair_top=3):
    inicio = time.perf_counter()
    resultado = metodo(matriz)
    duracao = time.perf_counter() - inicio

    if isinstance(resultado[0], list):  # Power Iteration retorna (valores, vetores)
        autovalores = resultado[0]
    else:
        autovalores = sorted(resultado, key=abs, reverse=True)[:extrair_top]

    erros = [erro_relativo(autovalores[i], referencia[i]) for i in range(extrair_top)]
    erro_medio = sum(erros) / extrair_top

    print(f"{nome} -> Tempo: {duracao:.6f}s | Erros relativos: {erros} | Erro médio: {erro_medio:.6f}")
