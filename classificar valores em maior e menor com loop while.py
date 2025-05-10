contador=media=maior_valor=valor=a=soma=0
a='S'
while a in 'sS':
   valor=int(input('Digite um número: '))
   a=str(input('Quer continuar[S/N]? ')).upper().strip()[0]
   if contador==1:
       maior_valor=valor
   if contador>1 and valor>maior_valor:
       maior_valor=valor
   contador+=1
   soma+=valor
print('FIM')
media=soma/contador
print(f' você digitou {contador} números, a média deles é {media} e o maior valor é {maior_valor}')







