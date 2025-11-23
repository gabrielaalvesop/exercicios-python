valor=float(input("Qual o valor da casa? R$ "))
salario = float(input("Qual o salario do comprador? R$ "))
tempo=int(input("Em quantos anos vai pagar? "))
prestacao=valor/(tempo*12)
if prestacao<=salario*0.3:
    print(f"Para pagar uma casa de R${valor:.2f} em {tempo} anos a prestação será de R${prestacao:.2f}, então o empréstimo foi aprovado.")
else:
    print(f"Para pagar uma casa de R${valor:.2f} em {tempo} anos a prestação será de R${prestacao:.2f}, então o empréstimo foi NEGADO.")