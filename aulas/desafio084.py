from isfloat import isfloat

people = []
data = []
maxName = []
minName = []

while True:
    data.append(input('Nome: ').strip())
    weight = input('Peso: ').strip()
    theNumberIsFloat = isfloat(weight)
    while not theNumberIsFloat:
        weight = input('Peso: ').strip()
    data.append(float(weight))

    people.append(data[:])

    data.clear()

    again = input('Quer continuar? [S/N] ').strip()[0].lower()
    while again not in 'ns':
        again = input('Quer continuar? [S/N] ').strip()[0].lower()
    if again == 'n':
        break

lenPeople = len(people)

for n in range(lenPeople):

    if n == 0:
        max = min = people[n][1]
    if max < people[n][1]:
        max = people[n][1]
    if min > people[n][1]:
        min = people[n][1]

for n in range(lenPeople):
    if max == people[n][1]:
        maxName.append(people[n][0][:])
    if min == people[n][1]:
        minName.append(people[n][0][:])
print(f'Ao todo, você cadastrou {lenPeople} pessoas.')
print(f'O maior peso foi de {max:.2f}Kg. Peso de: ',end='')
for n in maxName:
    print(n,end=' ')
print(f'\nO menor peso foi de {min:.2f}Kg. Peso de: ',end='')
for n in minName:
    print(n,end=' ')
