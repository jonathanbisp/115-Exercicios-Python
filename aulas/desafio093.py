jogador = {}
jogador['nome'] = input('Nome do Jogador: ').strip().capitalize()
jogador['gols'] = []
jogador['total']: int = 0
jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for n in range(1, jogos+1):
    jogador['gols'].append(int(input(f'Quantos gols na partida {n}? ').strip()))
    jogador['total'] += jogador['gols'][n-1]
print('=–'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=–'*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])}.')
for pos,gol in enumerate(jogador['gols']):
    print(f'    => Na partida {pos}, fez {gol} gols.')
print(f'Foi um total de {jogador["total"]} gols.')