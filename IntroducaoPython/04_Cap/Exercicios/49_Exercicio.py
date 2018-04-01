#Programa Empréstimo Bancário
valor_casa = float(input("Digite o preço da casa desejável: "))
salario = float(input("Digite o valor do seu salário: "))
anos = int(input("Em quantos anos você deseja pagar a casa: "))

porcentagem = salario * 0.30
prestacao = valor_casa / (anos * 12)

if prestacao < porcentagem:
    print("\nÉ possível comprar está casa")
    print("Valor da Prestação: R$ %.2f"%prestacao)
else:
    print("\nO valor da prestação é superior à 30% do seu salário.")
    print("Valor da Prestação: R$ %.2f"%prestacao)
