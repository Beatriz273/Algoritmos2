usuario = open("arquivos2/usuarios.txt", "w")
qntUsuarios = 2
espacoutilizado = []
nome = []
id = []
porcentagem = []
espacomedio = []
capacidadetotal = []

def nomeeID():
    for i in range(qntUsuarios):
        nome.append(input(f"Insira o nome do usuário: "))
        id.append(int(input(f"Insira o ID do usuário: ")))
        usuario.write(f"Nome do usuário {nome[i]}, e ID {id[i]} \n")
    
def espaco():
    for i in range(qntUsuarios):
        espacoutilizado.append(int(input("Insira o espaço utilizado em bytes: ")))
        espacoutilizado[i] = (espacoutilizado[i] / 1000024)
        capacidadetotal = []
        capacidadetotal += espacoutilizado[i]

def porcentagemusuarios():
    for i in range(qntUsuarios):
        porcentagem.append((espacoutilizado[i]/capacidadetotal[i]) * 100)

relatorio = open("arquivos2/relatorio.txt", "w")

nomeeID()
espaco()
porcentagemusuarios()

for i in range(qntUsuarios):
    relatorio.write(f"O {i+1}º usuário {nome[i]} utiliza cerca de {espacoutilizado[i]}MB. Cerca de {porcentagem[i]:.2f}% da capacidade total.")
    relatorio.write(f"Espaço total ocupado: {capacidadetotal}")
