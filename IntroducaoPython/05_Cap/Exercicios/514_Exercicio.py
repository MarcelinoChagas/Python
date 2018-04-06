count = 1
soma = 0
media = 0
while True:
    num = int(input("Digite um número inteiro: "))
    count = count + 1
    soma = soma + num
    media = soma/(count-1)
    if num == 0:
        break
print("Soma: %d"%soma)
print("Média: %d"%media)
