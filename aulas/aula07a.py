n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))

s = n1 + n2
m = n1*n2
d = n1/n2
di = n1//n2
p = n1**n2

print('A soma é {1}, a Multiplicação é {2}, a potenciação é {0}'.format(p,s,m),end=' ')
print('A divisão é {1:.3f}, a Divisão Inteira é {0}'.format(di,d))