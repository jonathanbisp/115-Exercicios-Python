from desafio115.utilidades.imprimir_padrao import imprimir_padrao


def exibir_pessoas():
    imprimir_padrao('PESSOAS CADASTRADAS')
    file = open("../files/cadastros.txt", encoding='utf-8')
    for texto in file:
        linha = texto.split(';')
        del linha[-1]
        for pessoa in linha:
            pessoa = pessoa.split(',')
            nome = pessoa [0]
            idade = pessoa[1]
            print(f'{nome:<25}{idade:>3} anos')

