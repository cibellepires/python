import os
#arquivos_extraidos=[]

#def pegar_arquivos_pasta(pasta):
   # arquivos=os.listdir(pasta)
    #print(pasta)
   # pass
#pegar_arquivos_pasta('pycharm-community-2024.3.4')

#def fatorial(numero):
   # if numero==0 or numero==1:
      # return 1
  #  else:
      #  return numero*fatorial(numero-1)
#n=int(input('digite um número para cálcular seu fatorial: '))
#resposta=fatorial(n)
#print(resposta)

#fibonacci
def fibonacci(num):
    if num <=1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
a=int(input('digite um número de algarismos para a sequencia: '))
resposta=(fibonacci(a-1))
print(resposta)