
def fibanocci(n):
    a=0
    b=1
    c=1

    if (n==0) or (n==1):
        return "fib"
    while a<n:
        a=b+c
        c=b
        b=a
    if a==n:
        return "fib number"
    else:
        return "not fib"






