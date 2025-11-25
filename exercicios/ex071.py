print("="*30)
print("{:^30}".format("BANCO CEV"))
print("="*30)

valor_saque=int(input("Que valor você quer sacar? R$ "))
maior_cedula=50
quantidade_notas=0

while True:
    if valor_saque>=maior_cedula:
        valor_saque-=maior_cedula
        quantidade_notas+=1
    else:
        if quantidade_notas>0:
            print(f"Total de {quantidade_notas} cédulas de R$ {maior_cedula:.2f}")
        if maior_cedula==50:
            maior_cedula=20
        elif maior_cedula==20:
            maior_cedula=10
        elif maior_cedula==10:
            maior_cedula=1
        quantidade_notas=0
        if valor_saque==0:
            break
print("="*30)
print(f" VOLTE SEMPRE AO BANCO CEV")