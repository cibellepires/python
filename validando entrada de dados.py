def leiaInt(msg):
    ok=False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print('ERRO! Digite um número interio válido')
        if ok:
            break
    return valor

n=leiaInt('Digite um número:')

print(f'Você acabou de digitar o número {n}')