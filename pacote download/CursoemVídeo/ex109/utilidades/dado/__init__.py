def leia_dinheiro(mensagem):
    válido = False
    while not válido:
        entrada = str(input(mensagem)).replace(',', '.')
        if entrada.isalpha()or entrada.strip() == '':
            print(f"\033[0;31mERRO: \'{entrada}\' é um preço inválido!\033[m")
        else:
            válido = True
            return float(entrada)