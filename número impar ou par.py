#numero ímpar ou par
numero=int(input('Digite um número qualquer'))
resultado=numero%2
print(f'O resultado foi {resultado}')
if resultado==1:
    print('O seu número é ímpar')
else:
    print('O seu número é par')