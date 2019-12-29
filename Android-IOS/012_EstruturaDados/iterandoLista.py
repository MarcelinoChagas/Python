# Não realiza a soma
# lista_numeros = [100,200,300,400]
# for item in lista_numeros:
#     item += 1000
# print(lista_numeros)

# Codigo com Range
# lista_numeros = [100,200,300,400,2]
# for item in range(len(lista_numeros)):
#     lista_numeros[item] += 1000
# print(lista_numeros)

print(range(0,4))
print(list(range(0,4)))

print()

l = ['a','b','c','d']
print(enumerate(l))
print(list(enumerate(l)))
print()

#Função com enumerate ao invés de range
lista_numeros = [100,200,300,400,2]
for idx,item in enumerate(lista_numeros): #
    lista_numeros[idx] += 1000
print(lista_numeros)