numeros = []
for i in range(10):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

media = sum(numeros) / len(numeros)

maiores_que_media = len([num for num in numeros if num > media])

print(f"A quantidade de números maiores que a média ({media}) é: {maiores_que_media}")
