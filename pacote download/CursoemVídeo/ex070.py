total=tot1000=menor=cont=0
barato=""
while True:
    produto=str(input("Qual o nome do produto: "))
    preco=float(input("Preço: R$ "))
    cont+=1
    total+=preco
    if preco>1000:
        tot1000+=1
    if cont==1 or preco<menor:
        menor=preco
        barato=produto
    resposta= ' '
    while resposta not in "SN":
        resposta=str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resposta == "N":
        break
print("{:^40}".format("FIM DO PROGRAMA"))
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {tot1000} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {barato} que custou R$ {menor:.2f}")