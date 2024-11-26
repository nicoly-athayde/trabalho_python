nome_arquivo = input("Digite o nome do arquivo: ")
texto = input("Digite o texto a ser gravado no arquivo: ")

with open(nome_arquivo, "w") as arquivo:
    arquivo.write(texto)

print(f"Arquivo '{nome_arquivo}' criado e texto gravado com sucesso!")
