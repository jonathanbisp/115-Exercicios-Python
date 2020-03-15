salario = float(input('Qual é o salário do funcionáro? R$').strip())

if salario > 1250:
    print(f'Quem ganhava R${salario:.2f} passa a ganhar {salario*1.1:.2f}')
else:
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario*1.15:.2f}')