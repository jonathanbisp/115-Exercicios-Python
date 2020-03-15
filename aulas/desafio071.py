value = int(input('Que valor você quer sacar? R$').strip())
fifty = twenty = ten = one = 0

while True:
    if value >= 50:
        value -= 50
        fifty += 1
    else:
        break
while True:
    if value >= 20:
        value -= 20
        twenty += 1
    else:
        break
while True:
    if value >= 10:
        value -= 10
        ten += 1
    else:
        break
while True:
    if value >= 1:
        value -= 1
        one += 1
    else:
        break
print(f'Total de {fifty} cédulas de R$50.00')
print(f'Total de {twenty} cédulas de R$20.00')
print(f'Total de {ten} cédulas de R$10.00')
print(f'Total de {one} cédulas de R$1.00')
