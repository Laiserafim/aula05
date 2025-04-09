dentro=0
fora=0
for x in range (1,5,1):
    n=int(input("Digite um número "))
    if n >=10 and n <=20:
        dentro = dentro + 1

    else:
        fora= fora + 1

print(f"Você digitou {dentro} dentro do intervalo")
print(f"Você digitou {fora} fora do intervalo")
