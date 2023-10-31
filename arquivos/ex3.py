#Escreva um programa que receba do usuário 5 números inteiros e o nome do arquivo no qual eles devem ser armazenados. 
# Em seguida, ler do arquivo os valores armazenados copiando-os para uma lista de inteiros e os imprimindo na tela.

d = input("Insira um nome para o arquivo: ")
arquivo = open(f"{d}.txt", "w")
n = 5
for linha in range(n):
    c = int(input("Insira um número inteiro: "))
    arquivo.write(f"{c} \n")

with open(f"{d}.txt", "r") as arquivo, open(f"Inteiros.txt", "w") as inteiros:
    for l in arquivo.readlines():
        if int(l) % 1 == 0:
            inteiros.write(f"{l}")
            print(l)