#maior e menor valor
n1=int(input('DIGITE UM VALOR:'))
n2=int(input('DIGITE OUTRO VALOR:'))
n3=int(input('DIGITE MAIS UM OUTRO VALOR:'))
#if n1>n2>n3:
   # print(f' o maior valor é {n1} e o menor valor é {n3}')
#elif n2>n1>n3:
    #print(f' o maior valor é {n2} e o menor valor é {n3}')
#elif n2>n3>n1:
  #  print(f' o maior valor é {n2} e o menor valor é {n1}')
#elif n3>n2>n1:
   # print(f' o maior valor é {n3} e o menor valor é {n1}')
#elif n3>n1>n2:
    #print(f' o maior valor é {n3} e o menor valor é {n2}')
menor=n1
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3

print('O menor valor digitado foi {}'.format(menor))



