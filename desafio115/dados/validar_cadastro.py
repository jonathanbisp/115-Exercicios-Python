from desafio115.utilidades.cores import colors


def validar_nome():

    while True:
        flag = False
        nome = input('Nome: ').strip().split()
        for pos, n in enumerate(nome):
            if not n.isalpha():
                flag = True
                continue
            nome[pos] = n.capitalize()

        if flag:
            print(f'{colors["red"]}ERRO! Nome inválido.{colors["none"]}')
        else:
            return ' '.join(nome)


def validar_idade():
    while True:
        try:
            age = int(input('Idade: ').strip())
        except:
            print(f'{colors["red"]}ERRO! Por favor, digite um número inteiro válido.{colors["none"]}')
            continue
        if age > 130 or age < 0:
            print(f'{colors["red"]}ERRO! Por favor, digite uma idade válida.{colors["none"]}')
        else:
            return age
