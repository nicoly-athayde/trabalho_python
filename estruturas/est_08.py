# Solicita três números ao usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Verifica se os três números são iguais
if num1 == num2 == num3:
    print("Os três números são iguais.")
else:
    # Verifica qual é o maior número
    maior = max(num1, num2, num3)
    print(f"O maior número é {maior}.")
