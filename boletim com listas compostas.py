ficha=list()
while True:
  nome=str(input('Nome: '))
  n1=float(input('Nota1: '))
  n2=float(input('Nota2: '))
  media=(n1+n2)/2
  ficha.append([nome,[ n1,n2] ,media])
  resp=str(input('Deseja continuar?[S/N]: ')).upper()
  if resp in 'Nn':
      break
print('-='*30)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
