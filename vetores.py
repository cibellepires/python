def main():
    a=[0,1,2,3,4]
    b=a
    print(f'a={a}')
    b[1]=7
    b[0]=1
    print(f'b={b}')
main()

def primos():
    primos=[]
    primos=primos+[9]
    primos=[2,3]+primos
