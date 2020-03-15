print('='*10,'LOJAS BISPO','='*10)

valor = float(input('Preço das compras: R$').strip())
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opc = int(input('Qual é a opção? ').strip())

if opc == 1:
    print(f'Sua compra de R${valor:.2f}, COM DESCONTO de 10%, vai custar R${valor*0.9:.2f} no final.')
elif opc == 2:
    print(f'Sua compra de R${valor:.2f} ,COM DESCONTO de 5%, vai custar R${valor * 0.95:.2f} no final.')
elif opc == 3:
    print(f'Sua compra será parcelada em 2x de R${valor / 2:.2f}, SEM DESCONTO.')
    print(f'Sua compra de R${valor:.2f} vai custar R${valor:.2f} no final.')
elif opc == 4:
    parcelas = int(input('Quantas parcelas? ').strip())
    print(f'Sua compra será parcelada em {parcelas}x de R${valor*1.2/parcelas:.2f} COM JUROS de 20%')
    print(f'Sua compra de R${valor:.2f} vai custar R${valor * 1.2:.2f} no final.')
else:
    print('OPÇÃO INVÁLIDA!!')