pt = int(input('Digite o primeiro termo da PA: ').strip())
razão = int(input('Digite a razão da PA: ').strip())

for c in range(pt,pt+razão*10,razão):
    print(c,end=" ←→ ")
print('ACABOU')
