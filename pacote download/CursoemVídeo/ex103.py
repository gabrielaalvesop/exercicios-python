def ficha(jogador='<desconhecido>', gol=0):
    print(f'O jogador {jogador} fez {gol} gols.')


nome =str(input('Nome do jogador: '))
gols=str(input('Gols: '))
if gols.isnumeric():
    gols=int(gols)
else:
    gols=0
if nome.strip()=='':
    ficha(gol=gols)
else:
    ficha(nome, gols)