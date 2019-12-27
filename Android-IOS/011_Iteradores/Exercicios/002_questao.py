print("Digite os valores do intervalo que você deseja imprimir ")
val1 = int(input("Digite o primeiro valor: "))
val2 = int(input("Digite o segundo valor: "))

if(val1 > val2):
    val1, val2 = val2, val1

for x in range(val1,val2):
    print(x)