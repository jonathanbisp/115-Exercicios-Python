n1 = int(input('Digite o primeiro valor: ').strip())
n2 = int(input('Digite o segundo valor: ').strip())
n3 = int(input('Digite o terceiro valor: ').strip())

menor = n1 if n1<n2 and n1<n3 else n2 if n2<n1 and n2<n3 else n3
maior = n1 if n1>n2 and n1>n3 else n2 if n2>n1 and n2>n3 else n3

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')