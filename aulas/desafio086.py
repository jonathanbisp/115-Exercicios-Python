matriz = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))

print('=-'*20)

for i in matriz:
    for j in i:
        print(f'[ {j} ]',end=' ')
    print()