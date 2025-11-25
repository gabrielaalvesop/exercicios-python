times_brasileirao=('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Botafogo',
                   'Bahia', 'Fluminense', 'São Paulo', 'Vasco', 'Bragantino',
                   'Corinthians', 'Grêmio', 'Ceará', 'Internacional', 'Atlético-MG',
                   'Santos', 'Vitória', 'Fortaleza', 'Juventude', 'Sport')

print("="*30)
print(f"TIMES BRASILEIRAO:{times_brasileirao}")
print("="*30)
print(f"Os 5 primeiros são: {times_brasileirao[:5]}")
print("="*30)
print(f"Os 4 últimos são: {times_brasileirao[-4:]}")
print("="*30)
print(f" Times em ordem alfabetica: {sorted(times_brasileirao)}")
print("="*30)
print(f'O Atlético-MG está na {times_brasileirao.index("Atlético-MG")+1}ª posição')