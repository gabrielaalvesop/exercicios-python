print("-=-"*20)
print(f"Analisador de triângulos")
print("-=-"*20)
reta1=float(input("Primeiro segmento: "))
reta2=float(input("Segundo segmento: "))
reta3=float(input("Terceiro segmento: "))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f" Os segmentos acima podem formar um triângulo")
else:
    print(f"Os segmentos acima não podem formar um triângulo")
