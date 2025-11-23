lista_temporaria = []
lista_principal = []
maior_peso=menor_peso=0
while True:
    lista_temporaria.append(str(input("Nome: ")))
    lista_temporaria.append(float(input("Peso: ")))
    if len(lista_principal) == 0:
        maior_peso=menor_peso=lista_temporaria[1]
    else:
        if lista_temporaria[1] > maior_peso:
            maior_peso=lista_temporaria[1]
        if lista_temporaria[1] < menor_peso:
            menor_peso=lista_temporaria[1]
    lista_principal.append(lista_temporaria[:])
    lista_temporaria.clear()
    resposta = str(input("Deseja continuar? [S/N]"))
    if resposta in 'Nn':
        break
print('-='*30)
print(f"Ao todo, você cadastrou {len(lista_principal)} pessoas.")
print(f"O maior peso foi de {maior_peso}Kg. Peso de", end=' ')
for pessoa in lista_principal:
    if pessoa[1] == maior_peso:
        print(f"[{pessoa[0]}]", end=' ')
print()
print(f"O menor peso foi de {menor_peso}Kg. Peso de", end=' ')
for pessoa in lista_principal:
    if pessoa[1] == menor_peso:
        print(f"[{pessoa[0]}]", end=' ')
print()

