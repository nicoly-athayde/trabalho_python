# Solicita o nome do produto, quantidade e preço unitário
produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))
preco_unitario = float(input("Digite o preço unitário do produto: "))

# Calcula o valor total da compra
valor_total = quantidade * preco_unitario

# Exibe o resultado
print(f"O valor total da compra de {quantidade} {produto}(s) é {valor_total}.")
