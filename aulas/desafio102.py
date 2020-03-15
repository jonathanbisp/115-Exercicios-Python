def fatorial(value, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param value: O número a ser calculado
    :param show: Define se vai retornar ou não a conta
    :return: retorna o resultado em forma de string, variando com o parametro show
    """
    total = 1
    resposta = ''
    for n in range(value, 0, -1):
        if show:
            resposta += f'{n}'
            if n != 1:
                resposta += ' x '
            else:
                resposta += ' = '
        total *= n
    resposta += str(total)
    return resposta


print(fatorial(5))
help(fatorial)