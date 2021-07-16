#n th fib number
def fib(n):
    a=0
    b=1
    while(n-1):
        a,b=b,a+b
        n=n-1
    return a
n=int(input())
print(fib(n))
