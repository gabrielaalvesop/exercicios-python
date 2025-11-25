valores = []
while True:
    numero = int(input("Digite um valor: "))
    if numero not in valores:
        valores.append(numero)
        print("Valor adicionado com sucesso!")
    else:
        print("Esse valor já foi adicionado, Por isso não vamos adicionar...")
    resp = input("Deseja continuar? [S/N] ")
    if resp in "Nn":
         break
valores.sort()
print(f"Os valores digitados foram {valores}")
