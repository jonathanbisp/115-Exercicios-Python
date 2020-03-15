even_and_odd = [[],[]]

for n in range(1,8):
    value = int(input(f'Digite o {n}° valor: ').strip())
    even_and_odd[value % 2].append(value)
    even_and_odd[value % 2].sort()
print(f'Os valores pares digitados foram {even_and_odd[0]}')
print(f'Os valores ímpares digitados foram {even_and_odd[1]}')