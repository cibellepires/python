r='S'
total=0
maiorpeso=menorpeso=0
dado=list()
grupo=list()
while r=='S':
   dado.append(str(input('Nome: ')))
   dado.append(int(input('Peso: ')))
   if total==0:
       maiorpeso=menorpeso=dado[1]
   else:
       if dado[1]>maiorpeso:
          maiorpeso=dado[1]
       if dado[1]<menorpeso:
           menorpeso=dado[1]
   total+=1
   r=str(input('Quer continuar?[S/N] ')).upper()
   grupo.append(dado[:])
   dado.clear()
print('-='*30)
print(grupo)
print(f' foram {total} pessoas cadastradas')
print('-='*30)
print(f' o maior peso foi {maiorpeso}')
for p in grupo:
    if p[1]==maiorpeso:
        print(f'[{p[0]}]', end='')
print(f' o menor peso foi {menorpeso}')

