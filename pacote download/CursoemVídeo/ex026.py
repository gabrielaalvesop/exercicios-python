frase=str(input("Digite uma frase: ")).strip()
print(f"A letra A aparece {frase.lower().count("a")} vezes")
print(f"A letra A aparece na posição {frase.lower().find("a")+1} na primeira vez")
print(f"A letra A aparece na posição {frase.rfind("a")+1} na última vez")