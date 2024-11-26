num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

if operador == "+":
    print(f"O resultado da soma é: {num1 + num2}")
elif operador == "-":
    print(f"O resultado da subtração é: {num1 - num2}")
elif operador == "*":
    print(f"O resultado da multiplicação é: {num1 * num2}")
elif operador == "/":
    if num2 != 0:
        print(f"O resultado da divisão é: {num1 / num2}")
    else:
        print("Erro: Não é possível dividir por zero.")
else:
    print("Erro: Operador inválido.")
