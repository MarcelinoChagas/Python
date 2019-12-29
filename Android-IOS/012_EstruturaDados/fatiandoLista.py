"""
 0  1  2  3  4  5
 P  Y  T  H  O  N
-6 -5 -4 -3 -2 -1

lista[X:Y:Z]
X -> Start
Y -> Stop
Z -> Step

"""


lista = list("Python")
print(lista[0])     # Imprimi o valor do indice 0º Elemento
print(lista[:2])    # Imprime o valor do indice 0º até o 1º Elemento
print(lista[2:])    # Imprime o valor do indice 2º até o último elemento
print(lista[::2])   # Imprime o valor do indice pulando de 2 em 2
print(lista[2::2])  # Imprime o valor do indice 2º pulando de 2 até o final
print(lista[::-1])  # Imprime a lista inversa


lista2 = list("Marcelino Francisco")
print(lista2[::-1])