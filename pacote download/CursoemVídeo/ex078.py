valores = []

for posição in range(0,5):
    valores.append(int(input(f"Digite um valor para a Posição {posição}: ")))
print(f"Os valores digitados foram {valores}")
print(f"O maior valor digitado foi {max(valores)} na posição {valores.index(max(valores))}.")
print(f"O menor valor digitado foi {min(valores)} na posição {valores.index(min(valores))}.")
