num = int(str(input('Digite um número')).strip())
unidade = num%10
dezena = int(((num-unidade)/10)%10)
centena = int(((num-unidade-dezena*10)/100)%10)
milhar = int((num-unidade-dezena*10-centena*100)/1000%10)
print(f'''Unidade: {unidade}
Dezena: {dezena}
Centena: {centena}
Milhar: {milhar}
''')
