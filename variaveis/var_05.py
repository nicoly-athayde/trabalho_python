# Solicita o salário bruto e o valor do desconto
salario_bruto = float(input("Digite seu salário bruto: "))
desconto = float(input("Digite o valor do desconto: "))

# Calcula o salário líquido
salario_liquido = salario_bruto - desconto

# Exibe o resultado
print(f"O seu salário líquido é {salario_liquido}.")
