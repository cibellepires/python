
prod=float(input('Qual o valor do produto?'))
pag=int(input(''' ESCOLHA A SUA FORMA DE PAGAMENTO:
[1] À VISTA
[2] 2X NO CARTÃO
[3] 3X OU MAIS NO CARTÃO
[4] À VISTA NO CARTÃO: '''))
valor1=0.9*prod
valor3=prod+0.2*prod
valor4=prod*0.95
if pag==1:
    print(f' o valor da sua compra é R$ {valor1}')
elif pag==prod:
    print(f' o valor da sua compra é R$ {prod}')
elif pag==3:
    print(f' o valor da sua compra é R$ {valor3}')
elif pag==4:
    print(f' O valor da sua compra é R$ {valor4}')



