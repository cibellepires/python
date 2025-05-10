#números primos
num=int(input('digite um número: ' ))
total=0
for c in range(1,num+1):
    if num%c==0:
        print('\033[34m', end=' ')
        total+=1
    else:
        print('\033[m',end=' ')
    print(f'{c}', end=' ')
print(f' o número {num} foi divisivel {total} vezes')
if total==2:
    print(f' o {num} é primo')
else:
    print(f' o {num} não é primo')