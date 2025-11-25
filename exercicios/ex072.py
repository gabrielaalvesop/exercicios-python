numeros_extenso=('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
                 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
                 'desesseis', 'desete', 'desoito', 'desenove', 'vinte')

while True:
    numero_escolhido=int(input("Digite um número entre 0 e 20: "))
    if numero_escolhido in range(0, 21):
        break
    else:
        print("Tente novamente.", end=' ')
print(f"Você digitou o número {numeros_extenso[numero_escolhido]}")