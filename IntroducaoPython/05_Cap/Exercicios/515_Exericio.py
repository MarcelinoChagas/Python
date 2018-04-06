total = 0
while True:
    codigo = int(input("Digite o código do produto: "))
    if codigo == 0:
        break
    qtd = int(input("Digite a quantidade do produto: "))

    if codigo == 1:
        total = total + (qtd * 0.50)
    elif codigo == 2:
        total = total + (qtd * 1)
    elif codigo == 3:
        total = total + (qtd * 4)
    elif codigo == 5:
        total = total + (qtd * 7)
    elif codigo == 9:
        total = total + (qtd * 8)
    else:
        print("Código Inválido !")
print("Total: %.2f"%total)
