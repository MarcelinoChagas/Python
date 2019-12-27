num1 = int(input("Digite o 1º Número: "))
num2 = int(input("Digite o 2º Número: "))
print()

val1 = int(input("1º Valor: "))
val2 = int(input("2º Valor: "))
val3 = int(input("3º Valor: "))
print()

for n in range(num1, num2):
    if(val1 == n or val2 == n or val3 == n):
        continue
    print(n)