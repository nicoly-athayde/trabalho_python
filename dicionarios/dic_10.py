livro = {
    "título": "O Senhor dos Anéis",
    "autor": "J.R.R. Tolkien",
    "ano": 1954
}

# Atualizando o ano de publicação
novo_ano = int(input("Digite o novo ano de publicação: "))
livro["ano"] = novo_ano

# Exibindo o dicionário atualizado
print(livro)
