# Faça um programa que preencha um vetor com 9 números inteiros, calcule e
# mostre os que são números primos e suas respectivas posições

N = 9
v = []

for i in range(N):
    v.append(int(input("Insira uma idade para a posição [{i}]: ")))

for i in range(N):
    cont = 0
    for x in range (2,v[i]):
        if (v[i] % x == 0):
            cont+= 1
    if cont == 0:
        print(f"Os valores primos estão no indice [{i}] - número: [{v[i]}]")
