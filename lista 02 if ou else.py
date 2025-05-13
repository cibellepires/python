#lista 02


#ex1) calculadora de imc
#peso=float(input('Digite o seu peso [kg}:  '))
#altura=float(input('Digite a altura [m]:  '))
#imc=peso/(altura*altura)
#if imc>=30:
    # print('Obesidade')
#elif 25<=imc<30:
   #  print('Sobrepeso')
#elif 18.5<=imc<25:
  #  print('Peso normal')
#elif imc<18.5:
  #  print('Abaixo do peso')
#print(f' o valor do seu imc é {imc}')


#ex2) classificação da temperatura
#t=int(input('Informe a temperatura:  [°C]'))
#if t<10:
   # print('Muito frio')
#elif 10<=t<=20:
   # print('Frio')
#elif 21<=t<=30:
   # print('Agradável')
#elif t>30:
 #   print('Quente')


 #ex3) votação obrigatória
#i=int(input('Digite sua idade: '))
#if 18<=i<=70:
    # print('Voto obrigatório')
#elif 16<=i<=17 or i>70:
    #print('Voto facultativo')
#elif i<16:
   # print('Não vota')


#ex4) desconto progressivo por qtds
#v=float(input('Digite o valor do produto:'))
#q=int(input('Digite o número de unidades do produto que você irá adquirir: '))
#conta=v*q
#desconto1=0.95*conta
#desconto2=0.90*conta
#if 1<=q<=5:
    #print(f' O valor total da sua conta é {conta}')
#if 6<=q<=10:
    #print(f'o valor da sua conta é {desconto1}')
#if q>10:
   # print(f'O valor da sua conta é {desconto2}')

#ex5) identificar o tipo de triângulo
#l1=int(input('Digite o valor do lado1 do triângulo: '))
#l2=int(input('Digite o valor do lado2 do triângulo: '))
#l3=int(input('Digite o valor do lado3 do triângulo: '))

#if l1==l2==l3:
   # print('Triângulo equilátero')
#elif l1==l2 or l2==l3 or l1==l3:
   # print('Triângulo isosceles')
#else:
  #  print('Triângulo escaleno')


#ex6) simulador de multas atraso na biblioteca
#atraso=int(input('quantos dias a entrega do livro está atrasada?'))
#if atraso<=5:
   # print(f' o valor da multa é R${atraso}')
#if 6<=atraso<=10:
   # print(f' o valor da multa é R${atraso*2}')
#if atraso>10:
   # print( f' O valor da multa é R${atraso*5}')

#ex8) jogo de par ou ímpar
#from random import randint
#n1=int(input('Escolha um número:'))
#a=str(input('Escolha par ou impar: '))
#n2=randint(0,100)
#print(f'o número escolhido pelo computador foi {n2}')
#soma=n1+n2
#print(f' a soma dos números é {soma}')
#if soma%2==0 and  a=='par':
   # print(f'o resultado é par, você venceu!')
#elif soma%2==0 and a=='impar':
    #print(f' o resultado é par, o computador venceu!')
#elif soma%2!=0 and a=='impar':
  #  print( f' O resulado é impar, você venceu!')
#elif soma%2!=0 and a=='par':
    #print(f' O resultado é impar, o computador venceu!')

    






