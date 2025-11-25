l=float(input("Qual a largura da parede?"))
a=float(input("Qual a altura da parede?"))
area=l*a
print(f"A largura da parede é de {l:.0f}m. \nA altura da parede é de {a:.0f}m. \nA área total é de {area:.1f}m².")
tinta=area/2
print(f"Para pintar essa parede você precisará de {tinta:.1f}l de tinta.")
