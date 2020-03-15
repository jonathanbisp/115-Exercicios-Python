from datetime import date

nascimento = int(input('Ano de nascimento do atleta: ').strip())
anoAtual = date.today().year
idade = anoAtual - nascimento
if 0 > idade > 130:
    print('Idade \033[31minválida\033[m. Tente novamente!')
else:
    if idade <= 9:
        print(f'Com {idade} anos. Você foi classificado na categoria \033[35mMIRIM\033[m!!')
    elif idade <= 14:
        print(f'Com {idade} anos. Você foi classificado na categoria \033[34mINFANTIL\033[m!!')
    elif idade <= 19:
        print(f'Com {idade} anos. Você foi classificado na categoria \033[31mJUNIOR\033[m!!')
    elif idade <= 25:
        print(f'Com {idade} anos. Você foi classificado na categoria \033[32mSÊNIOR\033[m!!')
    else:
        print(f'Com {idade} anos. Você foi classificado na categoria \033[30mMASTER\033[m!!')

