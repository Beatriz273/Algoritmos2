# Faça um programa que leia um vetor de 3 posições e uma matriz de 3 x
# 3 calcule e mostre o resultado da multiplicação do primeiro item do vetor, por toda a
# primeira coluna da matriz, do segundo item do vetor por toda a segunda coluna da
# matriz e assim sucessivamente e armazene os resultados linha a linha na matriz
# resultado.
import numpy as np

N = 2
V = []
M = np.zeros((N,N))
Mr = np.zeros((N,N))

for i in range(N):
    V.append(int(input(f"Insira um valor para o vetor: ")))
    for c in range(N):
        M[i][c] = int(input(f"Insira um valor para a linha ({i}) e a coluna ({c}): "))
print(f"""A primeira variação da nossa matriz é: 
{M}""")

soma = []

for i in range(N):
    for c in range(N):
        soma = M[i][c] * V[c]
        Mr[i][c] = soma
   
print(f"""Os valores inseridos para multiplicação são: {V}.
Após aplicar a multiplicação dos vetores sucessivamente na matriz, obtivemos tal resultado: 
{Mr}""")
        