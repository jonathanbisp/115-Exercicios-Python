from time import sleep

print(f'{"CONTAGEM REGRESSIVA":=^41}')
print(f'{"PARA":=^40}=')
print(f'{"OS FOGOS":=^40}=')

for n in range(10, -1, -1):
    print(f'{f"{n:0>2}":=^41}')
    sleep(1)
print('POW POW PLAM BOOM!!')