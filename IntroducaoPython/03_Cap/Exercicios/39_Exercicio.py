dias = int(input("Qtd. Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
print(" ")
print("Dias: %d" % dias)
print("Horas: %d" % horas)
print("Minutos: %d" % minutos)
print("Segundos: %d" % segundos)

total = (dias * 86400)
total = total + (horas * 3600)
total = total + (minutos * 60)
total = total + segundos

print("Total em Segundos: %i " % total)
