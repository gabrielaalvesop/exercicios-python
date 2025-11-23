primeiro=int(input("Digite o primeiro termo da PA: "))
razao=int(input("Razão da PA: "))
termo=primeiro
cont= 1

while cont <=10:
    print(f"{termo} -> ", end="")
    termo += razao
    cont += 1