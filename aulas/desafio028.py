from random import randint
from time import sleep

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)

val = int(input('Em que número eu pensei?').strip())

print('PROCESSANDO...')
sleep(2)

n = randint(0,5)

if val == n:
    print(f'PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no {n} e não no {val}!')