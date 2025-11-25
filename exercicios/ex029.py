carro=float(input("Qual a sua velocidade em Km/h? "))
multa= (carro-80)*7
if carro > 80:
    print(f"você foi mutado em R${multa:.2f}")
else:
    print(f"Tenha um bom dia e dirija com segurança")