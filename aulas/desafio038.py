print('-='*25,'\nDescubra qual entre dois valores é o maior!!\n','-='*25,)

n1 = int(input('Digite o primeiro valor: ').strip())
n2 = int(input('Digite o segundo valor: ').strip())

if n1 == n2:
    print('Não existe valor maior. OS DOIS SÃO IGUAIS!!')
elif n1>n2:
    print(f'O primeiro valor "{n1}" é o maior')
else:
    print(f'O segundo valor "{n2}" é o maior')
