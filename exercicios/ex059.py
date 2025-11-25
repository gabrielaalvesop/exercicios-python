numero1=int(input("Digite o primeiro valor: "))
numero2=int(input("Digite o segundo valor: "))
opcao=0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opcao=int(input("Digite a opção escolhida: "))
    if opcao == 1:
        soma = numero1 + numero2
        print(f"A soma entre {numero1} e {numero2} é {soma}")
    elif opcao == 2:
        multiplicacao = numero1 * numero2
        print(f"O resultado de {numero1} X {numero2} é {multiplicacao}")
    elif opcao == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print(f"Entre {numero1} e {numero2} o maior valor é {maior}")
    elif opcao == 4:
        print(f"Informe os números novamente:")
        numero1 = int(input("Digite o primeiro valor: "))
        numero2 = int(input("Digite o segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print(f"Opção inválida. Tente novamente.")
    print("=-="*10)
print(f" Fim do programa. Volte sempre!")