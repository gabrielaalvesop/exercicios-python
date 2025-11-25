soma=0
cont = 0
for c in range(1,7):
    numero=int(input("Digite o {} valor:".format(c)))
    soma+=numero
    cont +=1
print(f"Você informou {cont} números que somados ficam {soma}.")
