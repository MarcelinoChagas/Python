salario = int(input("Salario Atual: "))
porcentagem = float(input("Porcentagem: "))

aumento = salario + (salario * (porcentagem/100))

print("Salario com Aumento: R$ %.2f" %aumento)
