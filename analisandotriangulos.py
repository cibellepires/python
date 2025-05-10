l1=int(input('DIgite o valor de um lado'))
l2=int(input('digite o valor de outro lado'))
l3=int(input('digite o valor de mais um lado'))
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('os lados podem formar um triângulo', end=' ')
    if l1==l2==l3:
        print('equilátero')
    if l1==l2 or l2==l3 or l1==l3:
        print('Isósceles')
    if l1 != l2 != l3 and l1!=l3:
        print('escaleno')
else:
    print('o triângulo não existe')

