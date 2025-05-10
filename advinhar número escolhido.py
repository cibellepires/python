import random
from random import randint

computador=randint(0,5)

print('vou pensar em um número entre 0 e 5, tente adivinhar')
jogador=int(input('Em que número eu pensei?'))
print('Pensei no número {}'.format(computador))
if jogador==computador:
    print('o jogador venceu')
else:
    print('O computador venceu')




