coluna = []

with open("CLT.csv", "r") as CLT, open ("Ocupantes.csv", "r") as Relacao, open ("linhas.csv", "w"):
    for linha in CLT:
        coluna = linha.split(";")