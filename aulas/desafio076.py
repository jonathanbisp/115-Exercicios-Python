produtos = ('Batata Frita', 3.85, 'Arroz',3.20,
            'Feijão', 3.45, 'Carne', 19.50,
            'Placa de ovos',10.00, 'Biscoito',1.70)
print('–'*30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('–'*30)

for n in range(0,len(produtos),2):
    print(f'{produtos[n]:.<21}R${produtos[n+1]:>7.2f}')