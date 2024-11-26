def fatorial(n):
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

# Solicitar o número ao usuário
numero = int(input("Digite um número para calcular o fatorial: "))

# Chamar a função e exibir o resultado
resultado = fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")
