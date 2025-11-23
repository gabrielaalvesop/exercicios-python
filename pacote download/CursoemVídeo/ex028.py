from random import randint
from time import sleep

computador= randint(0, 5)
print(f"-=-"*20)
print(f"Vou pensar em um número entre 0 e 5. Tente adivinhar qual foi")
print(f"-=-"*20)
jogador=int(input("Em que núemro eu pensei? "))
print("PROCESSANDO...")
sleep(2)
if jogador == computador:
    print(f"Você venceu!!")
else:
    print(f"Você perdeu!! Eu pensei no número {computador} e não no {jogador} ")


