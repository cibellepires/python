n=int(input('Primeiro Termo'))
razao=int(input('Razao: '))
termo=n
contador=1
total=0
mais=10
while mais!=0:
   total=total+mais
   while contador<=total:
      print(f'{termo} ->',end=' ')
      termo+=razao
      contador+=1
   print ('Pausa')
   mais=int(input('Quantos termos você quer mostrar a mais?'))
print('FIm')
