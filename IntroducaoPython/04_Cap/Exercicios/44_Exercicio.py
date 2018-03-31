salário = float(input("Digite o salário: "))
if salário > 1250:
    salário = salário + (salário * 0.10)
    print("Salário: %.2f" %salário)
if salário <= 1250:
    salário = salário + (salário * 0.15)
    print("Salário: %.2f" %salário)
