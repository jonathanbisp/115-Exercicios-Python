from time import sleep


def contador(inicio, fim, passo = 0):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *=-1
    auxPasso = passo
    auxFim = fim
    if inicio > fim:
        passo = passo*-1
        fim -= 1
    else:
        fim += 1
    print('–=' * 20)
    print(f'Contagem de {inicio} até {auxFim} de {auxPasso} em {auxPasso}:')
    for n in range(inicio, fim, passo):
        print(n, end=' ')
        sleep(0.3)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('–='*20)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Ínicio: ')), int(input('Fim: ')), int(input('Passo: ')))
