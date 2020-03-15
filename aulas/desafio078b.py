valores = []
lstMaior = []
lstMenor = []
for n in range(0,5):
    valores.append(int(input(f'Digite um valor para adicionar na posição {n}: ').strip()))

print('=-'*30)
print(f'Você digitou os valores{valores}')

for pos,n in enumerate(valores):
    if n == max(valores):
        lstMaior.append(pos)
    if n == min(valores):
        lstMenor.append(pos)

print(f'O maior valor digitado foi {max(valores)} nas posiçôes ',end='')
for n in lstMaior:
    print(f'{n}... ',end='')

print(f'\nO menor valor digitado foi {min(valores)} nas posiçôes ',end='')
for n in lstMenor:
    print(f'{n}... ',end='')