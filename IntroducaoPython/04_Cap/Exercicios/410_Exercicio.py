# Calcular preço da Energia Elétrica
print("****** Tipo de Instalação ******")
print("\n1 - Residência\n2 - Indústrial\n3 - Comércios\n")
print("*********************************\n")

tipo = int(input("Digite a letra do tipo de Instalação: "))
kwh = float(input("Digite a quantidade de KWh: "))

if tipo == 1:
    if kwh <= 500:
        preço = kwh * 0.40
    else:
        preço = kwh * 0.65
elif tipo == 2:
    if kwh <= 1000:
        preço = kwh * 0.55
    else:
        preço = kwh * 0.60
elif tipo == 3:
    if kwh <= 5000:
        preço = kwh * 0.55
    else:
        preço = kwh * 0.60
else:
    print("\nTipo de Instalação Inválido")

print("Valor Total: %.2f"%preço)
