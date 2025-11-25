numeros=[]
while True:
    numeros.append(int(input('Digite um valor: ')))
    resposta=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'N':
        break
print(f"Foram digitados {len(numeros)} valores")
numeros.sort(reverse=True)
print(f"Os valores ordenados em ordem decrescente: {numeros}")
if 5 in numeros:
    print("O 5 está na lista")
else:
    print("O 5 não está na lista")