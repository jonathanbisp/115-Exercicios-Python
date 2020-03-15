from datetime import date
anoAtual = date.today().year

pessoa = {}
pessoa['Nome'] = input('Nome: ').strip().capitalize()
pessoa['Idade'] = anoAtual - int(input('Nascimento: ').strip())
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): ').strip())
if pessoa['CTPS'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: ').strip())
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = 35 - (anoAtual - pessoa['Ano de contratação']) + pessoa['Idade']
print('=–'*50)
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
