brasileirão = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico PR', 'São Paulo',
               'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama',
               'Atlético MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA',
               'Chapecoense', 'Avaí')
print('-'*30)
print('Os 5 primeiros colocados são: ')
for time in range(0,5):
    print(f'O {time+1}° colocado é {brasileirão[time]}')

print('-'*30)

print(f'Os 5 últimos times são:')
for time in brasileirão[15:21]:
    print(time)

print('-'*30)

print(sorted(brasileirão))

print('-'*30)

print(f'O time Chapecoense está na posição {brasileirão.index("Chapecoense")+1}')



