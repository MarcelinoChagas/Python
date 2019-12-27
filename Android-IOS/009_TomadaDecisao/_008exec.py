num1 = int(input("Digite 1º número: "))
num2 = int(input("Digite 2º número: "))

if(num1 > num2):
    print("1º Número é maior %d > %d"%(num1,num2))
elif(num1 < num2):
    print("2º Número é maior %d > %d"%(num2,num1))
else:
    print("Números são iguais")