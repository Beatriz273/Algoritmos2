# Faça um algoritmo com 100 valores armazenados em uma variável x
# (array, lista, tupla ou conjunto). Calcular e mostrar no final:
# ● a quantidade de valores pares armazenados em x.
# ● e a média dos valores impares armazenados em x.

var = []
N = 5
valor = []
par = 0
impar = []

for i in range(N):
    valor.append(int(input("Insira um valor inteiro: ")))
    if valor[i] % 2 == 0:
        par += 1
    else:
        impar.append(valor[i])

print(impar)

somar = 0
for i in impar:
    somar += i

print(f"Os números somados ímpares são: {somar} e a quantia é: {len(impar)}")

somar = somar/len(impar)
    
print (f"A quantidade de números existentes pares são: {par}")
print (f"A média de números ímpares existentes nessa lista são: {somar:.2f}")

