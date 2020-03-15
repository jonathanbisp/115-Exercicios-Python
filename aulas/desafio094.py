pessoas = []
pessoa = {}
average = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ').strip().capitalize()
    pessoa['sexo'] = input('Sexo: [M/F] ').strip()[0].upper()
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = input('Sexo: [M/F] ').strip()[0].upper()
    pessoa['idade'] = int(input('Idade: ').strip())
    average += pessoa['idade']
    pessoas.append(pessoa.copy())
    again = input('Quer continuar? [S/N] ').strip()[0]
    while again not in 'NnSs':
        again = input('Quer continuar? [S/N] ').strip()[0]
    if again in 'Nn':
        break
print('=–'*20)
length = len(pessoas)
print(f'O grupo tem {length} pessoas.')
average = average / length
print(f'A média de idade é de {average:5.2f}')
print('As mulheres cadastradas foram: ',end='')
for pess in pessoas:
    if pess['sexo'] == 'F':
        print(pess['nome'],end=' ')
print('\nLista de pessoas com idade acima da média: ')
for pess in pessoas:
    if pess['idade'] > average:
        for k,v in pess.items():
            print(f'{k} = {v};',end=' ')
        print()
print('<< ENCERRADO >>')