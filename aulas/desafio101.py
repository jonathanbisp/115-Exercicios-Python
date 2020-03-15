from datetime import date


def voto(anoNascimento):
    anoAtual = date.today().year
    age = anoAtual - anoNascimento
    return f"Com {age} anos: " + ("VOTO NEGADO" \
           if age < 16 else "VOTO OPCIONAL" if age < 18 or age >= 65 \
           else "VOTO OBRIGATORIO")


print('–'*25)
print(voto(int(input('Em que ano você nasceu? ').strip())))
