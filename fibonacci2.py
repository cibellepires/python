#n=int(input('Quantos termos você quer mostrar?'))
#t1=0
#t2=1
#print(f'{t1}->{t2}', end=' ')
#contador=3
#while contador<=n:
   #t3=t1+t2
   #print(f'->{t3}',end=' ')
   #t1=t2
   #t2=t3
   #contador+=1
#print('FIM')

# Solicita ao usuário quantos termos da sequência de Fibonacci ele deseja ver
n = int(input("Quantos termos da sequência de Fibonacci você deseja? "))

# Inicializa os dois primeiros termos
termo1, termo2 = 0, 1
contador = 0

# Verifica se o número de termos é válido
if n <= 0:
    print("Por favor, digite um número inteiro positivo.")
elif n == 1:
    print(f"Sequência de Fibonacci com {n} termo:")
    print(termo1)
else:
    print(f"Sequência de Fibonacci com {n} termos:")
    while contador < n:
        print(termo1, end=" ")
        proximo_termo = termo1 + termo2
        # Atualiza os valores para o próximo passo
        termo1 = termo2
        termo2 = proximo_termo
        contador += 1