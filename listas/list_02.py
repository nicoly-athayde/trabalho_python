entrada = input("Digite uma lista de números separados por espaços: ")
numeros = [int(x) for x in entrada.split()]

maior = max(numeros)
menor = min(numeros)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
