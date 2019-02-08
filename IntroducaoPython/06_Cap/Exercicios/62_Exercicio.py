import os
clear = lambda: os.system('cls')
L1 = []
L2 = []
while True:
    x = int(input("Digite um numero para a lista 1: "))
    L1.append(x)
    y = int(input("Digite um numero para a lista 2: "))
    L2.append(y)
    z = int(input("Deseje Continuar (1-Sim/2-Não)?  "))
    clear()
    if z == 2:
        break
L3 = L1[:]
L3.extend(L2[:])
v = 0
c = 1

while True:
    if L3[v] == L3[c]:
        del L3[v]
        L3[v] = L3[c]
        v += 1
    elif v > len(L3):
        break    

print("Valores da Lista 3")
print(sorted(L3))
