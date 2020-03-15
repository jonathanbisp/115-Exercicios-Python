expression = input('Digite a expressão: ').strip()

parentheses = []
for n in expression:
    if n == '(':
        parentheses.append('(')
    if n == ')' and len(parentheses) >= 1:
        parentheses.pop()
    elif n == ')':
        parentheses.append(')')

print(parentheses)
if len(parentheses) != 0:
    print('Sua expressão está errada!')
else:
    print('Sua expressão está válida!')
