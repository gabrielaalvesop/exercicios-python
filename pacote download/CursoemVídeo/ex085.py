números=[], []
valor = []
for contador in range(1, 8):
    valor=(int(input(f'Digite o {contador}º valor: ')))
    if valor % 2==0:
        números[0].append(valor)
    else:
        números[1].append(valor)
números[0].sort()
números[1].sort()
print(f"Os valores pares digitados foram {números[0]}")
print(f"Os valores ímpares digitados foram {números[1]}")