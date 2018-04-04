deposito = float(input("Digite o valor do deposito: R$ "))
taxa = float(input("Digite a taxa de juros: % "))
mes = 1
total = 0
juros = 0

while mes <= 24:
    juros = (deposito * (taxa/100))
    deposito = deposito + juros
    total = total + juros
    print("Valor no %d° Mês: %.2f" %(mes,deposito))
    mes = mes + 1
print("\nTotal Juros: %.2f"%total)
