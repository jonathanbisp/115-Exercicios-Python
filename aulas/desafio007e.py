n = int(input('Digite um número para exibir sua tabuada: '))
print('-='*20)
for elem in range(1,11):
    a = (f'{n} * {f"{elem:0>2}":>2} = {n*elem}')
    print(f'{a:^41}')
print('-='*20)
