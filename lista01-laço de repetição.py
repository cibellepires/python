#ex1) contagem simples
#for c in range(1,11):
    #print(f'{c}', end=' ')


#ex2) tabuada simples
#n=int(input('Escolha um número para obter a sua tabuada: '))
#for c in range(1,11):
   # m=c*n
   # print(f'{n}x{c}={m}')



#ex3) números pares 0 a 20
#for c in range (0,21):
   # if c%2==0:
     #   print(f'{c}', end=' ')



#ex4) soma de 5 números digitados
#soma=0
#for c in range(5):

   # n=int(input('Digite um número:  '))
    #soma+=n
#print(f' a soma dos números é {soma}')

#ex5) fatorial
#n = int(input("Digite um número inteiro não negativo: "))

#if n < 0:
    #print("Fatorial não está definido para números negativos.")
#else:
    #fatorial = 1
   # contador = 1
    #while contador <= n:
        #fatorial *= contador
       # contador += 1
  #  print(f"{n}! = {fatorial}")

#ex6 classificar numeros em par ou impar
#for i in range(8):
    #n=int(input('Digite um número: '))
  #  if n%2==0:
     #  print(f' {n} é par')
    #else:
       # print(f'{n} é ímpar')

#ou

#pares = []
#impares = []

#print("Digite 8 números para classificação:")

#for i in range(1, 9):
    #numero = int(input(f"Digite o {i}º número: "))
   # if numero % 2 == 0:
    #    pares.append(numero)
  #  else:
       # impares.append(numero)

#print("Resultado da classificação:")
#print(f"Números pares: {pares}")
#print(f"Números ímpares: {impares}")

#ex7) contagem regressiva
#for i in range(10,0,-1):
   # print(f'{i}', end=' ')

#ex8)média de notas
#soma=media=0
#for c in range(5):
   # nota=int(input(f' digite o valor da Nota{c+1}:'))
  #  soma+=nota
   # media=soma/5

#if media<7:
    # print(f'Média: {media}, Aluno reprovado')
#else:
     #print(f'Média {media}, Aluno aprovado')

#ex9) números primos:
#primos=[]
#for a in range (2,51):
   # for c in range (2, a):
      # if (a%c)==0:
          # break
  #  else:
       # primos.append(a)
#print( f' lista de números primos: {primos}')

#ex10) gerar n termos da sequencia de fibonacci:
# Solicita ao usuário o número de termos
#n = int(input("Quantos termos da sequência de Fibonacci você deseja gerar? "))

# Inicializa os dois primeiros termos
#fibonacci = [0, 1]

# Gera os termos subsequentes usando loop for
#for i in range(2, n):
   # proximo_termo = fibonacci[i-1] + fibonacci[i-2]
  #  fibonacci.append(proximo_termo)

# Ajusta para caso o usuário queira apenas 1 termo
#if n == 1:
    #fibonacci = [0]
#elif n == 0:
   # fibonacci = []

# Exibe o resultado
#print(f"Sequência de Fibonacci com {n} termos:")
#print(fibonacci[:n])


#loop while
#ex1) solicitar números até o usuario digitar 0
#tot=[]
#while True:
 #   n=int(input('Digite um número:   [0 para parar]'))
 #   if n==0:
 #       break
 #   tot.append(n)
#print(f' total de números digitados {len(tot)}')


#ex2 senha de acesso
#senha_correta = "12345"  # Senha de exemplo

#while True:
    #senha = input("Digite a senha de acesso: ")
   # if senha == senha_correta:
       # print("Acesso permitido!")
       # break
   # else:
      #  print("Senha incorreta. Tente novamente.")


#ex3) validação de idade
#while True:
  #  i=int(input('Digite uma idade:  '))
    #if 0<i<120:
   #     print(f'Idade válida registrada:{i}')
       # break
   # else:
    #    print('Idade inválida')

#ex5) soma acumulada
#n=soma=0
#while n!=-1:
    #n=int(input('Digite um número:   [-1 para parar]'))
   # soma+=n
#print(f'SOMA TOTAL {soma+1}')

#ex7) cadastrando alunos
#alunos=[]

#while alunos != "fim":
    #alunos =input('Digite o nome do aluno: ')


#print(f' Total de alunos cadastrados:{len(alunos)}')

#ex8) numeros palíndromos
#n=input('Digite um número de mais de 3 algarismos: ')
#p=n[::-1]
#print(p)
#if p==n:
  #  print(f' {n} e {p} são palíndromos')
#else:
  #  print(f'{n} e {p} não são palíndromos')

#ex10) caixa registradora
#soma=n=desconto=0
#while True:
   # n=float(input('Digite o valor do produto R$:      [0 para finalizar]'))
 #   soma+=n
  #  desconto=0.90*soma
 #   if n==0:
    #   break


#print(f' o valor total da compra é {soma} e o valor com desconto é {desconto}')













