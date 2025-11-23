def leia_numero_inteiro(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except (ValueError, TypeError):
            print(f"\033[31mERRO: por favor, digite um número inteiro válido!\033[m")
            continue
        except (KeyboardInterrupt):
            print(f"\n\033[31mUsuário preferiu não digitar esse número!\033[m")
            return 0
        else:
            return numero

def leia_numero_float(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except (ValueError, TypeError):
            print(f"\033[31mERRO: por favor, digite um número real válido!\033[m")
            continue
        except (KeyboardInterrupt):
            print(f"\n\033[31mUsuário preferiu não digitar esse número!\033[m")
            return 0
        else:
            return numero


numero_1=leia_numero_inteiro("Digite um número inteiro: ")
numero_2=leia_numero_float("Digite um número real: ")
print(f"O valor inteiro difitado foi {numero_1} e o real foi {numero_2}")
