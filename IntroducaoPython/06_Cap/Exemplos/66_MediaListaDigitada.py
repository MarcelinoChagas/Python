notas=[0,0,0,0,0]
soma = 0
x=0
while x<5:
    notas[x] = float(input("Nota %d: " % x))
    soma += notas[x]
    x += 1
x=0
while x<5:
    print("Nota %d: %.2f" %(x,notas[x]))
    x += 1
print("Média: %.2f" %(soma/x))
