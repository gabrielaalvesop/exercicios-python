nota1=float(input("Digite sua primeira nota: "))
nota2=float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f"Você tirou {nota1:.1f} e {nota2:.1f}, sua média é {media:.2f}. Você foi aprovado!")
elif media < 5:
    print(f"Você tirou {nota1:.1f} e {nota2:.1f}, sua média é {media:.2f}. Você foi reprovado!")
else:
    print(f"Você tirou {nota1:.1f} e {nota2:.1f}, sua média é {media:.2f}. Você está de recuperação!")
