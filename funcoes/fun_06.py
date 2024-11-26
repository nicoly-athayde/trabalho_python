def inverter(s):
    return s[::-1]

# Solicitar a palavra ao usuário
palavra = input("Digite uma palavra para inverter: ")

# Chamar a função e exibir o resultado
resultado = inverter(palavra)
print(f"A palavra invertida é: {resultado}")
