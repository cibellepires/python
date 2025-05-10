n1=float(input('digite sua primeira nota'))
n2=float(input('digite a sua segunda nota'))
nota=(n1+n2)/2
print(f'sua nota é {nota}')
if nota>=6:
    print('VOcê foi aprovado!')
elif nota<6:
    print('Você não passou')