def leiaInt(txt):
    while True:
        try:
            value = int(input(txt).strip())
            return value
        except:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


def leiaFloat(txt):
    while True:
        try:
            value = float(input(txt).strip())
            return value
        except:
            print('\033[31mERRO! Digite um número real válido.\033[m')


i = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar um número {i} e {r}')