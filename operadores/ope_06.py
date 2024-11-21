# Programa que troca os valores de duas variáveis sem usar uma variável auxiliar
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))

a = a + b  # Somando os valores
b = a - b  # Subtraindo o valor de b da soma
a = a - b  # Subtraindo o valor de a da soma

print(f"Após a troca, o valor de a é {a} e o valor de b é {b}")
