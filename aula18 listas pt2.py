#listas dentro das listas
teste=list()
teste.append('Cibelle')
teste.append('22')
galera=list()
galera.append(teste[:])
teste[0]='Maria'
teste[1]='12'
galera.append(teste[:])
print(galera)

lista=[['João',19], ['Lúcia', 15], ['Lia', 23], ['Daniela', 54]]
print(lista[2][1])  # o 2 é a posição da lista e 1 é a posição da info que eu quero
for p in lista:
    print(f' {p[0]} tem {p[1]} anos de idade')
print('='*20)
#coletar dadose formar uma lista
totmenor=0
totmaior=0
pessoal=list()
dado=list()
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoal.append(dado[:]) #cria uma cópia de dados
    dado.clear()
print(pessoal)
print('='*20)
for m in pessoal:
    if m[1]>=18:
        print(f' {m[0]} é maior de idade')
        totmaior+=1
    else:
        print(f'{m[0]} é menor de idade')
        totmenor+=1
print(f'Logo, temos {totmenor} menores de idade e {totmaior} maiores de idade')
print('='*20)

