
def voto(ano):
    from datetime import date
    atual=date.today().year
    idade=atual-ano
    if idade<16:
        return f'Com {idade} anos: Não vota'
    elif 16<= idade<18 or idade>65:
        return f' COm {idade} anos: Voto opcional'
    else:
        return f'com {idade} anos: Voto obrigatório'

nasc=int(input('Em que ano você nasceu? '))
print(voto(nasc))

