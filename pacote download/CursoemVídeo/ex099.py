from time import sleep

def maior(*numero):
    contador=maior=0
    print('-='*20)
    print(f"\nAnalisando os valores passados...")
    for valor in numero:
        print(f"{valor}", end=" ", flush=True)
        sleep(0.3)
        if contador==0:
            maior=valor
        else:
            if valor > maior:
                maior=valor
        contador+=1
    print(f"Foram informados {contador} valores")
    print(f"O maior valor informado foi {maior}")


#Programa principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()