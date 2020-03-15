from time import sleep

alunos = []
aluno = []
while True:
    aluno.append(input('Nome: ').strip().capitalize())
    aluno.append(round(float(input('Nota 1: ').strip()), 1))
    aluno.append(round(float(input('Nota 2: ').strip()), 1))
    alunos.append(aluno[:])
    aluno.clear()
    again = input('Quer continuar? [S/N] ').strip()[0]
    while again not in 'NnSs':
        again = input('Quer continuar? [S/N] ').strip()[0]
    if again in 'Nn':
        break
print('=–'*11)
print(f'No. {"NOME":<13}MÉDIA')
print('–'*22)
for pos, alun in enumerate(alunos):
    media = round((alun[1] + alun[2])/2,1)
    print(f'{pos:<3} {alun[0]:<13} {media:>4} ')
while True:
    key = int(input('Mostrar notas de qual aluno? (999 interrompe) ').strip())
    if key == 999:
        break
    print(f'Notas de {alunos[key][0]} são [{alunos[key][1]}, {alunos[key][2]}]')
sleep(0.4)
print('FINALIZANDO...')
print("<"*3,"VOLTE SEMPRE",">"*3)