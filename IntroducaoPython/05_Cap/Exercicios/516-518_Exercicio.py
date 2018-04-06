valor = int(input("Digite o valor a pagar: "))
caixa = 2000
ced_50 = 0
ced_20 = 0
ced_10 = 0
while valor > 50:
    ced_50 += 1
    valor = valor - 50
while valor >= 20:
    ced_20 += 1
    valor -= 20
while valor >= 10:
    ced_10 += 1
    valor -= 10
if valor == 0:
    print("Sem valor para saque")
print("Cedulas de 50: %d" %ced_50)
print("Cedulas de 20: %d" %ced_20)
print("Cedulas de 10: %d" %ced_10)
