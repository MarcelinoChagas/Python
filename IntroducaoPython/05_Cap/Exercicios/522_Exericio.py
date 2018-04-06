import os
clear = lambda: os.system('cls')
while True:
    print("***** Menu Calculadora *****")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    opcao = int(input("\nDigite a opção desejada: "))

    if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
        n1 = float(input("\nDigite o 1° valor: "))
        n2 = float(input("Digite o 2° valor: "))
    if opcao == 1:
        soma = n1 + n2
        texto = 'Soma'
        resultado = soma
        clear()
    elif opcao == 2:
        subtracao = n1 - n2
        texto = 'Subtração'
        resultado = subtracao
        clear()
    elif opcao == 3:
        mult = n1 * n2
        texto = 'Multiplicação'
        resultado = mult
        clear()
    elif opcao == 4:
        if n2 != 0:
            divisao = n1 / n2
            texto = 'Divisão'
            resultado = divisao            
            clear()
        else:
            print("Divisão Inválida")
            clear()
    elif opcao == 0:
        break
    else:
        print("Opção Inválida")
    print("1° Valor: %.2f"%n1)
    print("2° Valor: %.2f"%n2)
    print("Resultado da",texto,"%.2f\n"%resultado)
