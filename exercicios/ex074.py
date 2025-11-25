from random import randint

numero_escolhido = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f"Os números sorteados foram: ")

for numero in numero_escolhido:
    print(numero, end=' ')
print(f"\nO maior número sorteado foi {max(numero_escolhido)}")
print(f"O menor número sorteado foi {min(numero_escolhido)}")