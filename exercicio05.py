cont=0
for x in range(1,10,1):
    n = float(input("Digite o número"))
    if n < 0:
        cont = cont + 1
print(f"Você digitou {cont} números negativos.")