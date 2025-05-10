def lin():
    print('-'*50)

#programa principal
lin()
print('    Curso em video      ')
print('      aprenda PYTHON     ')
lin()

def msg():
    print('Sistema de alunos')
lin()
msg()
lin()

def soma (a,b):
    s=a+b
    print(s)
#programa principal
soma(4,5)
soma(8,9)
lin()
def contador(*num):
    tam=len(num)
    print(num)
    print(f' recebi os números {num} com {tam} números')
contador(2, 3, 5)
contador(2,4,6,7,8,0)
contador(3,6,7,3,2,7,9)


lin()
def dobra(lst):
    pos=0
    while pos< len(lst):
        lst[pos]*=2
        pos+=1

valores = [3, 6, 6, 7, 7, 3, 8, 5, 9, ]
dobra(valores)
print(valores)
lin()
def soma (*valores):
    s=0
    for num in valores:
        s+=num
    print(f' somando os valores {valores} temos {s}')
soma(4,2)
soma(2,9,4)