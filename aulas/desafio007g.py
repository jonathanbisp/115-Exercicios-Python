from math import ceil
l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))

print(f'A área da parede é {l*a}m^2, e precisa de {ceil((l*a)/2)}l de tinta')