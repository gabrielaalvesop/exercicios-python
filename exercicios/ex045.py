from random import randint
from time import sleep


itens=("Pedra", "Papel", "Tesoura")
computador=randint(0,2)

print(f'''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador=int(input("Qual a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print('-='*11)
print(f"O computador escolheu {itens[computador]}")
print(f"O jogador escolheu {itens[jogador]}")
print('-='*11)

if computador == 0: #computador jogou Pedra
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA")