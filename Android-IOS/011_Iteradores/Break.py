
i = 10
print("Inicio While")
while(i < 100):
    i += 1
    if(True):
        break
print("Fim While")

print("Inicio For")
for item in range(10):
    print(item)
    if(item==6):
        print("Verdade")
        break
print("Fim For")

