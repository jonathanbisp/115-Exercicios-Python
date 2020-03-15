somatorio: int = 0
contador: int = 0
for n in range(3, 501, 3):
    if n % 2 == 1:
        somatorio += n
        contador += 1

print(f'A soma de todos os {contador} valores solicitados é {somatorio}.')
