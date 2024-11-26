def é_par(n):
    return n % 2 == 0

# Solicitar o número ao usuário
numero = int(input("Digite um número: "))

# Chamar a função e exibir o resultado
if é_par(numero):
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
