from datetime import date

anoAtual = date.today().year
anoNascimento: int = 0
cont: int = 0
control: int = 0

for x in range(1, 8):
    anoNascimento = int(input(f'Digite o ano de nascimento da {x}° pessoa: ').strip())
    if (anoAtual - anoNascimento) > 130 or (anoAtual - anoNascimento) < 0:
        print('IDADE INVÁLIDA. TENTE NOVAMENTE!.')
        control = 1
        break
    elif anoAtual - anoNascimento > 20:
        cont += 1
if control == 0:
    print(f'Das 7 pessoas {cont} são maiores de idade e {7 - cont} são menores')
