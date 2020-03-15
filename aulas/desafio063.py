f1 = f2 = aux = 0
n = int(input('Quantos termos deseja ver da sequência de Fibonacci? ').strip())

if n == 1:
    print('0')
elif n == 2:
    print('0 ←→ 1')
else:
    while n > 0:
        print(f1,end='')
        if n != 1:
            print(' ←→ ',end='')
        aux = f1
        f1 = f2
        f2 = aux + f2
        n-=1
print(' ←→ ACABOU!!')
