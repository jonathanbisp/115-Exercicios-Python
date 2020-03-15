maiorIdNm = ''
média = timer = maiorIdade = 0

for pess in range(1, 5):
    print(f"{f'{pess}° PESSOA':=^30}")
    nome = input('Nome: ').strip()
    idade = int(input('Idade: ').strip())
    sexo = input('Sexo [M/F]: ').strip().upper()

    média += idade

    if sexo == 'M':
        if idade > maiorIdade:
            maiorIdade = idade
            maiorIdNm = nome
    elif sexo == 'F':
        if idade < 20:
            timer += 1

print(f'A média de idade do grupo é de {média / 4} anos.')
print(f'O homem mais velho tem {maiorIdade} anos e se chama {maiorIdNm}.')
print(f'Ao todo são {timer} mulheres com menos de 20 anos.')
