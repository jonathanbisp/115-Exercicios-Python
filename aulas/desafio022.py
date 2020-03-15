nome = str(input('Digite o seu nome: ')).strip()
print(f'''Em maiúsculo é { nome.upper() }.
Em minúsculo é { nome.lower() }.
Contém ao total {len(''.join(nome.split()))} letras.
O primeiro nome contém { len(nome.split()[0]) } letras.''')
