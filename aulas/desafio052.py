num = int(input('Digite um número para descobrir se ele é primo: ').strip())
if num == 2:
    print('É PRIMO!!')
elif num%2==0:
    print('NÃO É PRIMO!')
else:
    for n in range(3,num,2):
        if num%n==0:
            print(n)
            break
        elif num == n+2:
            print('É PRIMO!!')