entrada = input("Digite uma lista de números inteiros separados por espaços: ")
numeros = [int(x) for x in entrada.split()]

soma = sum(numeros)

print(f"A soma de todos os elementos é: {soma}")
