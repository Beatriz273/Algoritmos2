#Faça um algoritmo que lê duas listas A e B com 5 elementos cada. Construir
#uma lista C, sendo este a junção das duas outras listas, ou seja, a lista C deverá
#conter 10 elementos. Mostre no final a lista C.

a = []
b = []
c = []
N = 5

for i in range(N): 
    a.append(int(input(f"\nL1 - valor indice [{i}]: ")))

for i in range(N): 
    b.append(int(input(f"\nL2 - valor indice [{i}]: ")))

for i in range(N):
    c.append(a[i])

for i in range(N):
    c.append(b[i])

for i in range(N*2): 
    print(f"Resultado: [{i}]:[{c[i]}]")