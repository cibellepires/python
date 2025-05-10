def area(larg,comp):
  a=larg*comp
  print(f' a area de um terreno {larg}x{comp} é {a}')

print('         CONTROLE DE TERRENOS      ')
print('-'*50)

l = float(input('Largura(m): '))
c = float(input('Comprimento(m):  '))
area(l,c)
