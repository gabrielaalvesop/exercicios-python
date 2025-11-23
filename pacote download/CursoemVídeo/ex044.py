print("{:=^40}".format(" LOJA DA GABI"))
valor_de_compras=float(input("Digite o valor das compras: R$  "))
print(f'''FORMAS DE PAGAMENTO:
[1] à vista no dinheiro/cheque
[2] à vista no cartao
[3] 2x no cartao
[4] 3x ou mais no cartao''')
opcao=int(input("Qual vai ser a forma de pagamento? "))
if opcao == 1:
    total = valor_de_compras - (valor_de_compras*10/100)
elif opcao == 2:
    total = valor_de_compras - (valor_de_compras*5/100)
elif opcao == 3:
    total = valor_de_compras
    Parcela = total/2
    print(f"Sua compra será parcelada em 2X de R$ {Parcela:.2f}")
elif opcao == 4:
    total = valor_de_compras + (valor_de_compras*20/100)
    total_parcela=int(input('Quantas parcelas? '))
    parcela=total/total_parcela
    print(f"Sua compra será parcelada de {total_parcela} de R$ {parcela:.2f} com juros")
print(f"Sua compra de R$ {valor_de_compras:.2f} vai custar R$ {total:.2f}")


