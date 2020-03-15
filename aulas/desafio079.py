valores = []

while True:
    valor = int(input('Digite um valor: ').strip())
    if valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(valor)
        print('Valor adicionado com sucesso...')

    stopCondition = input('Quer continuar? [S/N] ').strip()[0].lower()
    while stopCondition not in 'sn':
        stopCondition = input('Quer continuar? [S/N] ').strip()[0].lower()
    if stopCondition == 'n':
        break
print('=-'*20)
print('Você digitou valores: ',end='')
valores.sort()
for valor in valores:
    print(valor,end=' ')