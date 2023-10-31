usuario = open("arquivos2/usuarios.txt", "w")
qntUsuarios = 1
espacoutilizado = []
nome = []
id = []
capacidadetotal = 2581.54
porcentagem = []


for i in range(qntUsuarios):
    nome.append(input(f"Insira o nome do usuário: "))
    id.append(int(input(f"Insira o ID do usuário: ")))
    espacoutilizado.append(float(input("Insira o espaço utilizado em bytes: ")))
    usuario.write(f"Nome do usuário {nome[i]}, e ID {id[i]} \n")
    espacoutilizado.append(espacoutilizado[i]//1000024)
    porcentagem = (espacoutilizado/capacidadetotal) * 100

relatorio = open("arquivos2/relatorio.txt", "w")
