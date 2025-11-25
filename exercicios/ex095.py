time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total=int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    partidas.clear()
    for contador in range(0,total):
        partidas.append(int(input(f'Quantos gols na partida {contador+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta=str(input('Deseja continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('-='*40)
print("cod", end=' ')
for indice in jogador.keys():
    print(f'{indice:<13} ', end='')
print()
print('-='*40)
for chave, valor in enumerate (time):
    print(f'{chave:>3} ', end='')
    for dado in valor.values():
        print(f'{str(dado):<13}', end='')
    print()
print('-='*40)
while True:
    busca=int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! Não existe jogador com código {busca}.")
    else:
        print(f"LEVANTAMENTO DO JOGADOR {time[busca]['nome']}")
        for indice, gols in enumerate(time[busca]['gols']):
            print(f'    No jogo {indice+1} fez {gols} gols.')
    print('-='*40)
print('<< VOLTE SEMPRE >>')

