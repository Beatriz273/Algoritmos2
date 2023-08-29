# Faça um algoritmo que lê 10 valores para uma variável do tipo lista de nome x.
#Após completar toda a leitura da lista, verificar se cada valor armazenado na
#lista é par ou ímpar. Se for par, fazer com que o valor seja atualizado para o
#resultado da multiplicação do valor contido pelo índice. Se for impar fazer com
#que a lista receba o valor do seu próprio índice

x = [0,0,0,0,0,0,0,0,0,0]

for i in range (10):
    x[i] = int(input(f"Informe o valor do índice {i}:"))

for i in range (10):
    if (x[i] % 2 == 0):
        x[i] = x[i] * i
    else:
        x[i] = i

for i in range (10):
    print(f"Os novos valores de sua lista são: [{i}]:[{x[i]}]")