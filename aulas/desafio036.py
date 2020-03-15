valorCasa = float(input('Valor da casa: R$').strip())
valorSalario = float(input('Salário do comprador: R$').strip())
anos = int(input('Quantos anos de financiamento? ').strip())

parcela = valorCasa/(anos*12)

print(f'Para pagar uma casa de R${valorCasa:.2f} em {anos} anos a prestação será de R${parcela:.2f}')

if parcela > 0.3*valorSalario:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')