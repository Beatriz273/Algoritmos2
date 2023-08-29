# Ler 2 vetores, R de 5 elementos e S de 10 elementos, ambos de inteiros. Gere
# um vetor X que possua os elementos comuns a R e a S. Considere que no
# mesmo vetor não haverá números repetidos.
import numpy as np

sMax = 3
rMax = 2
sVetor = []
rVetor = []
xVetor = []

for i in range(rMax):
    rVetor.append(int(input(f"Insira um valor para R:[{i}]: ")))

for i in range(sMax):
    sVetor.append(int(input(f"Insira um valor para S:[{i}]: ")))

for s in range(sMax):
    for r in range(rMax):
       if sVetor[s] == rVetor[r]:
           xVetor.append(rVetor[r])

print(f"Os valores iguais nos vetores são: {xVetor}")

