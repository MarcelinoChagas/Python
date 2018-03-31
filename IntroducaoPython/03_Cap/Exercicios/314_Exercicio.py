print("Valor do Dia com o Carro: R$ 60.00")
print("Valor do KM Rodado com o Carro: R$ 0.15")
print("*******************************************")
qtd_km = float(input("Digite a quantidade de KM percorrido: "))
dias = int(input("Digite a quantidade de Dias: "))
total_km = qtd_km * 0.15
total_dias = dias * 60
print("Valor Total dos KM: R$ %.2f" %total_km)
print("Valor Total dos Dias: R$ %.2f" %total_dias)
total = total_km + total_dias
print("Valor Total: R$ %.2f"%total)
