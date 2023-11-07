with open("arquivos/impar.txt", "w") as impar, open("arquivos/par.txt", "w") as par:
    for n in range(0, 10):
        if n % 2 == 0:
            par.write(f"{n}\n")
        else:
            impar.write(f"{n}\n")

with open("arquivos/divisivel4.txt", "w") as multiplos4, open("arquivos/par.txt", "r") as par:
    for l in par.readlines():
        if int(l) % 4 == 0:
            multiplos4.write(f"{l}")