#pesos
pesomaior=0
pesomenor=0
for c in range (1,6,1):
    peso=float(input(f'Qual o peso da {c}° pessoa? '))
    if c==1:
        pesomaior=peso
        pesomenor=peso
    else:
        if peso>pesomaior:
           pesomaior=peso
        if peso<pesomenor:
            pesomenor=peso
print(f'o peso maior foi {pesomaior}kg ')
print(f'e o peso menor foi {pesomenor}kg')




