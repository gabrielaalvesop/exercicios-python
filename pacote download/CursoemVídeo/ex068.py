from random import randint
v=0
while True:
    jogador=int(input("Digite um valor: "))
    computador=randint(0,11)
    total=jogador+computador
    tipo= ' '
    while tipo not in 'PI':
        tipo=str(input("Par ou ímpar? [P/I] ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador {computador} e o total {total}")
    print(f"Deu par " if total %2==0 else "Deu impar ", end="")
    if tipo == 'P':
        if jogador == computador:
            print(f"você venceu")
            v+=1
        else:
            print(f"você perdeu")
            break
    elif tipo == 'I':
        if total%2==1:
            print(f"você venceu")
            v+=1
        else:
            print(f"você Perdeu")
            break
    print(f"Vamos jogar novamente...")
print(f"GAME OVER! Você venceu {v} vezes")
