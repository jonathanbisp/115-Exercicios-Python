timer = total = num = 0

while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num!=999:
        total += num
        timer += 1
print(f'Você digitou {timer} números e a soma entre eles foi {total}.')
