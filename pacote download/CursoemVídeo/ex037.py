numero=int(input("Qual o número inteiro escolhido?"))
print(f'''Escolha uma das bases para conversão:
[1] para binário
[2] para octal
[3] para hexadecimal''')
opcao=int(input("Escolha uma opção: "))
if opcao == 1:
    print(f"{numero} convertido para binário é igual a {bin(numero)[2:]}")
elif opcao == 2:
    print(f"{numero} convertido para octal é igual a {oct(numero)[2:]}")
elif opcao == 3:
    print(f"{numero} convertido para hexadecimal é igual a {hex(numero)[2:]}")
else:
    print(f"Opção inválida")