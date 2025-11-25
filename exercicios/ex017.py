from math import hypot
cateto_oposto=float(input("comprimento do cateto oposto: "))
cateto_adjacente=float(input("Comprimento do cateto adjacente: "))
hi=hypot(cateto_oposto,cateto_adjacente)
print (f" A hipotenusa vai medir {hi:.2f}")

