import csv

try:
    with open("dados.csv", "r") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for linha in leitor:
            print("\t".join(linha))  # Exibe os dados separando por tabulação
except FileNotFoundError:
    print("Erro: O arquivo dados.csv não foi encontrado.")
