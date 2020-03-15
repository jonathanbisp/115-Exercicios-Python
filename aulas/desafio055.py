pes = ''

for pess in range(1,6):
    pes += str(float(input(f'Digite o peso da {pess}° pessoa (Kg): ').strip())) + ' '

pes = sorted(pes.split())

print(f'O menor peso foi {pes[0]}Kg. O maior peso foi {pes[-1]}kg')