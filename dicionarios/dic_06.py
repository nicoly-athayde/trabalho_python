dicionario = {}

for i in range(3):
    chave = input(f"Digite a chave do {i + 1}º par: ")
    valor = input(f"Digite o valor para '{chave}': ")
    dicionario[chave] = valor

# Exibindo o dicionário
print(dicionario)
