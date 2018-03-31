print("******************************************")
print("********* REDUÇÃO TEMPO DE VIDA **********")
print("******************************************")
print()
cigarros = int(input("Quantos cigarros você fuma por dia ? "))
anos = int(input("Por quantos anos você fuma ? "))
tempo_vida = (anos * (cigarros * 10))/24
if cigarros <= 5:
    print("Tempo de vida perdido: %d Dias" %tempo_vida)
else:
    if cigarros >= 10:
        print()
        print("Você está em Depressão peste ? Pare de Fumar ")
