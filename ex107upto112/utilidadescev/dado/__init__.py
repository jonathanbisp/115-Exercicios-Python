from aulas.isfloat import isfloat


def leiaDinheiro(txt):
    while True:
        num = input(txt).strip().split(',')
        num = '.'.join(num)
        if isfloat(num):
            num = float(num)
            break
        else:
            print(f'\033[31mERRO: "{num}" é um preço inválido!\033[m"')
    return num
