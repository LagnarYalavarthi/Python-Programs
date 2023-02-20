
def prime(n):
    if n == 1:
        return "neither prime nor composite"

    if n < 0:
        return "negative numbers are not prime"

    for i in range(2,n):
        if(n%i)==0:
            return "yes it is not prime"

    else:
        return "yes it is prime"

#print(prime((5)))

