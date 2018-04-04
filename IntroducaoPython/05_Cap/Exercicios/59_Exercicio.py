n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o primeiro numero: "))
aux = 0
resultado = 0

if n1 >= n2:
    while (aux != n1):
        aux = aux + n2
        resultado = resultado + 1
    print(n1,"/",n2,"=",resultado)
else:
    print("Não é uma divisao inteira.")
