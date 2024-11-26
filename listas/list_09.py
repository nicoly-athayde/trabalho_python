numeros = []
for i in range(5):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

maior = max(numeros)
numeros[numeros.index(maior)] = 0

print(f"Lista atualizada: {numeros}")
