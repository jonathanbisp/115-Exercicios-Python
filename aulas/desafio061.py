pt = int(input('Digite o primeiro termo da PA: ').strip())
razão = int(input('Digite a razão da PA: ').strip())
cont = 0
while cont < 10:
    print(pt, end=" ←→ ")
    pt = pt+razão
    cont +=1
print('ACABOU')
