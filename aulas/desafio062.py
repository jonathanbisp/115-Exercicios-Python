pt = int(input('Digite o primeiro termo da PA: ').strip())
razão = int(input('Digite a razão da PA: ').strip())

contador = 0
max = 9
valor = 1
while valor != 0:
    max +=valor
    while contador < max:
        contador += 1
        print(pt, end=" ←→ ")
        pt = pt + razão
    print('PAUSA')
    valor = int(input('Quantos termos você quer mostrar a mais? ').strip())
print(f'Progressão finalizada com {max} termos mostrados.')
