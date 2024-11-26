def media(numeros):
    return sum(numeros) / len(numeros)

# Solicitar uma lista de números ao usuário
entrada = input("Digite os números separados por espaço: ")
numeros = [float(x) for x in entrada.split()]

# Chamar a função e exibir o resultado
resultado = media(numeros)
print(f"A média dos números é: {resultado}")
