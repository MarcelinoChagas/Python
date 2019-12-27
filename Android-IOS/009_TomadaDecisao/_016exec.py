ip = (input("Digite um IP (Ex: 255.255.255.255): "))

tam = int (len(ip))

resto = ip // tam * 10
print(resto)
