# Elabore um algoritmo que leia duas listas de 5 posições, após a leitura realizar a
# soma e imprima o resultado da soma entre as duas listas de inteiros

l1 = []
l2 = []
l3 = []

N = 2

for i in range(N):
    l1.append(int(input(f"Insira um valor para a lista um no indice ({i}): ")))
    l2.append(int(input(f"Insira um valor para a lista dois no indice ({i}): ")))
    l3.append(l1[i]+l2[i])

print (l1)
print (l2)
print (l3)
