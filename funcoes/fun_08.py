def contar_vogais(s):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in s if letra in vogais)

# Solicitar uma frase ao usuário
frase = input("Digite uma frase: ")

# Chamar a função e exibir o resultado
resultado = contar_vogais(frase)
print(f"O número de vogais na frase é: {resultado}")
