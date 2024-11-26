def calcular_preco_final(preco, desconto):
    return preco * (1 - desconto / 100)

# Solicitar preço e desconto ao usuário
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite a porcentagem de desconto: "))

# Chamar a função e exibir o resultado
preco_final = calcular_preco_final(preco, desconto)
print(f"O preço final com desconto é: {preco_final}")
