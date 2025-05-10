numeros=list()
pares=list()
impares=list()
while True:
   n=int(input('Digite um número: '))

   if n not in numeros:
       numeros.append(n)
   else:
       print('Valor duplicado! Não adicionado...')

   a=str(input('Deseja continuar?[S/N] ')).upper()
   if a in 'Nn':
       break
for i, v in enumerate(numeros):
    if v%2==0:
        pares.append(v)
    elif v%2==1:
        impares.append(v)
print(numeros)
print(pares)
print(impares)
