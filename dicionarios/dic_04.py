pessoas = {
    "João": 25,
    "Maria": 30,
    "Pedro": 22
}

nome_buscar = input("Digite o nome da pessoa que deseja buscar: ")

if nome_buscar in pessoas:
    print(f"{nome_buscar} foi encontrado.")
else:
    print(f"{nome_buscar} não foi encontrado.")
