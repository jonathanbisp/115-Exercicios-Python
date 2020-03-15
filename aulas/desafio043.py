peso = float(input('Digite o peso em (Kg): ').strip())
altura = float(input('Digite a altura em (m): ').strip())

imc = round(peso/altura**2,1)

if imc > 0:
    print(f'Seu IMC é {imc}. Você está ',end='')
    if imc <= 18.5:
        print('\033[33mABAIXO DO PESO\033[m!!')
    elif imc <= 25:
        print('com \033[32mPESO IDEAL\033[m!!')
    elif imc <= 30:
        print('com \033[33mSOBREPESO\033[m!!')
    elif imc <= 40:
        print('com \033[31mOBESIDADE\033[m!!')
    else:
        print('com \033[31mOBESIDADE MÓRBIDA\033[m!!')
else:
    print('VALORES INVÁLIDOS!!')