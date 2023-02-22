def largest(l):
    l.sort()
    return(l[len(l)-1])
    

#print(largest([1,9999,2,3,4989]))

def secondlargest(lst):
    lst.sort()
    return(lst[len(lst)-2])
    

#print(secondlargest([1,9999,2,3,4989]))
