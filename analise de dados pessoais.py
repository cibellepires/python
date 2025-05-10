#analisando dados
somaidade=0
mediaidade=0
maioridadehomem=0
nomevelho=' '
totmulher20=0
for p in range (1,5):
    print(f'---------{p}°PESSOA--------')
    nome=str(input('Nome: ')).strip()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo[M/F]: ')).strip()
    somaidade+=idade
    if p==1 and sexo in 'Mm':
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Mm' and idade>maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Ff' and idade<20:
        totmulher20+=1
mediaidade=somaidade/4

print(f'a média de idade do grupo é de {mediaidade} anos')
print(f' o homem mais velho é o {nomevelho} e a sua idade é {maioridadehomem}')
print(f' ao total são {totmulher20} mulheres com menos de 20 anos')
