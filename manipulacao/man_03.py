nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

with open("usuario.txt", "a") as arquivo:  # "a" abre o arquivo para adicionar ao final
    arquivo.write(f"Nome: {nome}, Idade: {idade}\n")

print("Informações gravadas com sucesso!")
