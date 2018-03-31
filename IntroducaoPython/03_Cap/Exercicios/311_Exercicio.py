mercadoria = int(input("Preço Mercadoria: "))
porcentagem = float(input("Percentual Desconto: "))

porc_desconto = mercadoria * (porcentagem/100)
desconto = mercadoria - (mercadoria * (porcentagem/100))

print("Valor Desconto: R$ %.2f"% porc_desconto)
print("Valor a pagar com Desconto: R$ %.2f" %desconto)
