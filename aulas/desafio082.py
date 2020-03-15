values = []
even = []
odd = []
while True:
    values.append(int(input('Digite um valor: ').strip()))

    again = input('Quer continuar? [S/N] ').strip()[0].lower()
    while again not in 'sn':
        again = input('Quer continuar? [S/N] ').strip()[0].lower()
    if again == 'n':
        break

values.sort()

for value in values:
    if value % 2 == 0:
        even.append(value)
    else:
        odd.append(value)

print('-='*20)
print(f'A lista completa é {values}')
print(f'A lista de pares é {even}')
print(f'A lista de ímpares é {odd}')
