def ficha(nome, gols):
    if len(nome) == 0:
        nome = "<desconhecido>"
    if len(gols) == 0 or not gols.isnumeric():
        gols = 0
    return f'O jogador {nome} fez {gols} no campeonato'


print(ficha(nome=input('Nome do Jogador: ').strip(), gols=input('Número de Gols: ').strip()))
