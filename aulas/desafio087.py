matriz = [[], [], []]
even = thirdColumn = biggerValue = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))

print('=-'*20)

for i in matriz:
    for j in i:
        print(f'[ {j} ]',end=' ')
    print()

for posI, i in enumerate(matriz):
    for posJ, j in enumerate(i):
        if j % 2 == 0:
            even+=j
        if posI == 1:
            if posJ == 0 or j > biggerValue:
                biggerValue = j
    thirdColumn += matriz[posI][2]
print('=-'*20)
print(f'A soma dos pares é {even}')
print(f'A soma dos valores da terceira coluna é {thirdColumn}')
print(f'O maior valor da segunda linha é {biggerValue}')

