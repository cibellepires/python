# () tupla
lanche=('hamburger', 'suco','Pizza', 'Pudim')
print(lanche[3])
print(lanche[1:3])
print(lanche[:3])
print(lanche[-2:])

for cont in range(0, len(lanche)):
    print(f' eu vou comer {lanche[cont]}')

for pos, comida in enumerate(lanche):
    print(f' eu vou comer {comida} na posição {pos}')

print(sorted(lanche))

a=(2,5,4)
b=(5,8,1,2)
c=a+b
print(c)