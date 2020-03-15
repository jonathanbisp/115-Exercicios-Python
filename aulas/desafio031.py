dis = float(input('Qual é a distância da sua viagem? ').strip())
print(f'Você está prestes a iniciar uma viagem de {dis:.1f}Km.')
print(f'E o preço da sua passagem será de R${dis*0.50 if dis<= 200 else dis*0.45:.2f}')