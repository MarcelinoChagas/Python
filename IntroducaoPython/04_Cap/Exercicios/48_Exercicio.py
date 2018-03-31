n1 = float(input("Digite o 1° Valor: "))
n2 = float(input("Digite o 2° Valor: "))
print()
print("1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisao")
opcao = int(input("\nDigite a opção desejada: "))


if opcao == 1:
    soma = n1 + n2
    resultado = soma
elif opcao == 2:
    subtracao = n1 - n2
    resultado = subtracao
elif opcao == 3:
    multiplicacao = n1 * n2
    resultado = multiplicacao
elif opcao == 4:
    if n2 != 0:
        divisao = n1 / n2
        resultado = divisao
    else:
        print("Impossível Dividir por 0")
        resultado = 0
else:
    print("Opção Inválida.")
    resultado = 0
    
print("Resultado: %.2f" %resultado)
