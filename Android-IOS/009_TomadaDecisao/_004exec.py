idade = int(input("Digite Idade: "))

if(idade >0 and idade < 18):
    print("De Menor")
if(idade >= 18):
    print("De Maior")
elif(idade < 0):
    print("Nem Nasceu")