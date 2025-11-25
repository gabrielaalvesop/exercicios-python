resposta = "S"
soma=quant=media=maior=menor=0
while resposta in "Ss":
    numero = int(input("Digite um numero: "))
    soma+=numero
    quant+=1
    if quant == 1:
        maior=menor=numero
    else:
        if numero > maior:
            maior=numero
        if numero < menor:
            menor=numero
    resposta=str(input("Quer continuar? [S/N] ")).upper().strip()[0]
media = soma/quant
print(f"Você digitou {quant} números e a média foi {media:.2f}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
