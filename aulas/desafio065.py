maior = menor = media = cont = 0
key = ''
while key != 'N':
    num = int(input('Digite um valor: ').strip())
    if cont == 0:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    media += num
    cont += 1
    key = input('Quer continuar [S/N]? ').strip().upper()[0]
media /= cont
print(f'Você digitou {cont} números\nO menor valor foi {menor}\nO maior valor digitado foi {maior}\nA média foi {media}')
