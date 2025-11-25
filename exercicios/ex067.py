while True:
    numero=int(input("Quer ver a tabuada de qual valor? "))
    if numero<0:
        break
    print("-"*30)
    for c in range(1,11):
        print(f"{c} x {numero} = {c*numero}")
print("PROGRAMA ENCERRADO")
print("-"*30)