maior = 0
menor = 0

for p in range(1,6):
    peso = float(input(f'Digite o peso da {p}° pessoa: '))

    if p == 1:
        menor = peso
        maior = peso
    else:
        if menor > peso:
            menor = peso
        if maior < peso:
            maior = peso

print(f'O menor peso lido foi de {menor}Kg')
print(f'O maior peso lido foi de {maior}Kg')