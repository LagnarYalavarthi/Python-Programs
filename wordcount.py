def wcount(s):
    word=1
    for i in s:
        if i==" ":
            word+=1
    return word
s="i am lagnar from avanigadda"
print(wcount(s))



