primeiro_numero=int(input("Digite o primeiro número: "))
segundo_numero=int(input("Digite o segundo número: "))
terceiro_numero=int(input("Digite o terceiro número: "))
quarto_numero=int(input("Digite o quarto número: "))

numeros_escolhidos=(primeiro_numero, segundo_numero, terceiro_numero, quarto_numero)
print(numeros_escolhidos)
print(f"O valor 9 apareceu {numeros_escolhidos.count(9)} vezes")
if 3 in numeros_escolhidos:
    print(f"O primeiro valor 3 foi digitado na {numeros_escolhidos.index(3)+1}ª posição")
else:
    print(f"O valor 3 não foi digitado nenhuma vez")
print(f"Os valores pares digitados foram:", end=' ')
for numero_par in numeros_escolhidos:
    if numero_par%2==0:
        print(numero_par)