filho = int(input("Digite idade do Filho: "))
mae = int(input("Digite idade da Mãe: "))

if((mae - filho) < 10):
    print("IMPUSSIBRI")
if(mae-filho > 10 and mae-filho < 15):
    print("PEDOFILO?")
else:
    print("TEVE COM %d anos" %(mae-filho))