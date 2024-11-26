try:
    with open("original.txt", "r") as arquivo_original:
        conteudo = arquivo_original.read()
    with open("copia.txt", "w") as arquivo_copia:
        arquivo_copia.write(conteudo)
    print("Conteúdo copiado com sucesso para o arquivo copia.txt!")
except FileNotFoundError:
    print("Erro: O arquivo original.txt não foi encontrado.")
