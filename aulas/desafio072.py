writedForm1 = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
whitedForm2 = ('Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
writedForm = writedForm1 + whitedForm2

while True:
    print('-'*20)
    key = input('Digite um valor entre 0 e 20: ')
    while not key.isdigit():
        key = input('Digite um valor entre 0 e 20: ')
    key = int(key)
    if 0<= key <=20:
        print(f'Você digitou o número {writedForm[key]}')

    choice = input('Você quer continuar? [S/N] ').strip()[0].lower()
    if choice == 'n':
        break
