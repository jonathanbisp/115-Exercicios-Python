num = int(input('Digite um número para calcular seu fatorial: ').strip())
total = 1
print(f'Calculando {num}! = ', end='')
while num != 0:
    print(f'{num}','x ' if num != 1 else '', end='')
    total *= num
    num -=1
print('=',total)