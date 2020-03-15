from random import randint
from time import sleep

print('–'*50)
print(f'{"JOGAR NA MEGA SENA":^50}')
print('–'*50)

amount = int(input('Quantos jogos você quer que eu sorteie? ').strip())
games = []
print(f'{f"  SORTEANDO {amount} JOGOS  ":=^50}')

for i in range(amount):
    games.append([])
    for j in range(6):
        value = randint(0,60)
        while True:
            if value in games[i]:
                value = randint(0,60)
            else:
                break
        games[i].append(value)
    games[i].sort()
    print(f'JOGO {i+1}: {games[i]}')
    sleep(1)
print(f'{f" < BOA SORTE! > "}')