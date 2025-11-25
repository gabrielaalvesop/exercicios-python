def leia_numero_inteiro(mensagem):
    valido = False
    valor = 0
    while True:
        numero=str(input(mensagem))
        if numero.isnumeric():
            valor = int(numero)
            valido = True
        else:
            print(f"\033[0;31mERRO! Digite um número inteiro válido.\033[m")
        if valido:
            break
    return valor


numero=leia_numero_inteiro("Digite um número: ")
print(f"Você acabou de digitar o número {numero}.")