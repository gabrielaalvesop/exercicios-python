nome=str(input("Digite seu nome: ")).strip()
print(f"seu nome é {nome}")
print(f"seu nome com todas as letras maiúsculas é {nome.upper()}")
print(f"seu nome com todas as letras minusculas é {nome.lower()}")
print(f"seu nome ao todo tem {len(nome)-nome.count(" ")}")
print(f"Seu primeiro nome tem {nome.find(' ')}")


