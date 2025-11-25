def área(largura, comprimento):
    area = largura * comprimento
    print(f"A área de um terreno {largura} X {comprimento} é de {area}m2")


#Programa principal
print("CONTROLE DE TERRENOS")
print('-'*20)
larg=float(input('Largura (m): '))
comp=float(input('Comprimento (m): '))
print('-'*20)
área(larg,comp)
print('-'*20)
