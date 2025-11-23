salario=float(input("Qual o salário do funcionário? R$"))
if salario <= 1250:
    print(f"O salario passa a ser de {salario*1.15:.2f}")
else:
    print(f"O salario passa a ser de {salario*1.10:.2f}")
