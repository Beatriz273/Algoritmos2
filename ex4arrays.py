# Ler um vetor R de 5 elementos, inteiros, contendo o resultado da LOTO. A seguir ler
# um vetor A de 10 elementos inteiros contendo uma aposta. A seguir imprima quantos
# pontos fez o apostador
import random 

rMax = 5
aMax = 10

loto = []
aposta = []
cont = 0

for i in range(rMax):
    loto.append(random.randint(1,50))

for i in range(aMax):
    aposta.append(int(input(f"Insira um valor para apostar na loteria [{i}]: ")))

for a in range(aMax):
    for r in range(rMax):
        if aposta[a] == loto[r]:
            cont += 1

if cont == 5:
    print('\nVocê ganhou a loteria!')
elif cont == 0:
    print("\nVocê não acertou nenhum número!")
else:
    print(f"\nVocê acertou {cont} pontos!")

print(f"\nOs números da loteria eram: {loto}")



