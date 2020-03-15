def leiaInt(txt):
    while True:
        value = input(txt).strip()
        if value.isdecimal():
            value = int(value)
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return value


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar um número {n}')