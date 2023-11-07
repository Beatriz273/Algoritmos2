coluna = []

with open("Relacao_de_Empregados_CLT.csv", "r") as CLT, open ("Relacao_de_Ocupantes_CC___FG2.csv", "r") as Relacao, open ("linhas.csv", "w"):
    for linha in CLT:
        coluna = linha.split(;)