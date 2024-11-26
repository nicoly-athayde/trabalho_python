try:
    with open("mensagem.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("Erro: O arquivo mensagem.txt não foi encontrado.")
