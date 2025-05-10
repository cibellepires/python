#maioridade
from datetime import date
totmaior=0
totmenor=0
for c in range (1,7,1):
    nasc=int(input(f'em que ano a pessoa {c}° nasceu?'))
    atual = date.today().year
    idade=atual-nasc

    if idade>=18:
       totmaior+=1
    else:
        totmenor+=1
print(f' ao todo tivemos {totmaior} pessoas maiores de idade e {totmenor} pessoas menores de idade')



