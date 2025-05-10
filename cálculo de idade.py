from datetime import date
atual=date.today().year
nasc=int(input('QUal o ano de nascimento?'))
idade=atual-nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade==18:
    print('Você deve se alistar imediatamente')
elif idade>18:
    atraso=idade-18
    print(f'Você ja deveria ter se alistado há {atraso} anos')
elif idade<18:
     faltam=18-idade
     print(f' você ainda terá que se alistar, faltam {faltam} anos')



