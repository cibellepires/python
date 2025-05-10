#escrever números por extenso
lista=('zero', 'um','dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito','nove', 'dez', 'onze', 'doze','treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
a=int(input('Digite um número de 0 a 20: '))
while a>20 or a<0:
    break
print(f' {lista[a]}')


