from datetime import date
atual=date.today().year
nascimento=int(input('Qual o ano de nascimento do atleta?'))
idade=atual-nascimento
if idade<=9:
    print(f'O atleta tem {idade} e é mirim')
elif 9<idade<=14:
    print(f' o atleta tem {idade} e é infantil')
elif 14<idade<=19:
    print(f' o atleta tem {idade} e é junior')
elif 19<idade<=25:
    print(f' o atleta tem {idade} e é sênior')
elif idade>25:
    print(f' o atleta tem {idade} e é master')
