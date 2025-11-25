from random import randint

lista_mega=list()
jogos= list()

print('-='*30)
print('                   JOGO DA MEGA SENA                   ')
print('-='*30)

quantidade_de_jogos=int(input("Quantos jogos você quer que eu sorteie?"))
total=1
while total<=quantidade_de_jogos:
    contador=0
    while True:
        numero=randint(1,60)
        if numero not in lista_mega:
            lista_mega.append(numero)
            contador+=1
        if contador>=6:
            break
    lista_mega.sort()
    jogos.append(lista_mega[:])
    lista_mega.clear()
    total+=1

print('-='*3, f"SORTEANDO{quantidade_de_jogos} JOGOS", '-='*3)
for indice, linha in enumerate(jogos):
    print(f"Jogo {indice+1}: {linha}")