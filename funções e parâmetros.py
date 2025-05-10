
#def obter_pi():
    #return 3.141
#resultado=obter_pi()
#print(resultado)

def modificar_lista(lista):
    lista.append(4)
    lista=[1,2,3]
numeros=[1,2,3]
modificar_lista(numeros)
print(numeros)

def saudacao(nome,mensagem="Olá!"):
   print(f'{mensagem}, {nome}')
saudacao('Maria')

def calcular_retangulo(largura, altura):
    area=largura*altura
    perimetro=2*(largura+altura)
    return area,perimetro
resultado=calcular_retangulo(altura=5,largura=3)
print(resultado)

