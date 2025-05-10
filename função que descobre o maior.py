from time import sleep
def maior(*num):
    cont=maior=0
    print('Analisando os valores informados...')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.5)
        if cont==0:
            maior=valor
        else:
            if valor>maior:
                maior=valor
        cont+=1
    print(f' foram informados {cont} valores ao todo')
    print(f' o maior valor informado: {maior}')


maior(2, 3, 8, 9, 11)
maior(4, 7, 0)
