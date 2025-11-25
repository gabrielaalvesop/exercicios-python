from time import sleep


def contador(inicio, fim, passo):
    if passo<0:
        passo*=-1
    if passo==0:
        passo=1
    print('-='*20)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    sleep(2.5)

    if inicio<fim:
        contagem = inicio
        while contagem<=fim:
            print(f"{contagem}", end=" ", flush=True)
            sleep(0.5)
            contagem += passo
        print("FIM")
    else:
        contagem=inicio
        while contagem>=fim:
            print(f"{contagem}", end=" ", flush=True)
            sleep(0.5)
            contagem -= passo
        print("FIM")


#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-'*20)
print(f"Agora é sua vez de personalizar a contagem")
iniciar= int(input('Inicio: '))
finalizar = int(input('Fim: '))
passos=int(input('Passo: '))
contador(iniciar, finalizar, passos)
