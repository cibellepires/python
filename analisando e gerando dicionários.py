def notas(*n, sit=False):
    # -> função para anlisar notas e situações de vários alunos
    # para n: uma ou mais notas dos alunos (aceitar varias)
    # para sit: valor opcional indicando se deve ou não adicionar a situação
    # return: dicionário com várias informações sobre a situação da turma
    r=dict()
    r['total']=len(n)
    r['maior']= max(n)
    r['nenor']= min(n)
    r['media']= sum(n)/len(n)
    if sit:
        if r['media']>7:
            r['situação']='Boa'
        elif r['media']>= 5:
            r['situação']='Razoável'
        else:
            r['sitação']='Ruim'
    return r



resp=notas(10, 4.0, 9.8, 8, sit=True)
print(resp)