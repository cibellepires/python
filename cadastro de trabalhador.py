cadastro=dict()
cadastro['Nome']=str(input('Digite o nome: '))
cadastro['Nascimento']=int(input('Ano de nascimento: '))
cadastro['CTPS']=int(input('Carteira de trabalho (0 não tem): '))
cadastro['Contratação']=int(input('ANo de contratação: '))
cadastro['Salário']=float(input('Salário R$ '))
print('-='*30)
for v, k in cadastro.items():
    print(f' {v} : {k}')