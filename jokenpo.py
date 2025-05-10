from random import randint
jogador=int(input('''Escolha pedra, papel ou tesoura, suas opções:
[0] pedra
[1] papel
[2] tesoura'''))
itens=('pedra','papel', 'tesoura')
computador=randint(0,2)
print(f' o computador escolheu {itens[computador]}')
print(f' o jogador escolheu {itens[jogador]}')
if computador==0 and jogador==2 or computador==2 and jogador==1 or computador==1 and jogador==0:
    print('O computador venceu')
elif computador==0 and jogador==1 or computador==1 and jogador==2 or computador==2 and jogador==0:
    print(' o jogador venceu')
elif computador==jogador:
    print('empate')




