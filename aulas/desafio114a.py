import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('NÃO É POSSIVEL SE CONECTAR')
else:
    print('TUDO OK!!')
    print(site.read())
