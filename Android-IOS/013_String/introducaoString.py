s1 = 'Marcelino'
s2 = "Chagas"
s3 = '''aaaa
bbbb
cccc'''

print(s1)
print(s2)
print(s3)

# print(chr(101)) # Converte valor ao respectivo simbolo na tabela ASCII
# print(ord("e")) # Converte letra no respectivo valor na tabela ASCII

# for c in range(122):
#     print(str(c) +" - "+ chr(c))

s = "Marcelino é Lindo"
# lista = s.split(" ")
# print(lista[0]+" "+lista[2])
print(id(s))
print(s.replace("é", "É MUITO"))
s = s.replace("é", "É MUITO")
print(id(s))
