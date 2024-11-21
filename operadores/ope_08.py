# Programa que solicita o preço de um produto e o desconto, e calcula o valor final
preco = float(input("Digite o preço do produto: "))
desconto_percentual = float(input("Digite a porcentagem de desconto: "))

desconto = preco * (desconto_percentual / 100)
preco_final = preco - desconto

print(f"O valor do desconto é: {desconto}")
print(f"O preço final do produto com desconto é: {preco_final}")
