#Altere o algoritmo anterior para que ele realize o produto da primeira lista, pelo
#inverso da segunda lista.

l1 = []
l2 = []
l3 = []
N = 2

for i in range(N): 
    l1.append(int(input(f"\nL1 - valor indice [{i}]: ")))

for i in range(N): 
    l2.append(int(input(f"\nL2 - valor indice [{i}]: ")))

for i in range(N):
    j = N - 1 - i 
    x = l1[i] * l2[j]
    l3.append(x)

for i in range(N): 
    print(f"Resultado: [{i}]:[{l3[i]}]")