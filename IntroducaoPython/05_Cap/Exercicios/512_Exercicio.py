divida = float(input("Digite o valor da sua Divida R$ "))
juros_mensal = float(input("Digite o valor do juros mensal % "))

valor_mensal = (divida/12) + ((divida/12) * (juros_mensal/100))

print(valor_mensal)
