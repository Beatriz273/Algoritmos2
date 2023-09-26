# Faça um algoritmo que preencha um variável (array, lista, tupla ou
# conjunto) com 8 números inteiros, calcule e mostre as duas variáveis (array, lista,
# tupla ou conjunto) resultantes. A primeira variável deve conter os números positivos
# e o segundo, os números negativos informados pelo usuário. Cada variável de
# resultado terá, no máximo, oito posições, que poderão ou não ser utilizadas. No caso
# do valor 0, este não deverá ser incluído nas variáveis de resultado.

Var1 = []
Var2 = []
N = 2
i = 1


while i <= N:
    linha = int(input("Insira um valor inteiro: "))
    i += 1
    if linha == 0:
        print("Insira um valor diferente de zero!")
        i -= 1
    else:
        Var1.append(linha)

i = 1

while i <= N:
    linha = float(input("Insira um valor negativo: "))
    i += 1
    if linha >= 1:
        print("Insira um valor negativo!")
        i -= 1
    else:
        Var2.append(linha)

print(f"A primeira variável é: {Var1}")
print(f"A segunda variável é: {Var2}")

