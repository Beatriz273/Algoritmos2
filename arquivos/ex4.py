#Utilize os arquivos pares.txt e impares.txt gerados através do código-fonte, apresentado nos slides. 
# Faça a leitura destes dois arquivos e crie um só arquivo denominado de pareseimpares.txt 
# com base em todas as linhas dos dois arquivos lidos e para preservar a ordem numérica.
with open("arquivos/impar.txt", "w") as impar, open("arquivos/par.txt", "w") as par:
    for n in range(0, 10):
        if n % 2 == 0:
            par.write(f"{n}\n")
        else:
            impar.write(f"{n}\n")

with open("arquivos/impar.txt", "r") as impar, open("arquivos/par.txt", "r") as par, open("arquivos/pareimpar.txt", "w") as pareimpar:
    lpar = par.readlines()
    limpar = impar.readlines()
    for linha in range(len(lpar)):
        pareimpar.write(lpar[linha])
        pareimpar.write(limpar[linha])

                


