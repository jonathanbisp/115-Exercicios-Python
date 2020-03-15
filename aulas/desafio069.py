timerAge = timerMan = timerWomanLessThan20 = 0

print(f'{" START OF PROGRAM ":=^26}')

while True:
    print('-'*25)
    print(f'{"CADASTRE UMA PESSOA":^25}')
    print('-'*25)

    age = input('Idade: ').strip()
    while not age.isnumeric():
        age = input('Idade: ').strip()
    age = int(age)

    sex = input('Sexo: [M/F] ').strip()[0].upper()
    while sex not in 'MF':
        sex = input('Sexo: [M/F] ').strip()[0].upper()

    if age > 18:
        timerAge += 1
    if sex == 'M':
        timerMan += 1
    if age < 20 and sex == 'F':
        timerWomanLessThan20 += 1

    print('-'*25)

    again = input('Quer continuar? [S/N] ').strip()[0].upper()
    while again not in 'SN':
        again = input('Quer continuar? [S/N] ').strip()[0].upper()

    if again == 'N':
        print(f'{" END OF PROGRAM ":=^26}')
        print(f'Total de pessoas com mais de 18 anos: {timerAge}.')
        print(f'Ao todo temos {timerMan} homens cadastrados.')
        print(f'E temos {timerWomanLessThan20} com menos de 20 anos.')
        break