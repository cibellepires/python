#lista 03 de funções

#ex1) função nome
#def saudacao(nome):
   # print(f'Olá, {nome}!')
#saudacao('Maria')
#saudacao('João')

#ex2) função soma
#def soma(a,b):
   # s=a+b
   # print(f' a soma de {a}+{b} é {s}')
#soma(3,4)

#ex3 verificar se um numero é par ou impar
#def verificacao(numero):
   # if numero%2==0:
       # print(f' {numero} é Par')
  #  else:
       # print(f' {numero} é impar')
#verificacao(4)
#verificacao(7)

#ex4) receber uma lista de numeros e retornar a media dos valores
#def calculo_da_media(numeros):
   # if len(numeros)==0:
      #  return 0
   # return sum(numeros)/len(numeros)
#numeros=[5, 10, 10]
#media=calculo_da_media(numeros)
#print(media)

#ex5) função que retorne o maior valor de uma tupla de inteiros

#def analise_tupla(t):
  #  return max(t)

#t=(1,2,3,4,5,6,7,8,9,10)
#maior=analise_tupla(t)
#print(f' o maior valor da tupla é {maior}')

#ex6) crie uma função que use *args para somar qualquer qtd de numeros
#*args permite que você receba um número variavel de argumentos que são tratados como tupla dentro da função

#def soma(*args):
   # return sum(args)

#resultado=soma(1,2,3,4,5)
#print(resultado)

#ex7 Crie uma função que use **kwargs para montar um dicionário com dados pessoais (nome, idade, cidade).

#def dicionario (**kwargs):
   # return kwargs
#dados=dicionario(nome='Cibelle', idade= 22, cidade='Goiânia')
#print(dados)

#ex8) receber numero entre 1 à 20000 e retornar true se for primo

#def primo(x):
  #  if x<=1:
    #   return False
 #   for divisor in range (2,x): #verifica de 2 até x-1
  #     if x%divisor==0:
  #       return False
  #  return True
#print(primo(7))
#print(primo(1))
#print(primo(2))
#print(primo(15))

#ex9) função para ler apenas numeros inteiros
#def ler_inteiro():
  #  while True:
     #   try:
       #     return int(input("Digite um número inteiro: "))
    #    except:
     #       print("Inválido, tente novamente")

# Exemplo de uso:
#n = ler_inteiro()
#print("Número válido:", n)

#ex10) crie uma função que receba uma string e conte quantas vogais há nela

#def contar_vogais(texto):
   # contador = 0
  #  for letra in texto:
     #   if letra.lower() in 'aeiou':
        #    contador += 1
   # return contador

#print(contar_vogais('cibelle'))

#ex11) dicionário de notas
#def estatisticas_notas(notas):
   # return {
     #   'media': sum(notas) / len(notas),
      #  'maior': max(notas),
     #   'menor': min(notas)
  #  }

# Exemplo de uso:
#print(estatisticas_notas([7, 8.5, 6, 9]))
# Saída: {'media': 7.625, 'maior': 9, 'menor': 6}

#ex12) remoção de duplicatas em uma lista usando set
#def remover(lista):
   # return list(set(lista))

#lista1=[1,1,1,2,2,2,3,3,3,]
#lista2=remover(lista1)
#print(lista2)

#ex13) função que retorne quantos elementos de uma lista são maiores que a média
#def contar_acima_media(lista):
  #  if len(lista) == 0:
  #      return 0
 #   media = sum(lista) / len(lista)
 #   contador = 0
 #   for numero in lista:
 #       if numero > media:
 #           contador += 1
 #   return contador

#lista1=[1,2,3,4,5,6,7]
#print(contar_acima_media(lista1))

#ex14 uma função que receba um dicionário e retorne chaves ordenadas
#def ordenar_chaves(dicionario):
   # return sorted(dicionario)  # Dicionários iteram sobre as chaves por padrão

#dicionario={'b':1, 'a':2, 'c':3}
#ordem=ordenar_chaves(dicionario)
#print(ordem)

#ex15) função que receba uma lista de dicionario com nome de pessoas e retorne o nome da pessoa mais velha
#def pessoa_mais_velha(lista):
 #   mais_velha=lista[0]
 #   for pessoa in lista:
#        if pessoa['idade']>mais_velha['idade']:
 #           mais_velha=pessoa
 #   return mais_velha['nome']

#lista=[{'nome': 'Cib', 'idade':22}, {'nome': 'Bia', 'idade': 21}, {'nome': 'Joao', 'idade':123}]
#dados=pessoa_mais_velha(lista)
#print(dados)

#ex16 notas em uma tupla
#def notas(n):
    #media=sum(n)/len(n)
   # if media>7:
      #  return f'Média {media:.2f}: aprovado!'
  #  else:
      #  return 'Reprovado!'

#n=(9,10,5)
#print(notas(n))

#ex18 crie uma função recursiva que calcule o fatorial de um número
#def fatorial(n):
 #   if n==1:
#        return 1
 #   if n<0:
 #       return False
 #   else:
 #       return n*fatorial(n-1)
#print(fatorial(5))

#ex17 função que troque os pares e os impares de lugar
#def trocar_pares_impares(lista):
 #   for i  in range (0, len(lista)-1, 2):
  #      lista[i], lista[i+1]=lista[i+1], lista[i]
  #  return lista

#entrada=[1,2,3,4,5,6]
#saida=trocar_pares_impares(entrada)
#print(saida)

#ex19 função que inverta uma string
#def inversao_de_string(s):
   # return s[::-1]

#palavra_invertida=inversao_de_string('Pyhton')
#print(palavra_invertida)

#ex20) busca binária em uma lista ordenada
#def busca_binaria(lista, elemento):
 #   def recursao(inicio, fim):
 #       print(f"Analisando {lista[inicio:fim + 1]}")
 #       if inicio > fim:
 #           return -1
 #       meio = (inicio + fim) // 2
 #       if lista[meio] == elemento:
 #           return meio
 #       elif lista[meio] > elemento:
 #           return recursao(inicio, meio - 1)
 #       else:
 #           return recursao(meio + 1, fim)

 #   print(f"Busca por {elemento} em {lista}")
  #  return recursao(0, len(lista) - 1)

#lista_ordenada=[1,2,3,4,5,6,7,8]
#e=6
#resultado=busca_binaria(lista_ordenada,e)
#print(resultado)

