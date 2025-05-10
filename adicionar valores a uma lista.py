numeros=list()
while True:
   n=int(input('Digite um número: '))

   if n not in numeros:
       numeros.append(n)
   else:
       print('Valor duplicado! Não adicionado...')

   a=str(input('Deseja continuar?[S/N] ')).upper()
   if a in 'Nn':
       break
numeros.sort()
print(f' O resultado é: {numeros}')