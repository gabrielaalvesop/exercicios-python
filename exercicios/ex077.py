palavras=("Laranja", "Vermelho", "Verde", "Biscoito", "Marmita")

for palavra in palavras:
    print(f"\nNa palavra {palavra} temos ", end='')
    for vogal in palavra:
        if vogal.lower() in "aeiou":
            print(vogal, end=' ')