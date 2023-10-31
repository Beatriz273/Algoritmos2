# Faça um programa que crie um arquivo texto e que salve seu nome neste arquivo (o nome deve ser  informado via terminal).
# Faça um programa que crie um arquivo texto e que salve seu nome
# neste arquivo, após sobrescreva o conteúdo deste arquivo com a frase “Eu amo
# algoritmos!”.
arquivo = open("bia.txt", "w")

for linha in range(5):
    c = input("Insira seu nome: ")
    arquivo.write(f"{c} \n")

arquivo.close()
