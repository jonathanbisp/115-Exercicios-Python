values = []
while True:
    values.append(int(input('Digite um valor: ').strip()))
    again = input('Deseja continuar? [S/N] ').strip()[0].upper()
    while again not in 'SN':
        again = input('Deseja continuar? [S/N] ').strip()[0].upper()
    if again in 'N':
        break
reversedValues = sorted(values, reverse=True)
fiveInValues = 5 in values

print(f'Você digitou {len(values)} elementos.')
print(f'Os valores em ordem decrescente são {reversedValues}')

if fiveInValues:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 NÃO está na lista!')