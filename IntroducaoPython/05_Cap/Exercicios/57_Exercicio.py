n = int(input("Tabuada de : "))
inicio = int(input("Digite o número de inicio da tabuada: "))
fim = int(input("Digite o número fim da tabuada: "))

while inicio <= fim:
    print(n,"x",inicio,"=",(n*inicio))
    inicio = inicio + 1
