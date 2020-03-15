from time import sleep

opc = 0
while opc != 5:
    n1 = int(input('Primeiro valor: ').strip())
    n2 = int(input('Segundo valor: ').strip())
    while opc < 4:
        print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
        opc = int(input('>>>>>>> Qual é a sua opção? '))

        if opc == 1:
            print(f'A soma entre {n1} + {n2} = {n1+n2}')
        elif opc == 2:
            print(f'A multiplicação entre {n1} x {n2} = {n1*n2}')
        elif opc == 3:
            print(f'O maior entre {n1} e {n2} =', f'{n1}' if n1>n2 else f'{n2}')
        elif opc > 5:
            opc = 0
            print('Opção inválida. Tente novamente!')
        print('=-'*15)
        sleep(1)
print('Fim do programa!!')