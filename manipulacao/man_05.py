try:
    with open("texto.txt", "r") as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        print(f"O número total de palavras no arquivo é: {len(palavras)}")
except FileNotFoundError:
    print("Erro: O arquivo texto.txt não foi encontrado.")
