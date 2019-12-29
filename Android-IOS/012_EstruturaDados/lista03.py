lista = [1,2,3,4,5]
print(lista)

lista = lista + [6] #Concatenando valor no final da lista
print(lista)

lista = [-1] + lista #Concatenando valor no inicio da lista
print(lista)

lista = lista + [7,8,9] #Concatenando valores no final da lista
print(lista)

lista = lista + [[10,11]] #Concatenando lista no final da lista
print(lista)

lista.append(12) #Adiciona valor no final da lista
print(lista)

del(lista[10]) #Deleta Valor de uma lista apartir do indice
print(lista)