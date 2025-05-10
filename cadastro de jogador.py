jogador=dict()
partidas=list()
jogador['nome']=str(input('NOME DO JOGADOR: '))
tot=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range (0,tot):
    partidas.append(int(input(f'Quantos gols na partida {c}')))
jogador['gols']=partidas[:]
jogador['total']=sum(partidas)
print('-='*30)
print(jogador)


