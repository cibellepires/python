galera=list()
pessoa=dict()
media=soma=0
while True:
    pessoa.clear()
    pessoa['nome']=str(input('Nome: '))
    while True:
        pessoa['sexo']=str(input('Sexo:   [M//F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! digite apenas M ou F!')
    pessoa['idade']=int(input('Idade:  '))
    soma+=pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp=str(input('Quer continuar?[S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erros! responda com apenas S ou N')
    if resp=='N':
        break
print('-='*30)
print(f' ao todo temos {len(galera)} pessoas cadastradas')
media=soma/len(galera)
print(f' a média de idade é de {media:.2f} anos')
print(f' as mulheres cadastradas foram',end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f' {p['nome']}',end='')
print()
print(f' lista de pessoas acima da média: ')
for p in galera:
    if p['idade']>=media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k}={v}; ', end='')
        print()
print('>>>>>>>>>>>>>>>>ENCERRADO<<<<<<<<<<<<<<<<<')