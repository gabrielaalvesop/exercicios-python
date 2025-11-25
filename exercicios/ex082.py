numeros=[]
pares=list()
ímpares=list()

while True:
    numeros.append(int(input("Digite um valor: ")))
    resposta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resposta == "N":
        break
for indice, numero in enumerate(numeros):
    if numero % 2 == 0:
        pares.append(numero)
    elif numero % 2 == 1:
        ímpares.append(numero)

print(f"Os valores digitados foram {numeros}")
print(f"Os valores pares digitados foram {pares}")
print(f"Os valores ímpares digitados foram {ímpares}")
