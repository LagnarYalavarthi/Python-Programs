




def pallindrome(s):
    if len(s)==0:
        return 0
    
    rev=""
    for i in s:
        rev=i+rev
        if rev==s:
            return "it is pallindrome"
            break
    else:
        return "it is not pallindrome"
#print(pallindrome("lagnar"))
#print(pallindrome("racecar"))

