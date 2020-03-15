from desafio115.telas.menu_principal import menu_pricipal
from desafio115.telas.cadastrar_pessoa import cadastrar_pessoa
from desafio115.telas.exibir_pessoas import exibir_pessoas
from desafio115.telas.sair_sistema import sair_sistema


def main():
    while True:
        opc = menu_pricipal()
        if opc == 1:
            exibir_pessoas()
        if opc == 2:
            cadastrar_pessoa()
        if opc == 3:
            sair_sistema()
            break

main()