velocidade = float(input("Digite a velocidade do carro: "))

if velocidade > 80:
    print("Hey peste, você foi multado!")
    multa = (velocidade - 80) * 5
    print("Valor da Multa: %.2f" %multa)
