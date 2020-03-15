lanche = ('xburguer', 'suco', 'pizza', 'pudim')

for pos, food in enumerate(lanche):
    print(f'Eu vou comer {food} na posição {pos}')

for timer in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[timer]} na posição {timer}')

print(sorted(lanche))
print(lanche)