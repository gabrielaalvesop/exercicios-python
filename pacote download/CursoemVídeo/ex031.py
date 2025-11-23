distancia=float(input("Qual a distancia percorrida em km? "))
if distancia <= 200:
    print(f"Sua viagem vai custar R${distancia * 0.50:.2f}")
else:
    print(f"sua viagem vai custar R${distancia * 0.45:.2f}")