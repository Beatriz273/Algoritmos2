#Faça um algoritmo que lê 10 valores para uma variável do tipo lista de nome x e
#mostre os 10 valores armazenados.

x = [0,0,0,0,0,0,0,0,0,0]

for i in range (10):
    x[i] = int(input(f"Informe o valor do índice {i}:"))
    if x[i] == x[9]:
        print(f"Os valores da sua lista são: x:{x}")
