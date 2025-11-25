expressao=str(input("Digite uma Expressão: "))
lista=[]
for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print("Sua exprssão é válida")
else:
    print("Sua expressão está incorreta!")