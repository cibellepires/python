brasileirao=('Internacional','corinthians','Ceará', 'Fortaleza','Botafogo','Flamengo', 'Palmeiras', 'Juventude','Fluminense', 'Grêmio','Vasco de Gama', 'Cruzeiro','Bahia','São Paulo', 'Bragantino', 'Santos', 'Mirassol', 'Sport Recife', 'Atlético-mg', 'EC Vitóra')
print(f' Os 5 primeiros da tabela: {brasileirao[0:5]}')
print(f' os últimos 4 colocados: {brasileirao[-4:]}')
brasileirao_ordem=sorted(brasileirao)
print(f' lista em ordem alfabética: {brasileirao_ordem}')
pos=brasileirao.index('Fortaleza')
print(f'a posição do time fortaleza é {pos}')
