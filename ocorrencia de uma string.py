a=str(input('Digite uma frase: ')).upper()
print(f'A letra A aparece na frase {a.count('A')} vezes')
print( f'A primeria letra A apareceu na posição {a.find('A')+1}')
print(f'A última letra A apareceu na posição {a.rfind('A')+1}')