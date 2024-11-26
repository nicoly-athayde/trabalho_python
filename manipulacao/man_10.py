entrada = input("Digite a nova entrada para o diário: ")

try:
    with open("diario.txt", "a") as arquivo:
        arquivo.write(entrada + "\n")
    print("Entrada adicionada com sucesso!")
except FileNotFoundError:
    with open("diario.txt", "w") as arquivo:
        arquivo.write(entrada + "\n")
    print("Arquivo criado e entrada adicionada com sucesso!")
