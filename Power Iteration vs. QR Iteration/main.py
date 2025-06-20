from utils_matriz import ler_matriz_txt, imprimir_lista
from avaliacao import avaliar_metodo
from potencia import iteracao_potencia_com_deflacao
from qr import iteracao_qr_sem_deslocamento, iteracao_qr_com_deslocamento

caminho = "testes/matriz_exemplo.txt"
matriz = ler_matriz_txt(caminho)
referencia = [10.0, 5.0, 2.0]

avaliar_metodo("Iteração da Potência + Deflação", lambda A: iteracao_potencia_com_deflacao(A, 3), matriz, referencia)
avaliar_metodo("QR sem deslocamento", iteracao_qr_sem_deslocamento, matriz, referencia)
avaliar_metodo("QR com deslocamento", iteracao_qr_com_deslocamento, matriz, referencia)
