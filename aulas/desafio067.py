while True:
    valor = int(input('Quer ver a tabuada de qual valor? ').strip())
    print('-'*37)

    if valor < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break

    for i in range(1,11):
        print(f'{valor} x {i:0>2} = {valor*i}')
    print('-' * 37)