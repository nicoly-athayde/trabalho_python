entrada = input("Digite uma lista de palavras separadas por espaços: ")
palavras = entrada.split()

palavra_buscar = input("Digite a palavra que deseja buscar: ")

if palavra_buscar in palavras:
    print(f"A palavra '{palavra_buscar}' está na lista.")
else:
    print(f"A palavra '{palavra_buscar}' não está na lista.")
