from random import randint

cont = 0

print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')

while True:

    print('-='*15)

    jogador = int(input('Diga um valor: ').strip())
    pOri = ' '

    while pOri not in 'PI':
        pOri = input('Par ou Ímpar [P/I]? ').strip().upper()[0]

    computador = randint(0, 10)
    total = jogador + computador

    result = bool(total%2 == 0)

    print('-'*30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} {"DEU PAR" if result else "DEU ÍMPAR"}')
    print('-' * 30)

    if (result and pOri == 'P') or (not result and pOri == 'I'):
        print('Você VENCEU!\nVamos jogar novamente...')
        cont+=1
    else:
        print('Você PERDEU!')
        print('=-'*15)
        print(f'GAME OVER! Você venceu {cont} vezes.')
        break
