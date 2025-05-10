velocidade=float(input('Qual é a velocidade atual do carro?'))
if velocidade>80:
    print('VOcê foi multado!')
    multa=(velocidade-80)*7
    print(' Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('tenha um bom dia!')

