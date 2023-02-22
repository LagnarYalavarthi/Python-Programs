def oddindex(s):
    lst=[]
    for i in range(len(s)):
        if i%2!=0:
            lst.append(s[i])
    return lst
s="hyderabad"
#print(oddindex(s))


