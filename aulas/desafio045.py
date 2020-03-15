from time import sleep
from random import choice
opc = (['PEDRA', 'PAPEL', 'TESOURA'])
print('{:=^40}'.format('JO KEN PO'))
print('{:=^40}'.format('THE GAME'))
jogador = input('PEDRA PAPEL OU TESOURA: ').strip().upper()
maquina = choice(opc)
if jogador in opc:
    print('JO') ; sleep(1); print('KEN'); sleep(1); print('PO'); sleep(1)

    print('-=' * 15);
    print(f'JOGADOR ESCOLHEU {jogador}.')
    print(f'COMPUTADOR ESCOLHEU {maquina}.')
    print('-=' * 15)

    if maquina == jogador:
        print('EMPATOU')

    elif (maquina == 'PEDRA' and jogador == 'PAPEL') or (maquina == 'TESOURA' and jogador == 'PEDRA') or (
            maquina == 'PAPEL' and jogador == 'TESOURA'):
        print('VOCÊ GANHOU!!')

    elif (maquina == 'PEDRA' and jogador == 'TESOURA') or (maquina == 'PAPEL' and jogador == 'PEDRA') or (
            maquina == 'TESOURA' and jogador == 'PAPEL'):
        print('EU GANHEI HAHAHAHA!!')
else:
    print('\033[31mOPÇÃO INVÁLIDA!!\033[m')