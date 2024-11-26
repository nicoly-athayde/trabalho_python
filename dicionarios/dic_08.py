palavra = input("Digite uma palavra: ")

frequencia = {}

for letra in palavra:
    if letra in frequencia:
        frequencia[letra] += 1
    else:
        frequencia[letra] = 1

# Exibindo o dicionário de frequências
print(frequencia)
