p=float(input("Qual o preço do produto?R$"))
d=p*5/100
np=p-d
print(f"O novo preço com o desconto de R${d:.2f} é de R${np:.2f}")
