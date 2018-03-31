a = float(input("Digite o 1° Valor: "))
b = float(input("Digite o 2° Valor: "))
c = float(input("Digite o 3° Valor: "))

if a > b and a > c:
    print("1° Valor é maior")
    if c > b:
        print("2° Valor é menor")
    if b > c:
        print("3° Valor é menor")
if b > a and b > c:
    print("2° Valor é maior")
    if a > c:
        print("3° Valor é menor")
    if c > a:
        print("1° Valor é menor")
if c > a and c > b:
    print("3° Valor é maior")
    if b > a:
        print("1° Valor é menor")
    if a > b:
        print("2° Valor é menor")
if a == b and a == c and c == b:
    print("São iguais")
