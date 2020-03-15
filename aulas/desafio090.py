aluno = {}
aluno['Nome'] = input('Nome: ').strip().capitalize()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: ').strip())
aluno['Situção'] = 'Aprovado' if aluno['Média'] >= 7 else \
    'Recuperação' if aluno['Média'] >= 5 else 'Reprovado'

for k,v in aluno.items():
    print(f'{k} é igual a {v}')