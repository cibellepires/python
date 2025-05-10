#listas
val=list(range(2,8))
print(val)
#colocar em ordem
#tupla() = é imutável
#lista [] = é mutável
num=[2,6,4,8,9,10]
num[2]=23
num.sort()
num.remove(2)
if 4 in num:
    num.remove(4)
print(num)

valores=[]
valores.append(5)
valores.append(4)
valores.append(8)
for c, v in enumerate(valores):
    print(f' encontrei na posição {c} o valor {v}')

a=[1,1,1,1,1,1]
b=a[:]
b[2]=8
print(f' a lista a: {a}')
print(f' a lista b: {b}')