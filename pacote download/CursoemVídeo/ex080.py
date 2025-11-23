lista=[]
for valor in range(0,5):
    numero=int(input("Digite um valor: "))
    if valor == 0 or numero > lista[-1]:
        lista.append(numero)
        print(f"Valor adicionado ao final da lista")
    else:
        posição=0
        while posição < len(lista):
            if numero<=lista[posição]:
                lista.insert(posição,numero)
                print(f"Valor adicionado na posição {posição}")
                break
            posição+=1
print(f"Os valores digitados em ordem foram {lista}")