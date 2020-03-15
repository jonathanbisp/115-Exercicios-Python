from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para o ano atual: ').strip())

if ano == 0:
    ano =  date.today().year

if ano%4 == 0 and ano%100 != 100 or ano%400 == 0:
        print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO É BISSEXTO')