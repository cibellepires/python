n1=int(input('Digite um número: '))
n2=int(input('Digite um número: '))
n3=int(input('Digite um número: '))
n4=int(input('Digite um número: '))
n5=int(input('Digite um número: '))
n6=int(input('Digite um número: '))
n7=int(input('Digite um número: '))
pares=list()
impares=list()
numerospares=list()
numerosimpares=list()
if n1%2==0:
    pares.append(n1)
    numerospares.append(pares[:])
    pares.clear()
else:
    impares.append(n1)
    numerosimpares.append(impares[:])
    impares.clear()

if n2%2==0:
    pares.append(n2)
    numerospares.append(pares[:])
    pares.clear()
else:
    impares.append(n2)
    numerosimpares.append(impares[:])
    impares.clear()

if n3%2==0:
    pares.append(n3)
    numerospares.append(pares[:])
    pares.clear()
else:
    impares.append(n3)
    numerosimpares.append(impares[:])
    impares.clear()

if n4%2==0:
    pares.append(n4)
    numerospares.append(pares[:])
    pares.clear()
else:
    impares.append(n4)
    numerosimpares.append(impares[:])
    impares.clear()

if n5%2==0:
    pares.append(n5)
    numerospares.append(pares[:])
    pares.clear()
else:
    impares.append(n5)
    numerosimpares.append(impares[:])
    impares.clear()

if n6%2==0:
    pares.append(n6)
    numerospares.append(pares[:])
    pares.clear()
else:
    impares.append(n6)
    numerosimpares.append(impares[:])
    impares.clear()

if n7%2==0:
    pares.append(n7)
    numerospares.append(pares[:])
    pares.clear()
else:
    impares.append(n7)
    numerosimpares.append(impares[:])
    impares.clear()
    
numerospares.sort()
numerosimpares.sort()
print(numerospares)
print(numerosimpares)