
def fibanocciseries(n):
    first=0
    second=1
    lst=[]
    for i in range(n):
        #print(first,end=" ")
        temp=first
        first=second
        second=temp+first
        lst.append(temp)
    return lst
print(fibanocciseries(5))
