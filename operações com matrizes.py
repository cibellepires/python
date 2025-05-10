lista1 = list()
par=list()
for c in range(1, 4):
    a = int(input(f'Digite o valor [0,{c}]: '))
    if a%2==0:
     par.append(a)
    lista1.append(a)

lista2 = list()
for c in range(1, 4):
    b = int(input(f'Digite o valor de [1,{c}]'))
    if b%2==0:
      par.append(b)
    lista2.append(b)
lista3 = list()
for c in range(1, 4):
    s = int(input(f'Digite o valor de [2,{c}]'))
    if s%2==0:
        par.append(s)
    lista3.append(s)
print(lista1)
print(lista2)
print(lista3)
print('-='*30)
soma=lista1[2]+lista2[2]+lista3[2]
print(f'a soma dos elementos da terceira coluna é {soma}')
soma2=sum(par)
print(f' os pares da matriz: {par}')
print(f' a soma dos elementos pares é {soma2}')
maiorlista2=max(lista2)
print(f' o maior elemento da lista 2 é {maiorlista2}')

