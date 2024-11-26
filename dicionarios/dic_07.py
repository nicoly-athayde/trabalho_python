produtos = {
    "Arroz": 5.50,
    "Feijão": 7.30,
    "Macarrão": 3.40,
    "Óleo": 4.20,
    "Açúcar": 2.90
}

produto_buscar = input("Digite o nome do produto que deseja buscar: ")

if produto_buscar in produtos:
    print(f"O preço do {produto_buscar} é: R${produtos[produto_buscar]:.2f}")
else:
    print(f"O produto '{produto_buscar}' não foi encontrado.")
