def evenodd(a):
    even=[]
    odd=[]
    for i in a:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd
a=[1,99,10,28,77,37,88]
print(evenodd(a))
        
    


