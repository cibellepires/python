def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a
def fiblist():
    for i in range(40):
        if i>0:
            print(fib(i),end='->')

fiblist()