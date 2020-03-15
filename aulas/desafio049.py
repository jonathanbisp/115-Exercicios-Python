n = int(input('Digite um número para exibir sua tabuada: '))
print('-='*20)
for elem in range(1,11):
    a = (f'{n} x {elem:0>2} = {n*elem:0<2}')
    print(f'{a:^41}')
print('-='*20)
