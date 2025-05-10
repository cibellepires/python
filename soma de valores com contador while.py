soma=contador=0
while True:
    num=int(input('DIGITE UM NÚMERO: '))
    if num==999:
        break
    contador+=1
    soma+=num
print(f' a soma dos valores foi {soma}')
