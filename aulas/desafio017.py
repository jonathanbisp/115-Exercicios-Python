import math

co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente: '))
print(f'O valor da hipotenusa será {math.sqrt(math.pow(co,2)+math.pow(ca,2)):.2f}')
print(math.hypot(ca,co))