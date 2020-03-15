from isfloat import isfloat

totalBuys = timerProduct1000 = cheapValue = timer = 0
cheapName = ''

print('-'*25)
print(f'{"LOJA SUPER BARATÃO":^25}')
print('-'*25)

while True:
    nameOfProduct = input('Nome do produto: ').strip().lower()

    price = input('Preço: R$').strip()
    while not isfloat(price):
        price = input('Preço: R$').strip()
    price = float(price)

    timer += 1
    totalBuys += price
    if timer == 1:
        cheapValue = price
        cheapName = nameOfProduct

    if cheapValue > price:
        cheapValue = price
        cheapName = nameOfProduct

    if price > 1000:
        timerProduct1000 += 1

    again = input('Quer continuar? [S/N] ').strip()[0].upper()
    while again not in 'SN':
        again = input('Quer continuar? [S/N] ').strip()[0].upper()

    if again == 'N':
        print(f'{" FIM DO PROGRAMA ":-^25}')
        print(f'O total da compra foi de R${totalBuys:.2f}')
        print(f'Temos {timerProduct1000} produtos custando mais de R$1000.00')
        print(f'O produto mais barato foi {cheapName.upper()} que custa R${cheapValue:.2f}')
        break
