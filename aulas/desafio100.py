from time import sleep
from random import randint


def sorteia(lst):
    print('Sorteando 5 valores da lista: ',end='')
    for n in range(0,5):
        lst.append(randint(0,10))
        print(lst[n],end=' ')
        sleep(0.3)
    print('PRONTO!')

def somaPar(lst):
    sorteia(lst)
    total = 0
    for n in lst:
        if n%2 == 0:
            total += n
    print(f'A soma dos valores pares de {lst} é {total}')


números = []
somaPar(números)

