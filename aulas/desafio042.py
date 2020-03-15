l1 = int(input('Digite o tamanho da primeira reta: ').strip())
l2 = int(input('Digite o tamanho da segunda reta: ').strip())
l3 = int(input('Digite o tamanho da terceira reta: ').strip())

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('PODE formar um triângulo!! Do tipo ',end="")
    if l1 != l2 != l3 != l1:
        print('Escaleno.')
    elif l1 == l2 == l3:
        print('Equilátero.')
    else:
        print('Isósceles.')
else:
    print('NÃO PODE formar um triângulo!!')
