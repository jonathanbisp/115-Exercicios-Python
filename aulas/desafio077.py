palavras = ('arroz', 'cachorro', 'bolo', 'amor', 'baixinho', 'cor',
            'beleza', 'olhar', 'suavidadee', 'caneta', 'perfeitos',
            'vaidade', 'existe', 'bateria', 'porco', 'vaca', 'gatinhos')

for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos: ',end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra,end=' ')
    print()