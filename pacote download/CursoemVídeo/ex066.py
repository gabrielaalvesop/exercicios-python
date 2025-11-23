soma=cont=0
while True:
    numero = int(input("Digite um numero [999 para parar]: "))
    if numero==999:
        break
    soma+=numero
    cont+=1
print(f"A soma dos {cont} valores foi {soma:.0f}")