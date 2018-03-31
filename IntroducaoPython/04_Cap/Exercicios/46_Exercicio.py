distancia = float(input("Digite a distância: "))
if distancia <= 200:
    passagem = distancia * 0.50
    print("Valor da Passagem: %.2f" %passagem)
else:
    passagem = distancia * 0.45
    print("Valor da Passagem: %.2f" %passagem)
