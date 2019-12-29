# coding: utf-8

# a = 10
# b = 25
# c = 66
#
# x = int(input("Digite um número: "))
#
# #if(x == a or x == b or x == c ):
# if(x in [a,b,c]):
#     print("Está Contido")
# else:
#     print("Não está Contido")

cores = ["azul","amarela","vermelho","branco"]

while True:
    cor = input("Digite um nome de uma cor,"
                  "0 para sair: ")
    if(cor=="0"):
        break
    elif cor in cores:
        print("Essa cor está contida")
    else:
        print("Essa cor NÃO está contida")