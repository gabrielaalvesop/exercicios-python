import math
angulo=float(input("Dugute o angulo que você deseja: "))
seno=math.sin(math.radians(angulo))
print(f"O angulo de {angulo} tem o seno de {seno:.2f}")
cosseno=math.cos(math.radians(angulo))
print(f"O angulo de {angulo} tem o cosseno de {cosseno:.2f}")
tangente=math.tan(math.radians(angulo))
print(f"O angulo de {angulo} tem a tangente de {tangente:.2f}")

