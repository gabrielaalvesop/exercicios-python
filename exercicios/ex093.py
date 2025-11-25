jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
total=int(input(f'Quantas partidas {jogador["nome"]} jogou? : '))

for contador in range(0,total):
    partidas.append(int(input(f'Quantos gols na partida {contador+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}')
print('-='*30)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
for indice, valores in enumerate(jogador['gols']):
    print(f'Na partida {indice+1}, fez {valores} gols.')
print(f'Foi um total de {jogador["total"]} gols.')