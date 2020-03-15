n1 = float(input('Digite a primeira nota: ').strip())
n2 = float(input('Digite a segunda nota: ').strip())

m = (n1+n2)/2

print(f'A sua média foi {m:.1f}')

if m>=6.0:
    print('Sua média foi boa! PARABENS!!!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!!')

print('PARABÉNS!!' if m>=6 else 'ESTUDE MAIS!!')