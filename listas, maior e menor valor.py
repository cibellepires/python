valores=list()
for cont in range(0,5):
    valores.append(int(input('DIGITE UM VALOR: ')))
print(valores)
maximo=max(valores)
minimo=min(valores)
posmax=valores.index(maximo)
posmin=valores.index(minimo)
print(f' o valor máximo é {maximo} e está na posição {posmax} e o valor mínimo é {minimo} e está na posição {posmin}')