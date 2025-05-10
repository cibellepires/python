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
print(f' foram digitados {len(numeros)} números')
numeros.sort(reverse=True)
print(f' a lista em forma descrescente {numeros}')
if 5 in numeros:
    print('O números 5 está na lista')
else:
    print('O números 5 não está na lista')