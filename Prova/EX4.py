# Faça um algoritmo que preencha uma matriz 6 x 6 com números
# inteiros, execute as trocas especificadas a seguir e mostre a matriz resultante:
# ● A linha de índice 1 com a linha de índice 4;
# ● A coluna de índice 3 com a coluna de índice 5;
import numpy as np

N = 6
matriz = np.zeros((N,N))

for i in range(N):
    for c in range(N):
        matriz[i][c] = int(input(f"Insira um valor para a linha ({i}) e a coluna ({c}): "))

print(f"A primeira matriz gerada foi: {matriz}")

aux = 0

aux = matriz[1]
matriz[1] = matriz[4]
matriz[4] = aux

print(f"Ao trocarmos as linhas 1 e 4 a segunda matriz gerada foi: {matriz}")

for i in range(N):  
    matriz[i][3], matriz[i][5] = matriz[i][5], matriz[i][3]

print(f"Ao trocarmos a coluna 3 e 5 a terceira matriz gerada foi: {matriz}")
