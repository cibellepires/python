#menu de opções
n1=int(input('digite um valor: '))
n2=int(input('digite outro valor: '))
opçao=0
soma=[]
while opçao!=5:
  print('''[1] soma
  [2] multiplicar
  [3] maior
  [4] novos números
  [5] fim do programa''')
  opçao=int(input('Qual é a sua opção?'))
  if opçao == 1:
      soma+=1
      soma = n1 + n2
      print(f' a soma entre {n1} e {n2} é {soma}')
  if opçao == 2:
      multiplicaçao = n1 * n2
      print(f' a multiplicação entre {n1} e {n2} é {multiplicaçao}')
  if opçao == 3:
      if n1 > n2:
          print(f' o valor {n1} é maior que {n2}')
      elif n1 == n2:
          print(f' os valores são iguais')
      else:
          print(f' o valor {n2} é maior que {n1}')
  if opçao == 4:
      print('Digite novos números:')
      n1 = int(input('DIGITE O PRIMEIRO NÚMERO: '))
      n2 = int(input('DIGITE O SEGUNDO NÚMERO: '))
  else:
      print('erro, tente novamente')

print('FIm do programa')














