casa=float(input('Qual o valor da casa?'))
salario=float(input('Qual o seu salário?'))
anos=float(input('Em quantos anos você pretende pagar?'))
prestação=casa/(anos*12)
minimo= salario*30/100
print(f' para pagar uma casa de R${casa} em {anos} anos')
print(f' a prestação será de {prestação}')
if prestação <=minimo:
    print('EMPRÉSTIMO CONCEDIDO!')
else:
    print('Empréstimo negado')
    


