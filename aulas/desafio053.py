frase = input('Digite uma frase: ').strip().lower()
fraseAjustada = ''.join(frase.split())
fraseInversa = fraseAjustada[::-1]

print(f'O inverso de {fraseAjustada} é {fraseInversa}!')

if fraseAjustada == fraseInversa:
    print(f'Portanto, \033[4m{frase.capitalize()}\033[m \nÉ UM PALÍNDROMO.')
else:
    print(f'Portanto, \033[4m{frase.capitalize()}\033[m \nNÃO É UM PALÍNDROMO.')
