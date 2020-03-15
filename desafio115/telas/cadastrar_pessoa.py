from desafio115.utilidades.imprimir_padrao import imprimir_padrao
from desafio115.dados.validar_cadastro import validar_nome, validar_idade


def cadastrar_pessoa():
    imprimir_padrao('NOVO CADASTRO')
    nome = validar_nome()
    idade = validar_idade()
    file = open("../files/cadastros.txt", mode='a', encoding='utf-8')
    file.write(f'{nome},{idade};')
    file.close()
    print(f'Novo registro de {nome} adicionado.')