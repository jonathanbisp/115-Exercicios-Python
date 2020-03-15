valores = []

for n in range(0, 3):
    valor = int(input('Digite um valor: '))
    while True:
        if valor in valores:
            valor = int(input('Valor já adicionado. Digite um valor: '))
        else:
            break

    if n == 0:
        valores.append(valor)
        print('Primeiro elemento! Adicionado ao começo da lista...')
    elif valor >= valores[-1]:
        valores.append(valor)
        print('Adicionado ao final da lista...')
    else:
        for i in valores:
            if valor < i:
                pos = valores.index(i)
                valores.insert(pos,valor)
                print(f'Adicionado na posição {pos} da lista...')
                break

print('=-'*30,f'\nOs valores digitados em ordem foram {valores}')