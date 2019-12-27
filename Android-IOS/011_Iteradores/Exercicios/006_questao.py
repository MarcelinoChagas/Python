for n in range(1,100):
    dividendo = []
    for x in range(1,100):
        if(n % x == 0):
            dividendo += [x]
    if len(dividendo) == 2:
        print(n)