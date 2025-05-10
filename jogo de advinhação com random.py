from random import randint
computador=randint(0,10)
print('vou pensar em um número de 0 a 10, tente advinhar')
acertou=False
palpites=0
while not acertou:
    jogador=int(input('Qual é o seu palpite?'))
    palpites+=1
    if jogador==computador:
        acertou=True
    else:
        if jogador<computador:
            print('Mais... tente novamente')
        elif jogador>computador:
            print('Menos...tente novamente')
print(f'você acertou com {palpites} tentativas, Parabéns!')
