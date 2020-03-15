from desafio115.utilidades.imprimir_padrao import imprimir_padrao
from desafio115.utilidades.cores import colors
from desafio115.dados.validar_menu import validar_menu


def menu_pricipal():
    imprimir_padrao('MENU PRINCIPAL')
    print(f'{colors["yellow"]}1{colors["none"]} – {colors["blue"]}Ver pessoas cadastradas{colors["none"]}')
    print(f'{colors["yellow"]}2{colors["none"]} – {colors["blue"]}Cadastrar nova Pessoa{colors["none"]}')
    print(f'{colors["yellow"]}3{colors["none"]} – {colors["blue"]}Sair do Sistema{colors["none"]}')

    opc = validar_menu()
    return opc
