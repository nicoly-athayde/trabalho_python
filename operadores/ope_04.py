# Programa que recebe dois números inteiros e exibe o quociente inteiro e o resto
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

quociente = numero1 // numero2
resto = numero1 % numero2

print(f"O quociente da divisão de {numero1} por {numero2} é: {quociente}")
print(f"O resto da divisão de {numero1} por {numero2} é: {resto}")
