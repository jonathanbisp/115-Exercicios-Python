def moeda(value):
    value = f'{value:.2f}'.split('.')
    value = f"R${','.join(value)}"
    return value


def dobro(value, transform=False):
    total = value*2
    if transform:
        return moeda(total)
    return total


def metade(value, transform=False):
    total = value/2
    if transform:
        return moeda(total)
    return total


def aumentar(value, percent=0, transform=False):
    total = value*(100+percent)/100
    if transform:
        return moeda(total)
    return total


def diminuir(value, percent=0, transform=False):
    total = value*(100-percent)/100
    if transform:
        return moeda(total)

    return total


def resumo(value, perPlus, perLess):
    print('–'*31)
    print(f'{"RESUMO DO VALOR":^31}')
    print('–' * 31)
    print(f'{"Preço analisado:":<20}{moeda(value):>6}')
    print(f'{"Dobro do preço:":<20}{dobro(value, True):>6}')
    print(f'{"Metade do preço:":<20}{metade(value, True):>6}')
    print(f'{f"{perPlus}% de aumento:":<20}{aumentar(value, perPlus, True):>6}')
    print(f'{f"{perLess}% de redução:":<20}{diminuir(value, perLess, True):>6}')
    print('–' * 31)
