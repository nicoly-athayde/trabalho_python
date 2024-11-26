def é_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    return False

# Solicitar o ano ao usuário
ano = int(input("Digite um ano: "))

# Chamar a função e exibir o resultado
if é_bissexto(ano):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
