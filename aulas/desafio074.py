from random import randint

valores = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print('Os valores sorteados foram: ',end='')
for pos,v in enumerate(valores):
    print(v,end=' ')
    if pos == 0:
        menor = maior = v
    if menor > v:
        menor = v
    if maior < v:
        maior = v
print(f'\nO menor valor sorteado foi {menor}')
print(f'O maior valor sorteado foi {maior}')

print(f'\nO menor valor sorteado foi {min(valores)}')
print(f'O maior valor sorteado foi {max(valores)}')

