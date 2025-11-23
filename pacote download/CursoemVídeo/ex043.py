peso=float(input("Qual é seu peso (kg)"))
altura=float(input("Qual é sua altura (m)"))
IMC = peso/(altura**2)
if IMC < 18.5:
    print(f"O IMC dessa pessoa é de {IMC:.2f}", end=" ")
    print(". Essa pessoa está Abaixo do peso")
elif IMC >= 18.5 and IMC < 25:
    print(f"O IMC dessa pessoa é de {IMC:.2f}", end=" ")
    print(". Essa pessoa está no peso ideal")
elif IMC >= 25 and IMC < 30:
    print(f"O IMC dessa pessoa é de {IMC:.2f}", end=" ")
    print(". Essa pessoa está no sobrepeso")
elif IMC >= 30 and IMC < 40:
    print(f"O IMC dessa pessoa é de {IMC:.2f}", end=" ")
    print(". Essa pessoa está na obesidade")
else:
    print(f"O IMC dessa pessoa é de {IMC:.2f}", end=" ")
    print(". Essa pessoa está na obesidade mórbida")