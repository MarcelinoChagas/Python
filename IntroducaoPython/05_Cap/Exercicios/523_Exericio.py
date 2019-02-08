numero = int(input("Digite um número: "))
fim = 0
final = 0
cont = 2
while numero >= 2:
    while final != numero:
        if numero % 2 < numero:
            final += 1
        elif numero % 2 == 1:
            final += 1
        elif final >= 1 :
            print("%d Número Primo"%numero)
    #if numero == 2:
#        print("%d Número Primo" %numero)
    else:
        print("%d Não é primo" %numero)
    numero -= 1
