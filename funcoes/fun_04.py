def maior(a, b, c):
    return max(a, b, c)

# Solicitar os números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Chamar a função e exibir o resultado
resultado = maior(num1, num2, num3)
print(f"O maior número é: {resultado}")
