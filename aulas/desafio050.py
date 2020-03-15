num = 0
a = 0
for n in range(0,6):
    a = int(input('Digite um número par para somar: ').strip())
    if a%2 ==0:
        num+=a
print(num)