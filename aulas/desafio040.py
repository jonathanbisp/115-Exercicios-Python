n1 = float(input('Primeira nota: ').strip())
n2 = float(input('Segunda nota: ').strip())

média = round((n1+n2)/2,1)
print(f'A média do aluno foi {média}.')
if média < 5:
    print('Portanto ele foi \033[31mREPROVADO\033[m!!')
elif média < 7:
    print('Portanto ele foi para a \033[33mRECUPERAÇÃO\033[m!!')
else:
    print('Portanto ele foi \033[32mAPROVADO\033[m!!')