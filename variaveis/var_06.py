# Solicita três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Troca os valores conforme a solicitação
num1, num2, num3 = num2, num3, num1

# Exibe os novos valores
print(f"Após a troca, os valores são: num1 = {num1}, num2 = {num2}, num3 = {num3}.")
