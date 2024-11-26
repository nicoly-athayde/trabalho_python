alunos = {}

for i in range(5):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota

# Exibindo o nome e a nota de cada aluno
for nome, nota in alunos.items():
    print(f"{nome}: {nota}")
