valores = []

for n in range(0,5):
    valores.append(int(input(f'Digite um valor para adicionar na posição {n}: ').strip()))

print('=-'*30)
print(f'Você digitou os valores{valores}')

maior = max(valores)
index = 0
print(f'O maior valor digitado foi {maior} nas posiçôes ',end='')
for c in range(0, valores.count(maior)):
    aux = valores.index(maior,index)
    print(f'{aux}...',end=' ')
    index = aux+1

menor = min(valores)
index = 0
print(f'\nO menor valor digitado foi {menor} nas posições ',end='')
for c in range(0, valores.count(menor)):
    aux = valores.index(menor,index)
    print(f'{aux}... ',end='')
    index = aux+1
