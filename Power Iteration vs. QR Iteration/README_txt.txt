# Matrizes de Teste em Formato TXT

Este diretório contém as matrizes de teste prontas em formato texto, além deste README.

## Arquivos de Matrizes Densas (formato mat_n.txt)

- mat_3.txt         : Matriz quase-diagonal simétrica de dimensão 3×3.
- mat_10.txt        : Matriz quase-diagonal simétrica de dimensão 10×10.
- mat_100.txt       : Matriz quase-diagonal simétrica de dimensão 100×100.
- mat_300.txt       : Matriz quase-diagonal simétrica de dimensão 300×300.
- mat_500.txt       : Matriz quase-diagonal simétrica de dimensão 500×500.

Cada arquivo `mat_n.txt` possui `n` linhas e `n` colunas, onde cada linha contém `n` valores reais em notação científica, separados por espaços.

## Arquivo de Matriz Esparsa (formato sparse_mat_2500.txt)

- sparse_mat_2500.txt: Matriz esparsa de dimensão 2500×2500 em formato coordenado.

O formato de `sparse_mat_2500.txt` é:
  1. Primeira linha: `n_rows n_cols nnz`
  2. Cada linha subsequente: `i j value`, onde `i` e `j` são índices de linha e coluna (0-based) de um elemento não-nulo, e `value` é o valor correspondente em notação científica.

## Como Carregar em Python

Para matrizes densas:
```python
import numpy as np

A3 = np.loadtxt("mat_3.txt")      # Carrega matriz 3×3
A10 = np.loadtxt("mat_10.txt")    # Carrega matriz 10×10
# E assim por diante...
```

Para a matriz esparsa:
```python
import scipy.sparse as sp

# Ler o cabeçalho
with open("sparse_mat_2500.txt", "r") as f:
    n_rows, n_cols, nnz = map(int, f.readline().split())

rows = []
cols = []
data = []
for _ in range(nnz):
    i, j, v = f.readline().split()
    rows.append(int(i))
    cols.append(int(j))
    data.append(float(v))

A_sparse = sp.coo_matrix((data, (rows, cols)), shape=(n_rows, n_cols)).tocsr()
```

A matriz carregada `A_sparse` será do tipo `scipy.sparse.csr_matrix`.

## Observações

- Os valores estão em notação científica com 6 casas decimais (`%.6e`).
- Para matrizes densas, recomenda-se ter memória suficiente, especialmente para `mat_500.txt` (500×500).
- O arquivo de matriz esparsa `sparse_mat_2500.txt` descreve somente os elementos não-nulos, economizando espaço em disco e memória.

