from random import randint
from time import sleep
from os import system

venceu = contador = 0

while venceu != 1:
    print('-=-'*20)
    print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
    print('-=-'*20)

    val = int(input('Em que número eu pensei? ').strip())

    print('PROCESSANDO...')
    sleep(1)

    n = randint(0,10)

    contador+=1
    if val == n:
        print(f'Eu pensei no {n} e você no {val}!')
        print(f'PARABÉNS! Você conseguiu me vencer!')
        venceu = 1
        sleep(2.5)
    else:
        print(f'GANHEI! Eu pensei no {n} e não no {val}!')
        sleep(1.5)
    system("cls")
print(f'Tentativas usadas: {contador}')
a = input('Aperte qualquer tecla para fechar...')
