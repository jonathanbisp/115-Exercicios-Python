from desafio115.utilidades.cores import colors


def validar_menu():
    while True:
        print('–' * 40)
        value = input(f'{colors["green"]}Sua opção: {colors["none"]}')
        try:
            value = int(value)
            if 0 < value < 4:
                break
            else:
                print(f'{colors["red"]}ERRO! Por favor, digite uma opção válida.{colors["none"]}')
        except ValueError:
            print(f'{colors["red"]}ERRO! Por favor, digite um número inteiro válido.{colors["none"]}')
    return value
