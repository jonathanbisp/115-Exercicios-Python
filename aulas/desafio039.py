from datetime import date

sexo = input('Digite seu sexo (M) ou (F):').strip().upper()

if sexo == "M":
    nascimento = int(input('Digite o ano do seu nascimento: ').strip())

    anoAtual = date.today().year

    if nascimento > anoAtual:
        print('Data inválida. Tente novamente!')
    else:
        idade = anoAtual - nascimento
        if idade == 18:
            print('É hora de se alistar. Você tem exatamente 18 anos, a idade certa!')
        elif idade < 18:
            print(f'Ainda não é hora de se alistar. Você tem apenas {idade} anos')
            if abs(idade - 18) == 1:
                print(f'Faltando assim \033[4;31m{abs(idade - 18)} ano\033[m para o momento de se alistar.')
            else:
                print(f'Faltando assim \033[4;31m{abs(idade - 18)} anos\033[m para momento de se alistar.')

        else:
            print(f'Já passou da hora de se alistar. Você já tem {idade} anos')
            if abs(idade - 18) == 1:
                print(f'Portanto já passou \033[4;31m{abs(idade - 18)} ano\033[m do momento de se alistar.')
            else:
                print(f'Portanto já passaram \033[4;31m{abs(idade - 18)} anos\033[m do momento de se alistar.')
else:
    print('Para você o alistamento NÃO é obrigátorio!!')