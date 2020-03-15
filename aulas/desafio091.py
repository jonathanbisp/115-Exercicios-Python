from random import randint
from time import sleep
from operator import itemgetter

values = dict()
print('Valores sorteados:')
for n in range(1,5):
    values[f'jogador{n}'] = randint(1, 6)
    print(f'O jogador{n} tirou {values[f"jogador{n}"]}')
    sleep(1)
ranking = dict()
ranking = sorted(values.items(), key= itemgetter(1), reverse=True)
print('Ranking dos valores:')
for i,v in enumerate(ranking):
    print(f'{i}° lugar: {v[0]} com {v[1]}.')
    sleep(1)