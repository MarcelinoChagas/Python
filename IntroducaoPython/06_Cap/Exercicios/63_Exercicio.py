import os
clear = lambda: os.system('cls')

L1 = [1,2,2]
L2 = [3,3,6,6,7,7]

print(L1)
print(L2)

x = 0
L3 = []
tam = len(L1)

while len(L1) < x:
    if L1[x] == L1[tam-1]:
        x += 1

    L3.append(x)

print(L3)
