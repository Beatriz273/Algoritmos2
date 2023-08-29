import numpy as np

# Definir o tamanho da array
N = 5

# preencher a estrutura com zeros
vetor = np.zeros(N)

for i in range (N) :   
    vetor[i] = int(input(f"Digite o valor da posição {i}: "))

for i in range (N) :  
    print(vetor[i])