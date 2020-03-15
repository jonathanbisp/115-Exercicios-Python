jogadores = []
jogador = {}

while True:
    print('–'*36)
    jogador = {'nome': input('Nome do Jogador: ').strip().capitalize(), 'gols': [], 'total': 0}
    jogador['partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for n in range(1, jogador['partidas'] + 1):
        jogador['gols'].append(int(input(f'Quantos gols na partida {n}? ').strip()))
        jogador['total'] += jogador['gols'][n - 1]

    jogadores.append(jogador.copy())
    jogador.clear()

    again = input('Quer continuar? [S/N] ').strip()[0].upper()
    while again not in 'SN':
        again = input('Quer continuar? [S/N] ').strip()[0].upper()
    if again == 'N':
        break
print('=–'*18)
print(f'{"cod":>3} {"nome":<12}{"gols":<15}{"total":<5}')
print('–'*36)
for pos, jog in enumerate(jogadores):
    gols = jog["gols"]
    print(f'{pos:>3} {jog["nome"]:<11} {f"{gols}":<15}{jog["total"]:<5}')
while True:
    print('–' * 36)
    chave = int(input('Mostrar dados de qual jogador? (Para encerrar 999) ').strip())
    if chave == 999:
        print('<<< VOLTE SEMPRE >>>')
        break
    if 0 <= chave < len(jogadores):
        print(f'–– LEVANTAMENTO DO JOGADOR {jogadores[chave]["nome"]}:')
        for pos, n in enumerate(jogadores[chave]["gols"]):
            print(f'   No jogo {pos+1} fez {n} gols. ')
    else:
        print(f'ERRO! Não existe jogador com código {chave}! Tente novamente')
