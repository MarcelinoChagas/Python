num1 = int(input("Digite o 1º Número: "))
num2 = int(input("Digite o 2º Número: "))
print()

for n in range(num1,num2):
    dividendo = []
    for x in range(1,num2):
        if(n % x == 0):
            dividendo += [x]
    if len(dividendo) == 2:
        print(n)