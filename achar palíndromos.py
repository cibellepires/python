#palindromos
#a=str(input('digite uma frase: ')).strip().upper()
#b=a[::-1]
#print(b)
#if a==b:
    #print('ela é um palíndromo')
#else:
    #print('não é um palindromo')

frase=str(input('digite uma frase: ')).strip().upper()
palavras=frase.split()
junto=''.join(palavras)
print(f'você digitou a frase {junto}')
inverso=''
for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]
print(junto,inverso)
if inverso==junto:
       print('é palindromo')
else:
    print('não é palindromo')

