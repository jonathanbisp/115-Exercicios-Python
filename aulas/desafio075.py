fourValues = (int(input('Primeiro valor: ')),int(input('Segundo valor: ')),
              int(input('Terceiro valor: ')),int(input('Quarto valor: ')))

print(f'O valor 9 apareceu {fourValues.count(9)} vezes')
if 3 in fourValues:
    print(f'O valor 3 apareceu na posição {fourValues.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
par=0
for value in fourValues:
    if value%2 == 0:
        par+=1
print(f'Os valores pares digitados foram {par}')