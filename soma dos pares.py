#soma dos pares
soma=0
cont=0
for n in range (7):
   n=int(input('digite um número'))
   if n%2==0:
    soma=soma+n
    cont=cont+1
print(f'voce informou {cont} números e a soma foi {soma}')


