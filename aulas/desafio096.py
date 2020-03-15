def area(height, width):
    print(f'A área de um terreno {height:.1f}m x {width:.1f}m = {height*width:.1f}m²')


print('–'*3, 'CONTROLE DE TERRENOS', '–'*3)
print(f'–'*28)
altura = float(input('Altura: (m) ').strip())
largura = float(input('Largura: (m) ').strip())
area(altura,largura)
