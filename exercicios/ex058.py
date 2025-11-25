from random import randint

computador= randint(0, 10)
print(f"-=-"*20)
print(f"Vou pensar em um número entre 0 e 10. Tente adivinhar qual foi")
print(f"-=-"*20)
acertou= False
palpites=0
while not acertou:
    jogador=int(input("Qual o seu palpite? "))
    palpites=palpites+1
    if jogador == computador:
        acertou=True
    else:
        if jogador < computador:
            print("Mais... Tente novamente.")
        elif jogador > computador:
            print("Menos... Tente novamente.")
print(f"acertou com {palpites} tentativas!")
