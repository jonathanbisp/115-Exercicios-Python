n = int(input('Digite um número: ').strip())
timer: int = 0
for x in range(1,n+1):
    if n % x == 0:
        print(f'\033[33m{x}\033[m',end=' ')
        timer +=1
    else:
        print(f'\033[31m{x}\033[m',end=' ')
print(f'\nO número {n} foi divisível {timer} vezes')
if timer == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
