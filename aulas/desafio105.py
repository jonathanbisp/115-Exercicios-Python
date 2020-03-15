def notas(*notas, status=False):
    """
    FUNÇÃO QUE RETORNA UM OBJETO CONTENDO O TAMANHO,
    O MAIOR ELEMENTO, O MENOR ELEMENTO, A MÉDIA ENTRE
    OS ELEMENTOS.
    :param notas: VARIAVEL COMPACTADA, PARA SE INSERIR TODAS AS NOTAS DE UM ALUNO
    :param status: MUDE PARA TRUE, PARA MOSTRAR O ESTADO DO ALUNO (BOM, RAZOÁVEL, RUIM)
    :return: RETORNA UM DICIONARIO CONTENDO OS ESTATISTICAS DA NOTA
    """
    desempenho = {'total': len(notas)}
    average = 0
    for pos, nota in enumerate(notas):
        if pos == 0:
            maior = menor = nota
        if maior < nota:
            maior = nota
        if maior > nota:
            menor = nota
        average += nota
    desempenho['maior'] = maior
    desempenho['menor'] = menor
    desempenho['média'] = round(average/desempenho['total'], 2)
    if status:
        if desempenho['média'] < 5:
            desempenho['situação'] = 'RUIM'
        elif desempenho['média'] < 7:
            desempenho['situação'] = 'RAZOÁVEL'
        else:
            desempenho['situação'] = 'BOA'
    return desempenho


print(notas(5, 7, 3, 5, 8, 10, status=True))
help(notas)