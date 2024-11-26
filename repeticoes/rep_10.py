n = int(input("Digite um número inteiro positivo: "))

if n < 2:
    print(f"O número {n} não é primo.")
else:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    if primo:
        print(f"O número {n} é primo.")
    else:
        print(f"O número {n} não é primo.")
