# Faça um algoritmo que armazene 25 valores em uma variável (array,
# lista, tupla ou conjunto). O algoritmo deverá armazenar em uma nova variável os
# valores na ordem inversa e com o sinal inverso. Exemplo:

var = []
n = 5
valor = []

for i in range(n):
    valor = float(input("Insira um valor: "))
    valor = valor * (-1)
    var.append(valor)
    if i >= (n-1):
        var.reverse()

print(var)