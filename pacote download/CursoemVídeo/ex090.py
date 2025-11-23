aluno = dict()
aluno ['nome']=str(input("Nome: "))
aluno ['média']=float(input(f"Média de {aluno['nome']}: "))

if aluno['média'] >= 7:
    aluno['situação']='aprovado'
elif 5 <= aluno ['média'] <7:
    aluno['situação']='Recuperação'
else:
    aluno['situação']='Reprovado'

for keys, valores in aluno.items():
    print(f"{keys}: {valores}")