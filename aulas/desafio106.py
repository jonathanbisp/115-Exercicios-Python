from time import sleep


def imprimirTitulo(txt, cor='\033[m'):
    tam = len(txt) + 4
    print(f'{cor}',end='')
    print('~' * tam)
    print(f'  {txt}')
    print(f'~' * tam)
    print('\033[m',end='')

while True:
    imprimirTitulo('SISTEMA DE AJUDA PyHELP', cor='\033[42m')
    buscarComando = input('Função ou Biblioteca > ').strip().lower()
    if buscarComando == 'fim':
        imprimirTitulo('ATÉ LOGO!','\033[41m')
        break
    imprimirTitulo(f'Acessando o manual do comando "{buscarComando}"', cor='\033[44m')
    sleep(1)
    print('\033[7m')
    help(buscarComando)
    print('\033[m', end='')
    sleep(2)


