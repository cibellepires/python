#PROGRESSAO ARITMETICA
a1=int(input('PRIMEIRO TERMO: '))
razao=int(input('RAZÃO: '))
a11=a1+razao*10
for c in range (a1,a11,razao):
    print(f' {c}', end=' -> ')