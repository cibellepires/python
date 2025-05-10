from random import randint
v=0
while True:
    jogador=int(input('DIGA UM VALOR: '))
    computador=randint(0,11)
    total=jogador+computador
    tipo=' '
    while tipo not in 'PpIi':
        tipo=str(input('Par ou Impar? ')).strip().upper()[0]
    print(f' voce jogou {jogador} e o computador jogou {computador}')
    if tipo=='P':
        if total%2==0:
            print('você venceu')
            v+=1
        else:
            print('você perdeu')
            break
    elif tipo=='I':
        if total%2==1:
            print('você venceu')
            v+=1
        else:
            print('voce perdeu')
            break