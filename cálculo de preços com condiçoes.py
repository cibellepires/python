#calculo de preços
distancia=int(input('Qual a distancia da sua viagem?'))
if distancia<=200:
    passagem=distancia*0.5
    print(f'O valor da sua passagem será {passagem} reais')
elif distancia>200:
    passagem=distancia*0.45
    print(f' o valor da sua passagem será {passagem} reais')
