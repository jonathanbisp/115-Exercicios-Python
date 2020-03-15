r1 = float(input('Digite o tamanho da primeira reta: ').strip())
r2 = float(input('Digite o tamanho da segunda reta: ').strip())
r3 = float(input('Digite o tamanho da terceira reta: ').strip())

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Pode formar um triângulo!!')
else:
    print('Não pode formar um triângulo!!')