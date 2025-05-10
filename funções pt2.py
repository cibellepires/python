def contador (i,f,p):
  c=i
  while c<=f:
    print(f'{c}', end=' ')
    c+=p
contador(2,10,2) #começa em 2, termina em 10 e vai de dois em dois

print('-='*30)

def somar(a,b,c=0):
    s=a+b+c
    print(f' a soma vale {s}')
somar(3,2,5)

print('-='*30)

def teste():
#PROGRAMA PRINCIPAL
   n=2
   print(f'no programa principal, n vale {n}')
teste()

print('-='*30)

def funcao():
    n1=4
    print(f' N1 dentro vale {n1}')
n1=2
funcao()
print(f' n1 fora vale {n1}')

print('-='*30)

def somar(a=0, b=0, c=0): #colocar as somas para aparecerem todas juntas
    s=a+b+c
    return s

r1=somar(3,2,1)
r2=somar(1,7)
r3=somar(4)
print(f' os cálculos deram {r1}, {r2}, {r3}')