nomes = []

with open ("Final/CLT.csv", "r") as clt, open("Final/Ocupantes.csv", "r") as ocupantes, open("Final/Painel.csv", "w") as painel:
    for linha in clt:
        coluna = linha.split(";")
        if (coluna[1] not in nomes and coluna[1] != "Nome"):
            nomes.append(coluna[1])

    for linha in ocupantes:
        coluna = linha.split(";")
        if (coluna[1] not in nomes and coluna[1] != "Nome"):
            nomes.append(coluna[1])
    
    for i in nomes:
        painel.write(i + "\n")
    

print(nomes)
print(len(nomes))