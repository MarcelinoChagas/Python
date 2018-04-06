deposito = float(input("Digite o valor do deposito Inicial: R$ "))
taxa = float(input("Digite a taxa de juros: % "))
mes = 1
total = 0
juros = 0

while mes <= 24:
    if mes <= 1:
        juros = (deposito * (taxa/100))
        deposito = deposito + juros
        total_deposito = deposito
    deposito_mes = float(input("Digite o valor do deposito do %d° mês: R$ "%mes))
    juros = (total_deposito * (taxa/100))
    total = total + juros
    total_deposito = total_deposito + deposito_mes + juros
    print("Valor no %d° Mês: %.2f" %(mes,total_deposito))
    mes = mes + 1
print("\nTotal Juros: %.2f"%total)
