numero1=int(input("primeiro numero? "))
numero2=int(input("segundo numero? "))
numero3=int(input("terceiro numero? "))
if numero1 >= numero2 and numero1 >= numero3:
    print(f"O número maior é {numero1}")
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"O número maior é o {numero2}")
else:
    print(f"O número maior é o {numero3}")
if numero1 <= numero2 and numero1 <= numero3:
    print(f"O menor número é {numero1}")
elif numero2 <= numero1 and numero2 <= numero3:
    print(f"O menor número é {numero2}")
else:
    print(f"O menor número é {numero3}")
