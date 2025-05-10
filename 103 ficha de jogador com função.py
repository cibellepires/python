def ficha(jog='<desconhecido>',gol=0):
    print (f' o Jogador {jog} fez {gol} gol(s) no campeonato.')


n=str(input('Nome do jogador: '))
g=str(input('Número de gols: '))
if g.isnumeric():
    g=int(g)
else:
    g=0
if n.strip()=='' :  #eliminar todos os espaços e verificar se está vazio
    ficha(gol=g)
else:
    ficha(n,g)