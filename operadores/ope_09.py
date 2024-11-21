# Programa que solicita a distância percorrida e o tempo gasto e calcula a velocidade média
distancia = float(input("Digite a distância percorrida (em km): "))
tempo = float(input("Digite o tempo gasto (em horas): "))

velocidade_media = distancia / tempo
print(f"A velocidade média foi: {velocidade_media} km/h")
