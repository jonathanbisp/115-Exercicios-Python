frase = str(input('Digite uma frase: ')).strip()

print(f'''A letra "a" aparece {frase.lower().count('a')} vezes.
A letra "a" aparece pela primeira vez na posição {frase.lower().find('a') + 1 }.
A letra "a" aparece pela última vez na posição { frase.lower()[::-1].rfind('a') + 1 }''')