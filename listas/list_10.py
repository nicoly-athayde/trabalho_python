lista1 = []
lista2 = []

for i in range(5):
    num1 = int(input(f"Digite o {i + 1}º número para a lista 1: "))
    lista1.append(num1)

for i in range(5):
    num2 = int(input(f"Digite o {i + 1}º número para a lista 2: "))
    lista2.append(num2)

soma_listas = [lista1[i] + lista2[i] for i in range(5)]

print(f"A soma dos elementos correspondentes das listas é: {soma_listas}")

