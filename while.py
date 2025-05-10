#contador=1
#while contador <=5:
    #print(contador)
    #contador+=1

#calculo de media de alunos

contador=1
medias=[]

while contador<=10:
    print(f' nota do aluno {contador}')
    n1=int(input('Informe a nota1: '))
    n2=int(input('Informe a nota2: '))
    media=(n1+n2)/2
    print(f' a media do aluno{contador} é {media}')
    contador+=1
    medias.append(media)
media_turma=sum(medias)/len(medias)
print(f'a média da turma é {media_turma}')

