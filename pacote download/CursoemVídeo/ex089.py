ficha_do_aluno=list()

while True:
    nome=str(input('Nome: '))
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    media=(nota1+nota2)/2
    ficha_do_aluno.append([nome, [nota1, nota2], media])
    resposta=str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-='*30)
print(f"{'No.':<4} {"Nome":<10}{"Média":>8}")
print('-'*26)
for indice, aluno in enumerate(ficha_do_aluno):
    print(f"{indice:<4} {aluno[0]:<10} {aluno[2]:>8.1f}")
while True:
    print('-'*35)
    opção=int(input("Mostrar notas de qual aluno? [999 para parar] "))
    if opção == 999:
        print('FINALIZANDO...')
        break
    if opção <= len(ficha_do_aluno)-1:
        print(f"Notas de {ficha_do_aluno[opção][0]} são {ficha_do_aluno[opção][1]}")
print("<<<VOLTE SEMPRE>>>")
