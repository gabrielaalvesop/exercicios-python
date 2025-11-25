from datetime import date

anoatual = date.today().year
nascimento=int(input("Digite seu ano de nascimento: "))
idade=anoatual - nascimento

if idade <=9:
    print(f"Você tem {idade} anos e é um atleta mirim")
elif idade >9 and idade <= 14:
    print(f"Você tem {idade} anos e é um atleta Infantil")
elif idade >14 and idade <= 19:
    print(f"Você tem {idade} anos e é um atleta Junior")
elif idade >19 and idade <= 25:
    print(f"Você tem {idade} anos e é um atleta Sênior")
else:
    print(f"Você tem {idade} anos e é um atleta Master")