import numpy


def teste(b):
    a = 3
    b += 4
    print(f'A dentro valo {a}')
    print(f'B dentro valo {b}')
    return b


a = 5
print(f'A fora vale {a}')
a = teste(a)
print(f'A fora vale {a}')
