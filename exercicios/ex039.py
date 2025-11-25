from datetime import date
nascimento = int(input("Digite o ano de nascimento: "))
atual = date.today().year
idade = atual - nascimento
print(f"Quem nasceu em {nascimento} tem {idade} anos em {atual}.")
if idade == 18:
    print(f"você tem que se alistar imediatamente!")
elif idade < 18:
    print(f"Você ainda não precisa se alistar, falta {18 - idade} anos.!")
else:
    print(f"Você já deveria ter se alistado a {idade - 18} anos.!")