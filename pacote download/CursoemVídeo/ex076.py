print('='*40)
print(f'{"LISTA DE SUPERMERCADO":^40}')
print('='*40)

lista_de_produtos=("Pão", 5,
                   "Carne", 45.90,
                   'Queijo', 10.89,
                   'Saco de Lixo', 6.50)

for posicao_do_produto in range(0, len(lista_de_produtos)):
    if posicao_do_produto%2==0:
        print(f'{lista_de_produtos[posicao_do_produto]:.<30}', end=' ')
    else:
        print(f"R$ {lista_de_produtos[posicao_do_produto]:>5.2f}")
print('='*40)