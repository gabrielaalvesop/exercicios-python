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


def linha(tam=42):
    return "-" * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    contador = 1
    for item in lista:
        print(f"\033[33m{contador}\033[m - \033[034m{item}\033[m")
        contador += 1
    print(linha())
    opcao=leia_numero_inteiro("\033[32mSua opção: \033[m")
    return opcao