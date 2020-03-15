from time import sleep


def maior(*num):
    print('–='*30)
    print(f'Analisando os valores passados...')
    for n in num:
        print(n, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) > 0:
        maior = num[0]
        for pos, n in enumerate(num):
            if maior < n:
                maior = n
        print(f'O maior valor informado foi {maior}.')
    else:
        print('Você não informou nenhum valor.')
    sleep(1)


maior(500, 5, 7, 11, -1, 5)
maior(2, 3, 5)
maior(5)
maior()