def ncount(s):
    if s=="":
        return "string is empty"
    numbercount=0
    lettercount=0
    for i in s:
        if (i.isalpha()):
            lettercount+=1
        elif (i.isdigit()):
            numbercount+=1
    return lettercount,numbercount
s="lagnar12345"
print(ncount(s))
            
